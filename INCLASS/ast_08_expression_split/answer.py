import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "XExprSplit"))
from XExprSplitVisitor import XExprSplitVisitor
from common.ast_nodes import BinOp, Num, Var
from common.parser_utils import parse


class ASTGeneration(XExprSplitVisitor):
    def visitExp(self, ctx):
        expression = self.visit(ctx.term(0))
        for index, operator in enumerate(ctx.addop()):
            expression = BinOp(self.visit(operator), expression, self.visit(ctx.term(index + 1)))
        return expression

    def visitAddop(self, ctx):
        return ctx.getText()

    def visitTerm(self, ctx):
        expression = self.visit(ctx.factor(0))
        for index, operator in enumerate(ctx.mulop()):
            expression = BinOp(self.visit(operator), expression, self.visit(ctx.factor(index + 1)))
        return expression

    def visitMulop(self, ctx):
        return ctx.getText()

    def visitFactor(self, ctx):
        if ctx.ID() is not None:
            return Var(ctx.ID().getText())
        if ctx.INTLIT() is not None:
            return Num(int(ctx.INTLIT().getText()))
        return self.visit(ctx.exp())


def solve(source):
    return ASTGeneration().visit(parse(source, "XExprSplit", "exp"))
