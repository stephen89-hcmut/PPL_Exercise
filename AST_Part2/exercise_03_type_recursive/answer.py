from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "MPTypeRecursive"))

from common.ast_nodes import ArrayType, FloatType, IntType, RangeType, UnionType
from common.parser_utils import parse
from MPTypeRecursiveVisitor import MPTypeRecursiveVisitor


class ASTGeneration(MPTypeRecursiveVisitor):
    def visitProgram(self, ctx):
        return self.visit(ctx.mptype())

    def visitMptype(self, ctx):
        return self.visit(ctx.primtype() or ctx.arraytype())

    def visitPrimtype(self, ctx):
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitArraytype(self, ctx):
        element_type = self.visit(ctx.primtype())
        ranges = [self.visit(dimen) for dimen in ctx.dimens().dimen()]
        index_type = ranges[0]
        for range_type in ranges[1:]:
            index_type = UnionType(index_type, range_type)
        return ArrayType(index_type, element_type)

    def visitDimen(self, ctx):
        return RangeType(self.visit(ctx.num(0)), self.visit(ctx.num(1)))

    def visitNum(self, ctx):
        return int(ctx.getText())


def solve(source: str, start_rule: str = "program"):
    return ASTGeneration().visit(parse(source, "MPTypeRecursive", start_rule))
