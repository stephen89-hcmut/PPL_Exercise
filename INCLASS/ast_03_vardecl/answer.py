import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "XDecl"))
from XDeclVisitor import XDeclVisitor
from common.ast_nodes import FloatType, IntType, VarDecl
from common.parser_utils import parse


class ASTGeneration(XDeclVisitor):
    def visitVardecl(self, ctx):
        typ = self.visit(ctx.typ())
        return [VarDecl(name, typ) for name in self.visit(ctx.ids())]

    def visitIds(self, ctx):
        return [token.getText() for token in ctx.ID()]

    def visitTyp(self, ctx):
        return IntType() if ctx.INTTYPE() is not None else FloatType()


def solve(source):
    return ASTGeneration().visit(parse(source, "XDecl", "vardecl"))
