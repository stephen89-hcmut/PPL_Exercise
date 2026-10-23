from __future__ import annotations

from dataclasses import dataclass


class IntType:
    def __repr__(self):
        return "IntType"


class FloatType:
    def __repr__(self):
        return "FloatType"


class BoolType:
    def __repr__(self):
        return "BoolType"


@dataclass
class Index:
    value: int


@dataclass
class CName:
    value: str


@dataclass
class Symbol:
    name: str
    mtype: object
    value: Index | CName


@dataclass
class IntLiteral:
    value: int


@dataclass
class FloatLiteral:
    value: float


@dataclass
class BoolLiteral:
    value: bool


@dataclass
class Id:
    name: str


@dataclass
class BinExpr:
    op: str
    e1: object
    e2: object


@dataclass
class VarDecl:
    name: str
    typ: object


class Frame:
    def __init__(self):
        self.next_index = 0

    def getNewIndex(self):
        index = self.next_index
        self.next_index += 1
        return index


class Emitter:
    def __init__(self):
        self.output = []

    def printout(self, text):
        self.output.append(str(text))

    def emitPUSHICONST(self, value, _):
        return str(value)

    def emitPUSHFCONST(self, value, _):
        return str(value)

    def emitREADVAR(self, name, *_):
        return f"READVAR({name})"

    def emitGETSTATIC(self, name, *_):
        return f"GETSTATIC({name})"

    def emitATTRIBUTE(self, name, typ, _):
        return f".field static {name} {'I' if isinstance(typ, IntType) else 'F'}"

    def emitVAR(self, index, name, typ, *_):
        return f".var {index} is {name} {'I' if isinstance(typ, IntType) else 'F'} from start to end"


class CodeGeneration:
    def __init__(self, symbols=None):
        self.emit = Emitter()
        self.frame = Frame()
        self.sym = symbols or []
        self.className = "Program"
        self.storage = {}

    def visitIntLiteral(self, ctx, o):
        raise NotImplementedError

    def visitFloatLiteral(self, ctx, o):
        raise NotImplementedError

    def visitBinExpr(self, ctx, o):
        raise NotImplementedError

    def visitId(self, ctx, o):
        raise NotImplementedError

    def visitVarDecl(self, ctx, o):
        raise NotImplementedError

    def eval_expr(self, node):
        if isinstance(node, IntLiteral):
            return self.visitIntLiteral(node, type("O", (), {"frame": self.frame})())
        if isinstance(node, FloatLiteral):
            return self.visitFloatLiteral(node, type("O", (), {"frame": self.frame})())
        if isinstance(node, BoolLiteral):
            return node.value, BoolType()
        if isinstance(node, Id):
            return self.visitId(node, type("O", (), {"frame": self.frame, "sym": self.sym, "isLeft": False})())
        if isinstance(node, BinExpr):
            return self.visitBinExpr(node, type("O", (), {"frame": self.frame})())
        raise TypeError(f"unsupported expression: {node!r}")

    def eval_bin(self, node):
        left, left_type = self.eval_expr(node.e1)
        right, right_type = self.eval_expr(node.e2)
        op = node.op
        if op in {"+.", "-.", "*.", "/."}:
            op = op[0]
            left_type = right_type = FloatType()
        result_type = FloatType() if op == "/" or isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
        if result_type is FloatType:
            left, right = float(left), float(right)
        if op == "+":
            value = left + right
        elif op == "-":
            value = left - right
        elif op == "*":
            value = left * right
        elif op == "/":
            value = left / right
        elif op == ">":
            value, result_type = left > right, BoolType()
        elif op == "<":
            value, result_type = left < right, BoolType()
        elif op == ">=":
            value, result_type = left >= right, BoolType()
        elif op == "<=":
            value, result_type = left <= right, BoolType()
        elif op == "!=":
            value, result_type = left != right, BoolType()
        elif op == "==":
            value, result_type = left == right, BoolType()
        else:
            raise ValueError(f"unsupported operator: {node.op}")
        if result_type is IntType and op == "/":
            value = int(value)
        return value, result_type

    def run_expression(self, node):
        return self.eval_expr(node)[0]

    def run_declarations(self, declarations):
        symbols = []
        for declaration, frame in declarations:
            symbols.append(self.visitVarDecl(declaration, frame))
        return "\n".join(self.emit.output)
