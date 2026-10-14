from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "MPExprRecursive"))

from common.ast_nodes import Binary, BooleanLiteral, Id, IntLiteral
from common.parser_utils import parse
from MPExprRecursiveVisitor import MPExprRecursiveVisitor


class ASTGeneration(MPExprRecursiveVisitor):
    def visitProgram(self, ctx):
        return self.visit(ctx.exp())

    def visitExp(self, ctx):
        if ctx.ASSIGN():
            return Binary(ctx.ASSIGN().getText(), self.visit(ctx.term()), self.visit(ctx.exp()))
        return self.visit(ctx.term())

    def visitTerm(self, ctx):
        if ctx.COMPARE():
            return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
        return self.visit(ctx.factor(0))

    def visitFactor(self, ctx):
        if ctx.ANDOR():
            return Binary(ctx.ANDOR().getText(), self.visit(ctx.factor()), self.visit(ctx.operand()))
        return self.visit(ctx.operand())

    def visitOperand(self, ctx):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText() == "True")
        return self.visit(ctx.exp())


def solve(source: str, start_rule: str = "program"):
    return ASTGeneration().visit(parse(source, "MPExprRecursive", start_rule))
