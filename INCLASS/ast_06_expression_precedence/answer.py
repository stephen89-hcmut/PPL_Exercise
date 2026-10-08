import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "XExprRecursive"))
from XExprRecursiveVisitor import XExprRecursiveVisitor
from common.ast_nodes import BinOp, Num, Var
from common.parser_utils import parse


class ASTGeneration(XExprRecursiveVisitor):
	def visitExp(self, ctx):
		if ctx.getChildCount() == 1:
			return self.visit(ctx.term())
		return BinOp(ctx.getChild(1).getText(), self.visit(ctx.exp()), self.visit(ctx.term()))

	def visitTerm(self, ctx):
		if ctx.getChildCount() == 1:
			return self.visit(ctx.factor())
		return BinOp(ctx.getChild(1).getText(), self.visit(ctx.factor()), self.visit(ctx.term()))

	def visitFactor(self, ctx):
		if ctx.ID() is not None:
			return Var(ctx.ID().getText())
		if ctx.INTLIT() is not None:
			return Num(int(ctx.INTLIT().getText()))
		return self.visit(ctx.exp())


def solve(source):
	return ASTGeneration().visit(parse(source, "XExprRecursive", "exp"))
