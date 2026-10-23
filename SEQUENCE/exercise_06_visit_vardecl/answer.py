import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import CName, CodeGeneration, Index, Symbol


class AnswerCodeGeneration(CodeGeneration):
    def visitVarDecl(self, ctx, o):
        if o is None:
            self.emit.printout(self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False))
            return Symbol(ctx.name, ctx.typ, CName(self.className))
        index = o.getNewIndex()
        self.emit.printout(self.emit.emitVAR(index, ctx.name, ctx.typ, "start", "end"))
        return Symbol(ctx.name, ctx.typ, Index(index))


def solve(declarations):
    generator = AnswerCodeGeneration()
    return generator.run_declarations(declarations)
