from __future__ import annotations

import sys
from pathlib import Path

from antlr4 import ParserRuleContext

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "recursive"))

from MPRecursiveVisitor import MPRecursiveVisitor
from common.parser_utils import parse


class NonTerminalCount(MPRecursiveVisitor):
    def visitProgram(self, ctx):
        return self._count(ctx)

    def _count(self, node) -> int:
        if not isinstance(node, ParserRuleContext):
            return 0
        return 1 + sum(self._count(node.getChild(index)) for index in range(node.getChildCount()))


def solve(source: str, start_rule: str = "program") -> int:
    tree, _ = parse(source, "recursive")
    return NonTerminalCount().visit(tree)
