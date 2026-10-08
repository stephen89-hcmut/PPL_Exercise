from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "repeated"))

from MPRepeatedVisitor import MPRepeatedVisitor

from common.ast_nodes import FloatType, Id, IntType, Program, VarDecl
from common.parser_utils import parse


class ASTGeneration(MPRepeatedVisitor):
    def visitProgram(self, ctx):
        declarations = []
        for declaration in ctx.vardecl():
            declarations.extend(self.visit(declaration))
        return Program(declarations)

    def visitVardecl(self, ctx):
        var_type = self.visit(ctx.mptype())
        return [VarDecl(identifier, var_type) for identifier in self.visit(ctx.ids())]

    def visitMptype(self, ctx):
        return IntType() if ctx.INTTYPE() is not None else FloatType()

    def visitIds(self, ctx):
        return [Id(identifier.getText()) for identifier in ctx.ID()]


def solve(source: str, start_rule: str = "program") -> Program:
    tree, _ = parse(source, "repeated")
    return ASTGeneration().visit(tree)
