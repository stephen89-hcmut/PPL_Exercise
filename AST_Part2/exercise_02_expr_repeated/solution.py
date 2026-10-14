from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "MPExprRepeated"))

from common.parser_utils import parse
from MPExprRepeatedVisitor import MPExprRepeatedVisitor


class ASTGeneration(MPExprRepeatedVisitor):
    def visitProgram(self, ctx):
        return None

    def visitExp(self, ctx):
        return None

    def visitTerm(self, ctx):
        return None

    def visitFactor(self, ctx):
        return None

    def visitOperand(self, ctx):
        return None


def solve(source: str, start_rule: str = "program"):
    return ASTGeneration().visit(parse(source, "MPExprRepeated", start_rule))
