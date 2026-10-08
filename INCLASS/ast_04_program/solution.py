import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "generated" / "XProgram"))
from XProgramVisitor import XProgramVisitor
from common.ast_nodes import Program
from common.parser_utils import parse


class ASTGeneration(XProgramVisitor):
    def visitProgram(self, ctx):
        return None


def solve(source):
    return ASTGeneration().visit(parse(source, "XProgram", "program"))
