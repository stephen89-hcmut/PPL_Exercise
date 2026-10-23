import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import Access, BreakSignal, CodeGeneration, ContinueSignal, Ref


class AnswerCodeGeneration(CodeGeneration):
    def visitId(self, ctx, o):
        symbol = self.resolve(ctx.name)
        self.storage.setdefault(ctx.name, 0)
        return (Ref(self.storage, ctx.name) if o.isLeft else self.storage[ctx.name]), symbol.mtype

    def visitAssign(self, ctx, o):
        lhs = self.visitId(ctx.lhs, Access(o.frame, o.sym, True))[0]
        lhs.set(self.expression(ctx.rhs))

    def visitIf(self, ctx, o):
        if self.expression(ctx.expr):
            self.statement(ctx.tstmt)
        elif ctx.estmt is not None:
            self.statement(ctx.estmt)

    def visitFor(self, ctx, o):
        o.frame.enterLoop()
        try:
            self.visitAssign(type("AssignContext", (), {"lhs": ctx.idx, "rhs": ctx.ini})(), o)
            while self.storage[ctx.idx.name] <= self.expression(ctx.end):
                try:
                    self.statement(ctx.stmt)
                except ContinueSignal:
                    pass
                except BreakSignal:
                    break
                self.storage[ctx.idx.name] += self.expression(ctx.upd)
        finally:
            o.frame.exitLoop()


def solve(program):
    return AnswerCodeGeneration().run(program)
