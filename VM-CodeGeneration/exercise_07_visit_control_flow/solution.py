import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import CodeGeneration
from cases import IfCase, WhileCase, ForCase

class StudentCodeGeneration(CodeGeneration):
    def visitIf(self, ctx, o):
        return None
    def visitWhile(self, ctx, o):
        return None
    def visitFor(self, ctx, o):
        return None
    def generate(self, ctx):
        return {IfCase: self.visitIf, WhileCase: self.visitWhile, ForCase: self.visitFor}[type(ctx)](ctx, self.frame)

def solve(case):
    return StudentCodeGeneration().generate(case)
