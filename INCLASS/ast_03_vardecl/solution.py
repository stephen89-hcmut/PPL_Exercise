import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "XDecl"))
from XDeclVisitor import XDeclVisitor
from common.ast_nodes import Decl
from common.parser_utils import parse


class ASTGeneration(XDeclVisitor):
    def visitVardecl(self, ctx):
        return None

    def visitIds(self, ctx):
        return None

    def visitTyp(self, ctx):
        return None


def solve(source):
    return ASTGeneration().visit(parse(source, "XDecl", "vardecl"))
