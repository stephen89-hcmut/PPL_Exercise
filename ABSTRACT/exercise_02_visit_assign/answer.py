import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import Access, CodeGeneration


class AnswerCodeGeneration(CodeGeneration):
    def visitId(self, ctx, o):
        symbol = self.resolve(ctx.name)
        self.storage.setdefault(ctx.name, 0)
        if o.isLeft:
            from common.runtime import Ref
            return Ref(self.storage, ctx.name), symbol.mtype
        return self.storage[ctx.name], symbol.mtype

    def visitAssign(self, ctx, o):
        rhs = (self.expression(ctx.rhs), None)
        lhs = self.visitId(ctx.lhs, Access(o.frame, o.sym, True))
        self.emit.printout(lambda: lhs[0].set(rhs[0]))


def solve(program):
    return AnswerCodeGeneration().run(program)
