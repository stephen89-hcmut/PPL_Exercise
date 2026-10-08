from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "recursive"))

from MPRecursiveVisitor import MPRecursiveVisitor

from common.ast_nodes import Program
from common.parser_utils import parse


class ASTGeneration(MPRecursiveVisitor):
    def visitProgram(self, ctx):
        return None

    def visitVardecls(self, ctx):
        return None

    def visitVardecltail(self, ctx):
        return None

    def visitVardecl(self, ctx):
        return None

    def visitMptype(self, ctx):
        return None

    def visitIds(self, ctx):
        return None


def solve(source: str, start_rule: str = "program") -> Program:
    tree, _ = parse(source, "recursive")
    return ASTGeneration().visit(tree)
