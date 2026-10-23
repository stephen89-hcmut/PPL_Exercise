import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import CodeGeneration


class AnswerCodeGeneration(CodeGeneration):
    def visitId(self, ctx, o):
        symbol = next(symbol for symbol in o.sym if symbol.name == ctx.name)
        return self.storage[ctx.name], symbol.mtype


def solve(case):
    generator = AnswerCodeGeneration(case["symbols"])
    generator.storage.update(case["values"])
    return generator.run_expression(case["node"])
