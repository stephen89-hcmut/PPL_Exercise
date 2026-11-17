import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import CodeGeneration, FloatType


class StudentCodeGeneration(CodeGeneration):
    def visitFloatLiteral(self, ctx, o):
        return self.emit.emitPUSHFCONST(ctx.value, o.frame), FloatType() 


def solve(node):
    return StudentCodeGeneration().run_expression(node)
