from functools import reduce
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "XExprLoop"))
from XExprLoopVisitor import XExprLoopVisitor
from common.ast_nodes import BinOp, Num, Var
from common.parser_utils import parse


class ASTGeneration(XExprLoopVisitor):
    def visitExp(self, ctx):
        return None

    def visitTerm(self, ctx):
        return None

    def visitFactor(self, ctx):
        if ctx.ID():
            return Var(ctx.ID().getText())
        if ctx.INTLIT():
            return Num(int(ctx.INTLIT().getText()))
        return self.visit(ctx.exp()) 


def solve(source):
    return ASTGeneration().visit(parse(source, "XExprLoop", "exp"))
