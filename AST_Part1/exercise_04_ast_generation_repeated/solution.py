from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "repeated"))

from MPRepeatedVisitor import MPRepeatedVisitor

from common.ast_nodes import FloatType, Id, IntType, Program, VarDecl
from common.parser_utils import parse


class ASTGeneration(MPRepeatedVisitor):
    def visitProgram(self, ctx):
        return Program([v for vardecl_list in ctx.vardecl() for v in self.visit(vardecl_list)])
    def visitVardecl(self, ctx):
        return [VarDecl(id_node, self.visit(ctx.mptype())) for id_node in self.visit(ctx.ids())]

    def visitMptype(self, ctx):
        if ctx.INTTYPE():
            return IntType()
        return FloatType()
    def visitIds(self, ctx):
        return [Id(id_node.getText()) for id_node in ctx.ID()]

def solve(source: str, start_rule: str = "program") -> Program:
    tree, _ = parse(source, "repeated")
    return ASTGeneration().visit(tree)
