import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "XIdsRecursive"))
from XIdsRecursiveVisitor import XIdsRecursiveVisitor
from common.parser_utils import parse


class ASTGeneration(XIdsRecursiveVisitor):
    def visitIds(self, ctx):
        return None


def solve(source):
    return ASTGeneration().visit(parse(source, "XIdsRecursive", "start").ids())
