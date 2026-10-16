import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "XExprRecursive"))

from common.ast_nodes import BinOp, Num, Var
from common.parser_utils import parse
from XExprRecursiveVisitor import XExprRecursiveVisitor

class ASTGeneration(XExprRecursiveVisitor):
    def visitExp(self, ctx):
        return None
    
    def visitTerm(self, ctx):
        return None

    def visitFactor(self, ctx):
        return None


def solve(source):
    return ASTGeneration().visit(parse(source, "XExprRecursive", "exp"))
