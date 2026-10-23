import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import CodeGeneration


class AnswerCodeGeneration(CodeGeneration):
    def visitIf(self, ctx, o):
        if self.expression(ctx.expr):
            self.statement(ctx.tstmt)
        elif ctx.estmt is not None:
            self.statement(ctx.estmt)


def solve(program):
    return AnswerCodeGeneration().run(program)
