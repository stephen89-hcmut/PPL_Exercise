import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import CodeGeneration


class StudentCodeGeneration(CodeGeneration):
    def visitId(self, ctx, o):
        return None


def solve(case):
    generator = StudentCodeGeneration(case["symbols"])
    generator.storage.update(case["values"])
    return generator.run_expression(case["node"])
