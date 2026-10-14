from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "MPExprRepeated"))

from common.ast_nodes import Binary, BooleanLiteral, Id, IntLiteral
from common.parser_utils import parse
from MPExprRepeatedVisitor import MPExprRepeatedVisitor


class ASTGeneration(MPExprRepeatedVisitor):
    def visitProgram(self, ctx):
        return self.visit(ctx.exp())

    def visitExp(self, ctx):
        terms = [self.visit(term) for term in ctx.term()]
        result = terms[-1]
        for index in range(len(ctx.ASSIGN()) - 1, -1, -1):
            result = Binary(ctx.ASSIGN(index).getText(), terms[index], result)
        return result

    def visitTerm(self, ctx):
        if ctx.COMPARE():
            return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
        return self.visit(ctx.factor(0))

    def visitFactor(self, ctx):
        result = self.visit(ctx.operand(0))
        for index, operator in enumerate(ctx.ANDOR()):
            result = Binary(operator.getText(), result, self.visit(ctx.operand(index + 1)))
        return result

    def visitOperand(self, ctx):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        if ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText() == "True")
        return self.visit(ctx.exp())


def solve(source: str, start_rule: str = "program"):
    return ASTGeneration().visit(parse(source, "MPExprRepeated", start_rule))
