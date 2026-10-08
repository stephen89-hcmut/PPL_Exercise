from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "recursive"))

from MPRecursiveVisitor import MPRecursiveVisitor
from common.ast_nodes import FloatType, Id, IntType, Program, VarDecl
from common.parser_utils import parse


class ASTGeneration(MPRecursiveVisitor):
    def visitProgram(self, ctx):
        return Program(self.visit(ctx.vardecls()))

    def visitVardecls(self, ctx):
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecltail(self, ctx):
        if ctx.vardecl() is None:
            return []
        return self.visit(ctx.vardecl()) + self.visit(ctx.vardecltail())

    def visitVardecl(self, ctx):
        var_type = self.visit(ctx.mptype())
        return [VarDecl(variable, var_type) for variable in self.visit(ctx.ids())]

    def visitMptype(self, ctx):
        return IntType() if ctx.INTTYPE() is not None else FloatType()

    def visitIds(self, ctx):
        identifiers = [Id(ctx.ID().getText())]
        if ctx.ids() is not None:
            identifiers.extend(self.visit(ctx.ids()))
        return identifiers


def solve(source: str, start_rule: str = "program") -> Program:
    tree, _ = parse(source, "recursive")
    return ASTGeneration().visit(tree)
