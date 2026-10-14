from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "MPTypeRecursive"))

from common.parser_utils import parse
from MPTypeRecursiveVisitor import MPTypeRecursiveVisitor


class ASTGeneration(MPTypeRecursiveVisitor):
    def visitProgram(self, ctx):
        return None

    def visitMptype(self, ctx):
        return None

    def visitPrimtype(self, ctx):
        return None

    def visitArraytype(self, ctx):
        return None

    def visitDimens(self, ctx):
        return None

    def visitDimen(self, ctx):
        return None

    def visitNum(self, ctx):
        return None


def solve(source: str, start_rule: str = "program"):
    return ASTGeneration().visit(parse(source, "MPTypeRecursive", start_rule))
