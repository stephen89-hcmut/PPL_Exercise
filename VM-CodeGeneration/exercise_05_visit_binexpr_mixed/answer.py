import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import BoolType, CodeGeneration, FloatType, IntType


class AnswerCodeGeneration(CodeGeneration):
    def visitIntLiteral(self, ctx, o):
        return self.emit.emitPUSHICONST(ctx.value, o.frame), IntType()

    def visitFloatLiteral(self, ctx, o):
        return self.emit.emitPUSHFCONST(ctx.value, o.frame), FloatType()

    def visitBinExpr(self, ctx, o):
        e1c, e1t = self.visit(ctx.e1, o)
        e2c, e2t = self.visit(ctx.e2, o)
        op = ctx.op
        comparison = op in (">", "<", ">=", "<=", "!=", "==")
        numeric_type = FloatType() if isinstance(e1t, FloatType) or isinstance(e2t, FloatType) or op == "/" else IntType()
        if isinstance(numeric_type, FloatType):
            if isinstance(e1t, IntType): e1c += self.emit.emitI2F(o.frame)
            if isinstance(e2t, IntType): e2c += self.emit.emitI2F(o.frame)
        code = e1c + e2c
        if comparison:
            return code + self.emit.emitREOP(op, numeric_type, o.frame), BoolType()
        if op in ("+", "-"):
            return code + self.emit.emitADDOP(op, numeric_type, o.frame), numeric_type
        if op in ("*", "/"):
            return code + self.emit.emitMULOP(op, numeric_type, o.frame), numeric_type
        raise ValueError(f"unsupported operator: {op}")


def solve(node):
    return AnswerCodeGeneration().run_expression(node)
