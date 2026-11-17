import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import CodeGeneration, Index


class AnswerCodeGeneration(CodeGeneration):
    def visitId(self, ctx, o):
        symbol = next(symbol for symbol in o.sym if symbol.name == ctx.name)
        if isinstance(symbol.value, Index):
            code = self.emit.emitREADVAR(ctx.name, symbol.mtype, symbol.value.value, o.frame)
        else:
            code = self.emit.emitGETSTATIC(f"{symbol.value.value}/{ctx.name}", symbol.mtype, o.frame)
        return code, symbol.mtype


def solve(case):
    generator = AnswerCodeGeneration(case["symbols"])
    generator.storage.update(case["values"])
    return generator.run_expression(case["node"])
