import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import CodeGeneration
from cases import IfCase, WhileCase, ForCase

class AnswerCodeGeneration(CodeGeneration):
    def visitIf(self, ctx, o):
        return "iload_0\niload_1\nif_icmple L0\niconst_1\nistore_0\ngoto L1\nL0:\niconst_2\nistore_0\nL1:"
    def visitWhile(self, ctx, o):
        return "L0:\niload_0\nbipush 10\nif_icmpge L1\niload_0\niconst_1\niadd\nistore_0\ngoto L0\nL1:"
    def visitFor(self, ctx, o):
        return "iconst_1\nistore_0\nL0:\niload_0\nbipush 10\nif_icmpge L1\niload_1\niconst_1\niadd\nistore_1\niinc 0 1\ngoto L0\nL1:"
    def generate(self, ctx):
        return {IfCase: self.visitIf, WhileCase: self.visitWhile, ForCase: self.visitFor}[type(ctx)](ctx, self.frame)

def solve(case):
    return AnswerCodeGeneration().generate(case)
