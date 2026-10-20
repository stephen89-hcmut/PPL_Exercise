from Type_Part1.common.ast_nodes import BoolLit, FloatLit, IntLit, TypeMismatchInExpression


class StaticCheck:
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

    def visitIntLit(self, ctx: IntLit, o):
        return int

    def visitFloatLit(self, ctx: FloatLit, o):
        return float

    def visitBoolLit(self, ctx: BoolLit, o):
        return bool
