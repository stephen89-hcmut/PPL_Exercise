import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import CodeGeneration, FloatType


class AnswerCodeGeneration(CodeGeneration):
    def visitFloatLiteral(self, ctx, o):
        code = self.emit.emitPUSHFCONST(ctx.value, o.frame)
        return code, FloatType()


def solve(node):
    return AnswerCodeGeneration().run_expression(node)
