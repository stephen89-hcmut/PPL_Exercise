from Type_Part1.common.ast_nodes import (
    BoolType, FloatType, IntType, RedeclaredDeclaration,
    TypeMismatchInExpression, UndeclaredIdentifier,
)


class StaticCheck:
    def visitProgram(self, ctx, o=None):
        environment = {}
        for declaration in ctx.decl:
            declaration.accept(self, environment)
        return ctx.exp.accept(self, environment)

    def visitVarDecl(self, ctx, o):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        o[ctx.name] = ctx.typ.accept(self, o)
        return o[ctx.name]

    def visitIntType(self, ctx, o):
        return int

    def visitFloatType(self, ctx, o):
        return float

    def visitBoolType(self, ctx, o):
        return bool

    def visitBinOp(self, ctx, o):
        left = ctx.e1.accept(self, o)
        right = ctx.e2.accept(self, o)
        if ctx.op in {"+", "-", "*"}:
            if left not in {int, float} or right not in {int, float}:
                raise TypeMismatchInExpression(ctx)
            return float if float in {left, right} else int
        if ctx.op == "/":
            if left not in {int, float} or right not in {int, float}:
                raise TypeMismatchInExpression(ctx)
            return float
        if ctx.op in {"&&", "||"}:
            if left is not bool or right is not bool:
                raise TypeMismatchInExpression(ctx)
            return bool
        if ctx.op in {">", "<", "==", "!="}:
            if left is not right:
                raise TypeMismatchInExpression(ctx)
            return bool
        raise ValueError(f"Unsupported binary operator: {ctx.op}")

    def visitUnOp(self, ctx, o):
        value = ctx.e.accept(self, o)
        if ctx.op == "!":
            if value is not bool:
                raise TypeMismatchInExpression(ctx)
            return bool
        if ctx.op == "-":
            if value not in {int, float}:
                raise TypeMismatchInExpression(ctx)
            return value
        raise ValueError(f"Unsupported unary operator: {ctx.op}")

    def visitIntLit(self, ctx, o):
        return int

    def visitFloatLit(self, ctx, o):
        return float

    def visitBoolLit(self, ctx, o):
        return bool

    def visitId(self, ctx, o):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)
        return o[ctx.name]
