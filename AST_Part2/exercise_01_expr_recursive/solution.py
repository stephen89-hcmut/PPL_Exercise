from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "MPExprRecursive"))

from common.parser_utils import parse
from MPExprRecursiveVisitor import MPExprRecursiveVisitor


class ASTGeneration(MPExprRecursiveVisitor):
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
    return ASTGeneration().visit(parse(source, "MPExprRecursive", start_rule))
