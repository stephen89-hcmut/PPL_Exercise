import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import CodeGeneration, IntType


class AnswerCodeGeneration(CodeGeneration):
    def visitIntLiteral(self, ctx, o):
        return ctx.value, IntType()


def solve(node):
    return AnswerCodeGeneration().run_expression(node)
