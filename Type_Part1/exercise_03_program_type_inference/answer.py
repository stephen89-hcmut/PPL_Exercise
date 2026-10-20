from Type_Part1.common.type2_nodes import (
    Assign, BinOp, BoolLit, FloatLit, Id, IntLit, TypeCannotBeInferred,
    TypeMismatchInExpression, TypeMismatchInStatement, UndeclaredIdentifier,
    Redeclared, UnOp,
)


UNKNOWN = object()


def lookup(name, env):
    if name not in env:
        raise UndeclaredIdentifier(name)
    return env[name]


class StaticCheck:
    def visit(self, node, o=None):
        return node.accept(self, o)

    def visitProgram(self, ctx, o=None):
        env = {}
        for declaration in ctx.decl:
            if declaration.name in env:
                raise Redeclared(declaration)
            env[declaration.name] = UNKNOWN
        for statement in ctx.stmts:
            self.visit(statement, env)

    def visitVarDecl(self, ctx, o):
        return UNKNOWN

    def _set_id(self, expression, expected, env):
        if isinstance(expression, Id):
            current = lookup(expression.name, env)
            if current is UNKNOWN:
                env[expression.name] = expected
            elif current is not expected:
                raise TypeMismatchInExpression(expression)
            return expected
        return self._infer(expression, env, expected)

    def _infer(self, expression, env, expected):
        if isinstance(expression, Id):
            current = lookup(expression.name, env)
            if current is UNKNOWN and expected is not None:
                env[expression.name] = expected
                return expected
            return current
        if isinstance(expression, IntLit):
            actual = int
        elif isinstance(expression, FloatLit):
            actual = float
        elif isinstance(expression, BoolLit):
            actual = bool
        elif isinstance(expression, UnOp):
            required = {"-": int, "-.": float, "!": bool, "i2f": int, "floor": float}
            if expression.op not in required:
                raise ValueError(f"Unsupported unary operator: {expression.op}")
            operand_type = required[expression.op]
            self._set_id(expression.e, operand_type, env)
            actual = float if expression.op == "i2f" else int if expression.op == "floor" else operand_type
        elif isinstance(expression, BinOp):
            rules = {
                "+": (int, int), "-": (int, int), "*": (int, int), "/": (int, int),
                "+.": (float, float), "-.": (float, float),
                "*.": (float, float), "/.": (float, float),
                ">": (int, bool), "=": (int, bool),
                ">.": (float, bool), "=.": (float, bool),
                "&&": (bool, bool), "||": (bool, bool),
                ">b": (bool, bool), "=b": (bool, bool),
            }
            if expression.op not in rules:
                raise ValueError(f"Unsupported binary operator: {expression.op}")
            operand_type, actual = rules[expression.op]
            for operand in (expression.e1, expression.e2):
                try:
                    self._set_id(operand, operand_type, env)
                except TypeMismatchInExpression:
                    if isinstance(operand, (IntLit, FloatLit, BoolLit, Id)):
                        raise TypeMismatchInExpression(expression)
                    raise
        else:
            raise ValueError(f"Unsupported expression: {expression!r}")
        if expected is not None and actual is not expected:
            raise TypeMismatchInExpression(expression)
        return actual

    def visitAssign(self, ctx, o):
        lhs_type = lookup(ctx.lhs.name, o)
        if lhs_type is not UNKNOWN and isinstance(ctx.rhs, (IntLit, FloatLit, BoolLit)):
            if self._infer(ctx.rhs, o, None) is not lhs_type:
                raise TypeMismatchInStatement(ctx)
        rhs_type = self._infer(ctx.rhs, o, None if lhs_type is UNKNOWN else lhs_type)
        lhs_type = lookup(ctx.lhs.name, o)
        if lhs_type is UNKNOWN and rhs_type is not UNKNOWN:
            o[ctx.lhs.name] = rhs_type
        elif lhs_type is UNKNOWN:
            raise TypeCannotBeInferred(ctx)
        elif lhs_type is not rhs_type:
            raise TypeMismatchInStatement(ctx)

    def visitBinOp(self, ctx, o):
        return self._infer(ctx, o, None)

    def visitUnOp(self, ctx, o):
        return self._infer(ctx, o, None)

    def visitIntLit(self, ctx, o):
        return int

    def visitFloatLit(self, ctx, o):
        return float

    def visitBoolLit(self, ctx, o):
        return bool

    def visitId(self, ctx, o):
        return lookup(ctx.name, o)
