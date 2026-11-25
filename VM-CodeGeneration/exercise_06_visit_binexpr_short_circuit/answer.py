import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.runtime import BinExpr, BoolType, CodeGeneration, Emitter, FloatType, IntType, IntLiteral, FloatLiteral, BoolLiteral


class AnswerEmitter(Emitter):
    def emitANDOR(self, op, left_code, right_code, frame):
        first = frame.getNewLabel()
        second = frame.getNewLabel()
        if op == "&&":
            return (left_code + f"ifeq Label{second}\n" + right_code +
                    f"ifeq Label{second}\niconst_1\ngoto Label{first}\n"
                    f"Label{second}:\niconst_0\nLabel{first}:\n")
        if op == "||":
            return (left_code + f"ifne Label{first}\n" + right_code +
                    f"ifne Label{first}\niconst_0\ngoto Label{second}\n"
                    f"Label{first}:\niconst_1\nLabel{second}:\n")
        raise ValueError(f"unsupported logical operator: {op}")


class AnswerCodeGeneration(CodeGeneration):
    def __init__(self):
        super().__init__()
        self.emit = AnswerEmitter()

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
        op = ctx.op
        if op in ("&&", "||"):
            left_code, _ = self.generate(ctx.e1)
            right_code, _ = self.generate(ctx.e2)
            return self.emit.emitANDOR(op, left_code, right_code, o.frame), BoolType()

        left, left_type = self.generate(ctx.e1)
        right, right_type = self.generate(ctx.e2)
        comparison = op in (">", "<", ">=", "<=", "!=", "==")
        result_type = FloatType() if op == "/" or isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
        if isinstance(result_type, FloatType):
            if isinstance(left_type, IntType):
                left += self.emit.emitI2F(o.frame)
            if isinstance(right_type, IntType):
                right += self.emit.emitI2F(o.frame)
        code = left + right
        if comparison:
            return code + self.emit.emitREOP(op, result_type, o.frame), BoolType()
        if op in ("+", "-"):
            return code + self.emit.emitADDOP(op, result_type, o.frame), result_type
        if op in ("*", "/"):
            return code + self.emit.emitMULOP(op, result_type, o.frame), result_type
        raise ValueError(f"unsupported operator: {op}")


def solve(node):
    return AnswerCodeGeneration().generate(node)
