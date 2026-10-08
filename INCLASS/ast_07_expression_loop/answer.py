import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "XExprLoop"))
from XExprLoopVisitor import XExprLoopVisitor
from common.ast_nodes import BinOp, Num, Var
from common.parser_utils import parse


class ASTGeneration(XExprLoopVisitor):
    def visitExp(self, ctx):
        expression = self.visit(ctx.getChild(0))
        for index in range(1, ctx.getChildCount(), 2):
            expression = BinOp(ctx.getChild(index).getText(), expression, self.visit(ctx.getChild(index + 1)))
        return expression

    def visitTerm(self, ctx):
        expression = self.visit(ctx.getChild(0))
        for index in range(1, ctx.getChildCount(), 2):
            expression = BinOp(ctx.getChild(index).getText(), expression, self.visit(ctx.getChild(index + 1)))
        return expression

    def visitFactor(self, ctx):
        if ctx.ID() is not None:
            return Var(ctx.ID().getText())
        if ctx.INTLIT() is not None:
            return Num(int(ctx.INTLIT().getText()))
        return self.visit(ctx.exp())


def solve(source):
    return ASTGeneration().visit(parse(source, "XExprLoop", "exp"))
