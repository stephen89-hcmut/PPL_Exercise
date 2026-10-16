from functools import reduce
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "XExprSplit"))
from common.ast_nodes import BinOp, Num, Var
from XExprSplitVisitor import XExprSplitVisitor
from common.parser_utils import parse


class ASTGeneration(XExprSplitVisitor):
    def visitExp(self, ctx):
        return None

    def visitAddop(self, ctx):
        if ctx.ADDOP():
            return ctx.ADDOP().getText()
        return ctx.SUBOP().getText() 

    def visitTerm(self, ctx):
        return None

    def visitMulop(self, ctx):
        if ctx.MULOP():
            return ctx.MULOP().getText()
        return ctx.DIVOP().getText()

    def visitFactor(self, ctx):
        if ctx.ID():
            return Var(ctx.ID().getText())
        if ctx.INT():
            return Num(int(ctx.INT().getText()))
        return self.visit(ctx.exp())

def solve(source):
    return ASTGeneration().visit(parse(source, "XExprSplit", "exp"))
