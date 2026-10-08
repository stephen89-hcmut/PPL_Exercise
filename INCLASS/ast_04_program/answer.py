import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "XProgram"))
from XProgramVisitor import XProgramVisitor
from common.ast_nodes import FloatType, IntType, Program, VarDecl
from common.parser_utils import parse


class ASTGeneration(XProgramVisitor):
    def visitProgram(self, ctx):
        declarations = []
        for declaration in ctx.vardecl():
            declarations.extend(self.visit(declaration))
        return Program(declarations)

    def visitVardecl(self, ctx):
        typ = self.visit(ctx.typ())
        return [VarDecl(name, typ) for name in self.visit(ctx.ids())]

    def visitIds(self, ctx):
        return [token.getText() for token in ctx.ID()]

    def visitTyp(self, ctx):
        return IntType() if ctx.INTTYPE() is not None else FloatType()


def solve(source):
    return ASTGeneration().visit(parse(source, "XProgram", "program"))
