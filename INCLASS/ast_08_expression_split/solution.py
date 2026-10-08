import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "XExprSplit"))
from XExprSplitVisitor import XExprSplitVisitor
from common.parser_utils import parse


class ASTGeneration(XExprSplitVisitor):
    def visitExp(self, ctx):
        return None

    def visitAddop(self, ctx):
        return None

    def visitTerm(self, ctx):
        return None

    def visitMulop(self, ctx):
        return None


def solve(source):
    return ASTGeneration().visit(parse(source, "XExprSplit", "exp"))
