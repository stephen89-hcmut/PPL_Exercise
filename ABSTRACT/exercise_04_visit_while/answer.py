import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import BreakSignal, CodeGeneration, ContinueSignal


class AnswerCodeGeneration(CodeGeneration):
    def visitId(self, ctx, o):
        symbol = self.resolve(ctx.name)
        self.storage.setdefault(ctx.name, 0)
        from common.runtime import Ref
        return (Ref(self.storage, ctx.name) if o.isLeft else self.storage[ctx.name]), symbol.mtype

    def visitAssign(self, ctx, o):
        lhs = self.visitId(ctx.lhs, type("A", (), {"isLeft": True, "frame": o.frame, "sym": o.sym})())
        rhs = self.expression(ctx.rhs)
        lhs[0].set(rhs)

    def visitIf(self, ctx, o):
        if self.expression(ctx.expr):
            self.statement(ctx.tstmt)
        elif ctx.estmt is not None:
            self.statement(ctx.estmt)

    def visitWhile(self, ctx, o):
        o.frame.enterLoop()
        try:
            while self.expression(ctx.expr):
                try:
                    self.statement(ctx.stmt)
                except ContinueSignal:
                    continue
                except BreakSignal:
                    break
        finally:
            o.frame.exitLoop()


def solve(program):
    return AnswerCodeGeneration().run(program)
