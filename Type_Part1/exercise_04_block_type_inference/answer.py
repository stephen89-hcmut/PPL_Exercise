from Type_Part1.common.type2_nodes import (
    BoolLit, FloatLit, IntLit, TypeCannotBeInferred,
    TypeMismatchInExpression, TypeMismatchInStatement, UndeclaredIdentifier,
    Redeclared, Id, BinOp, UnOp,
)


UNKNOWN = object()


def lookup(name, env):
    for scope in env:
        if name in scope:
            return scope[name]
    raise UndeclaredIdentifier(name)


def require(value, node):
    if value is UNKNOWN:
        raise TypeCannotBeInferred(node)
    return value


class StaticCheck:
    def visit(self, node, o=None):
        return node.accept(self, o)

    def visitProgram(self, ctx, o=None):
        scope = {}
        self._declare(ctx.decl, scope)
        env = [scope]
        for stmt in ctx.stmts:
            self.visit(stmt, env)

    def _declare(self, declarations, scope):
        for declaration in declarations:
            if declaration.name in scope:
                raise Redeclared(declaration)
            scope[declaration.name] = UNKNOWN

    def visitVarDecl(self, ctx, o):
        return UNKNOWN

    def visitBlock(self, ctx, o):
        scope = {}
        self._declare(ctx.decl, scope)
        env = [scope] + o
        for stmt in ctx.stmts:
            self.visit(stmt, env)

    def visitAssign(self, ctx, o):
        rhs = self.visit(ctx.rhs, o)
        lhs = lookup(ctx.lhs.name, o)
        if lhs is UNKNOWN and rhs is UNKNOWN:
            raise TypeCannotBeInferred(ctx)
        if lhs is UNKNOWN:
            self._set(ctx.lhs.name, rhs, o)
        elif rhs is UNKNOWN:
            self._set_from_expression(ctx.rhs, lhs, o)
        elif lhs is not rhs:
            raise TypeMismatchInStatement(ctx)

    def _set(self, name, value, env):
        for scope in env:
            if name in scope:
                scope[name] = value
                return

    def _set_from_expression(self, expression, expected, env):
        if isinstance(expression, Id):
            self._set(expression.name, expected, env)
            return
        if isinstance(expression, BinOp):
            self._infer_bin(expression, expected, env)
            return
        if isinstance(expression, UnOp):
            if expression.op in {"i2f", "floor"}:
                self._set_from_expression(expression.e, int if expression.op == "i2f" else float, env)
                return
        raise TypeCannotBeInferred(expression)

    def visitBinOp(self, ctx, o):
        left, right = self.visit(ctx.e1, o), self.visit(ctx.e2, o)
        if left is UNKNOWN or right is UNKNOWN:
            raise TypeCannotBeInferred(ctx)
        groups = {
            "int": ({"+", "-", "*", "/"}, int),
            "float": ({"+.", "-.", "*.", "/."}, float),
            "bool": ({">b", "=b", "&&", "||"}, bool),
        }
        for result, (operators, operand) in groups.items():
            if ctx.op in operators:
                if left is not operand or right is not operand:
                    raise TypeMismatchInExpression(ctx)
                return bool if ctx.op in {">b", "=b"} else operand
        if ctx.op in {">", "="}:
            if left is not int or right is not int:
                raise TypeMismatchInExpression(ctx)
            return bool
        if ctx.op in {">.", "=."}:
            if left is not float or right is not float:
                raise TypeMismatchInExpression(ctx)
            return bool
        raise ValueError(f"Unsupported binary operator: {ctx.op}")

    def _infer_bin(self, ctx, expected, env):
        self._set_from_expression(ctx.e1, int if ctx.op in {"+", "-", "*", "/"} else float, env)
        self._set_from_expression(ctx.e2, int if ctx.op in {"+", "-", "*", "/"} else float, env)

    def visitUnOp(self, ctx, o):
        value = self.visit(ctx.e, o)
        if value is UNKNOWN:
            raise TypeCannotBeInferred(ctx)
        required = {"-": int, "-.": float, "!": bool, "i2f": int, "floor": float}
        if ctx.op not in required:
            raise ValueError(f"Unsupported unary operator: {ctx.op}")
        if value is not required[ctx.op]:
            raise TypeMismatchInExpression(ctx)
        return float if ctx.op == "i2f" else int if ctx.op == "floor" else value

    def visitIntLit(self, ctx, o):
        return int

    def visitFloatLit(self, ctx, o):
        return float

    def visitBoolLit(self, ctx, o):
        return bool

    def visitId(self, ctx, o):
        return lookup(ctx.name, o)
