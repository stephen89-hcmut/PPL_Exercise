import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import Access, CodeGeneration, Ref


class AnswerCodeGeneration(CodeGeneration):
    def visitId(self, ctx, o: Access):
        symbol = self.resolve(ctx.name)
        self.storage.setdefault(ctx.name, 0)
        if o.isLeft:
            code = self.emit.emitWRITEVAR(ctx.name, symbol.mtype, symbol.value, o.frame)
            return Ref(self.storage, ctx.name), symbol.mtype
        if symbol.value.__class__.__name__ == "Index":
            code = self.emit.emitREADVAR(ctx.name, symbol.mtype, symbol.value.value, o.frame)
        else:
            code = self.emit.emitGETSTATIC(f"{symbol.value.value}/{ctx.name}", symbol.mtype, o.frame)
        return self.storage[ctx.name], symbol.mtype


def solve(program):
    return AnswerCodeGeneration().run(program)
