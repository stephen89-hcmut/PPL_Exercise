import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import BinExpr, CodeGeneration, Emitter, BoolLiteral, BoolType, FloatLiteral, FloatType, IntLiteral, IntType


class StudentEmitter(Emitter):
    def emitANDOR(self, op, left_code, right_code, frame):
        return None


class StudentCodeGeneration(CodeGeneration):
    def __init__(self):
        super().__init__()
        self.emit = StudentEmitter()

    def generate(self, node):
        if isinstance(node, IntLiteral):
            return self.emit.emitPUSHICONST(node.value, self.frame), IntType()
        if isinstance(node, FloatLiteral):
            return self.emit.emitPUSHFCONST(node.value, self.frame), FloatType()
        if isinstance(node, BoolLiteral):
            return self.emit.emitPUSHICONST(int(node.value), self.frame), BoolType()
        if isinstance(node, BinExpr):
            return self.visitBinExpr(node, type("O", (), {"frame": self.frame})())
        raise TypeError(f"unsupported expression: {node!r}")

    def visitBinExpr(self, ctx, o):
        return None


def solve(node):
    return StudentCodeGeneration().generate(node)
