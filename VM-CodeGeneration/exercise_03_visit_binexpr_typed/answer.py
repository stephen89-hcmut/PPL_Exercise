import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import CodeGeneration, FloatType, IntType


class AnswerCodeGeneration(CodeGeneration):
    def visitIntLiteral(self, ctx, o):
        return ctx.value, IntType()

    def visitFloatLiteral(self, ctx, o):
        return ctx.value, FloatType()

    def visitBinExpr(self, ctx, o):
        left, _ = self.eval_expr(ctx.e1)
        right, _ = self.eval_expr(ctx.e2)
        if ctx.op == "+":
            return left + right, IntType()
        if ctx.op == "-":
            return left - right, IntType()
        if ctx.op == "*":
            return left * right, IntType()
        if ctx.op == "/":
            return int(left / right), IntType()
        op = ctx.op[0]
        if op == "+":
            return float(left) + float(right), FloatType()
        if op == "-":
            return float(left) - float(right), FloatType()
        if op == "*":
            return float(left) * float(right), FloatType()
        return float(left) / float(right), FloatType()


def solve(node):
    return AnswerCodeGeneration().run_expression(node)
