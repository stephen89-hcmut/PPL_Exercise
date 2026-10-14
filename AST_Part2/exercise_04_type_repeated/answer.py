from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "MPTypeRepeated"))

from common.ast_nodes import ArrayType, FloatType, IntType, RangeType, UnionType
from common.parser_utils import parse
from MPTypeRepeatedVisitor import MPTypeRepeatedVisitor


class ASTGeneration(MPTypeRepeatedVisitor):
    def visitProgram(self, ctx):
        return self.visit(ctx.mptype())

    def visitMptype(self, ctx):
        return self.visit(ctx.primtype() or ctx.arraytype())

    def visitPrimtype(self, ctx):
        return IntType() if ctx.INTTYPE() else FloatType()

    def visitArraytype(self, ctx):
        if ctx.primtype():
            element_type = self.visit(ctx.primtype())
            return ArrayType(self.visit(ctx.dimen()), element_type)
        previous = self.visit(ctx.arraytype())
        index_type = UnionType(previous.indexType, self.visit(ctx.dimen()))
        return ArrayType(index_type, previous.eleType)

    def visitDimen(self, ctx):
        return RangeType(self.visit(ctx.num(0)), self.visit(ctx.num(1)))

    def visitNum(self, ctx):
        return int(ctx.getText())


def solve(source: str, start_rule: str = "program"):
    return ASTGeneration().visit(parse(source, "MPTypeRepeated", start_rule))
