import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "XIdsLoop"))
from XIdsLoopVisitor import XIdsLoopVisitor
from common.parser_utils import parse


class ASTGeneration(XIdsLoopVisitor):
    def visitIds(self, ctx):
        return None


def solve(source):
    return ASTGeneration().visit(parse(source, "XIdsLoop", "ids"))
