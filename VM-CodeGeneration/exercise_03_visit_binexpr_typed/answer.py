import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import CodeGeneration, FloatType, IntType


class AnswerCodeGeneration(CodeGeneration):
    def visitIntLiteral(self, ctx, o):
        return self.emit.emitPUSHICONST(ctx.value, o.frame), IntType()

    def visitFloatLiteral(self, ctx, o):
        return self.emit.emitPUSHFCONST(ctx.value, o.frame), FloatType()

    def visitBinExpr(self, ctx, o):
        e1c, _ = self.visit(ctx.e1, o)
        e2c, _ = self.visit(ctx.e2, o)
        op = ctx.op
        if op in ("+", "-"):
            return e1c + e2c + self.emit.emitADDOP(op, IntType(), o.frame), IntType()
        if op in ("+.", "-."):
            return e1c + e2c + self.emit.emitADDOP(op[0], FloatType(), o.frame), FloatType()
        if op in ("*", "/"):
            return e1c + e2c + self.emit.emitMULOP(op, IntType(), o.frame), IntType()
        if op in ("*.", "/."):
            return e1c + e2c + self.emit.emitMULOP(op[0], FloatType(), o.frame), FloatType()
        raise ValueError(f"unsupported operator: {op}")


def solve(node):
    return AnswerCodeGeneration().run_expression(node)
