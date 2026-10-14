from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "MPTypeRepeated"))

from common.parser_utils import parse
from MPTypeRepeatedVisitor import MPTypeRepeatedVisitor


class ASTGeneration(MPTypeRepeatedVisitor):
    def visitProgram(self, ctx):
        return None

    def visitMptype(self, ctx):
        return None

    def visitPrimtype(self, ctx):
        return None

    def visitArraytype(self, ctx):
        return None

    def visitDimen(self, ctx):
        return None

    def visitNum(self, ctx):
        return None


def solve(source: str, start_rule: str = "program"):
    return ASTGeneration().visit(parse(source, "MPTypeRepeated", start_rule))
