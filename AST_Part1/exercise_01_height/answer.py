from __future__ import annotations

import sys
from pathlib import Path

from antlr4 import TerminalNode

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "recursive"))

from MPRecursiveVisitor import MPRecursiveVisitor
from common.parser_utils import parse


class Height(MPRecursiveVisitor):
    def visitProgram(self, ctx):
        return self._height(ctx)

    def _height(self, node) -> int:
        if isinstance(node, TerminalNode):
            return 1
        child_heights = [self._height(node.getChild(index)) for index in range(node.getChildCount())]
        return 1 if not child_heights else 1 + max(child_heights)


def solve(source: str, start_rule: str = "program") -> int:
    tree, _ = parse(source, "recursive", start_rule)
    return Height()._height(tree)
