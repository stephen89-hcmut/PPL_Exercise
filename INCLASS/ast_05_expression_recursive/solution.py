import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "XExprRecursive"))
from XExprRecursiveVisitor import XExprRecursiveVisitor
from common.parser_utils import parse


class ASTGeneration(XExprRecursiveVisitor):
    def visitExp(self, ctx):
        return None

    def visitTerm(self, ctx):
        return None

    def visitFactor(self, ctx):
        return None


def solve(source):
    return ASTGeneration().visit(parse(source, "XExprRecursive", "exp"))
