import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import CodeGeneration, FloatType, IntType


class StudentCodeGeneration(CodeGeneration):
    def visitIntLiteral(self, ctx, o):
        return self.emit.emitPUSHICONST(ctx.value, o.frame), IntType()

    def visitFloatLiteral(self, ctx, o):
        return self.emit.emitPUSHFCONST(ctx.value, o.frame), FloatType()

    def visitBinExpr(self, ctx, o):
        e1c, e1t = self.visit(ctx.e1, o)
        e2c, e2t = self.visit(ctx.e2, o)
        op = ctx.op
        if op in ['+', '-']:
            return e1c + e2c + self.emit.emitADDOP(op, IntType(), o.frame), IntType()
        elif op in ['+.', '-.']:
            return e1c + e2c + self.emit.emitADDOP(op[0], FloatType(), o.frame), FloatType()
        elif op in ['*', '/']:
            return e1c + e2c + self.emit.emitMULOP(op, IntType(), o.frame), IntType()
        elif op in ['*.', '/.']:
            return e1c + e2c + self.emit.emitMULOP(op[0], FloatType(), o.frame), FloatType()


def solve(node):
    return StudentCodeGeneration().run_expression(node)
