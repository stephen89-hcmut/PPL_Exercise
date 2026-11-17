import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import CName, CodeGeneration, Index


class AnswerCodeGeneration(CodeGeneration):
    def visitId(self, ctx, o):
        for symbol in o.sym:
            if symbol.name != ctx.name:
                continue
            if isinstance(symbol.value, Index):
                if getattr(o, "isLeft", False):
                    code = self.emit.emitWRITEVAR(ctx.name, symbol.mtype, symbol.value.value, o.frame)
                else:
                    code = self.emit.emitREADVAR(ctx.name, symbol.mtype, symbol.value.value, o.frame)
            elif isinstance(symbol.value, CName):
                field = f"{symbol.value.value}/{ctx.name}"
                if getattr(o, "isLeft", False):
                    code = self.emit.emitPUTSTATIC(field, symbol.mtype, o.frame)
                else:
                    code = self.emit.emitGETSTATIC(field, symbol.mtype, o.frame)
            else:
                raise TypeError(f"unsupported symbol value: {symbol.value!r}")
            return code, symbol.mtype
        raise NameError(f"undeclared identifier: {ctx.name}")


def solve(case):
    generator = AnswerCodeGeneration(case["symbols"])
    generator.storage.update(case["values"])
    return generator.run_expression(case["node"])
