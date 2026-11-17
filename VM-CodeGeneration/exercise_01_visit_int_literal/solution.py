import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import CodeGeneration, IntType


class StudentCodeGeneration(CodeGeneration):
    def visitIntLiteral(self, ctx, o):
        return self.emit.emitPUSHICONST(ctx.value, o.frame), IntType()


def solve(node):
    return StudentCodeGeneration().run_expression(node)
