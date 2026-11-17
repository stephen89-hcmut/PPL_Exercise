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
        op = ctx.op
        exp1, typ1 = self.visit(ctx.e1, o)
        exp2, typ2 = self.visit(ctx.e2, o)
        mtype = FloatType() if isinstance(typ1, FloatType) or isinstance(typ2, FloatType) else IntType()
        if op == "/":
            mtype = FloatType()
        if isinstance(mtype, FloatType):
            if isinstance(typ1, IntType): exp1 += self.emit.emitI2F(o.frame)
            if isinstance(typ2, IntType): exp2 += self.emit.emitI2F(o.frame)
        if op in (">", "<", ">=", "<=", "!=", "=="):
            return exp1 + exp2 + self.emit.emitREOP(op, mtype, o.frame), BoolType()
        if op in ("+", "-"):
            return exp1 + exp2 + self.emit.emitADDOP(op, mtype, o.frame), mtype
        if op in ("*", "/"):
            return exp1 + exp2 + self.emit.emitMULOP(op, mtype, o.frame), mtype
        raise ValueError(f"unsupported operator: {op}")


def solve(node):
    generator = AnswerCodeGeneration()
    generator.float_division = True
    return generator.run_expression(node)
