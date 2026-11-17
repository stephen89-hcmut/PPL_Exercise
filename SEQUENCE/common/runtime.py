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
        self.next_label = 0

    def getNewIndex(self):
        index = self.next_index
        self.next_index += 1
        return index

    def getNewLabel(self):
        label = self.next_label
        self.next_label += 1
        return label


class Emitter:
    def __init__(self):
        self.output = []

    def printout(self, text):
        self.output.append(str(text))

    def emitPUSHICONST(self, value, _):
        value = int(value)
        if value == -1:
            return "iconst_m1\n"
        if 0 <= value <= 5:
            return f"iconst_{value}\n"
        if -128 <= value <= 127:
            return f"bipush {value}\n"
        if -32768 <= value <= 32767:
            return f"sipush {value}\n"
        return f"ldc {value}\n"

    def emitPUSHFCONST(self, value, _):
        value = float(value)
        if value in (0.0, 1.0, 2.0):
            return f"fconst_{int(value)}\n"
        return f"ldc {value!r}\n"

    @staticmethod
    def _type_code(typ):
        return "f" if isinstance(typ, FloatType) else "i"

    @staticmethod
    def _descriptor(typ):
        return "F" if isinstance(typ, FloatType) else "I"

    def emitREADVAR(self, name, typ, index, _):
        return f"{self._type_code(typ)}load {index}\n"

    def emitWRITEVAR(self, name, typ, index, _):
        return f"{self._type_code(typ)}store {index}\n"

    def emitGETSTATIC(self, name, typ, _):
        return f"getstatic {name} {self._descriptor(typ)}\n"

    def emitPUTSTATIC(self, name, typ, _):
        return f"putstatic {name} {self._descriptor(typ)}\n"

    def emitADDOP(self, op, typ, _):
        suffix = "add" if op == "+" else "sub"
        return f"{'f' if isinstance(typ, FloatType) else 'i'}{suffix}\n"

    def emitMULOP(self, op, typ, _):
        suffix = {"*": "mul", "/": "div"}[op]
        return f"{'f' if isinstance(typ, FloatType) else 'i'}{suffix}\n"

    def emitI2F(self, _):
        return "i2f\n"

    def emitREOP(self, op, typ, frame):
        true_label = frame.getNewLabel()
        end_label = frame.getNewLabel()
        if isinstance(typ, FloatType):
            branch = {">": "ifgt", "<": "iflt", ">=": "ifge", "<=": "ifle",
                      "==": "ifeq", "!=": "ifne"}[op]
            compare = "fcmpl\n"
        else:
            branch = {">": "if_icmpgt", "<": "if_icmplt", ">=": "if_icmpge", "<=": "if_icmple",
                      "==": "if_icmpeq", "!=": "if_icmpne"}[op]
            compare = ""
        return (compare + f"{branch} Label{true_label}\niconst_0\ngoto Label{end_label}\n"
                f"Label{true_label}:\niconst_1\nLabel{end_label}:\n")

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
        self.float_division = False

    def visit(self, node, o):
        method = getattr(self, "visit" + type(node).__name__, None)
        if method is None:
            raise TypeError(f"no visitor for {type(node).__name__}")
        return method(node, o)

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
        # Invoke the visitor to check code generation, then execute the AST in
        # this lightweight local harness to display the same value as the exam.
        _, result_type = self.eval_expr(node)
        value = self._evaluate(node)
        if isinstance(result_type, FloatType):
            return float(value)
        if isinstance(result_type, (IntType, BoolType)):
            if isinstance(result_type, BoolType):
                return int(bool(value))
            return int(value)
        return value

    def _evaluate(self, node):
        if isinstance(node, IntLiteral):
            return node.value
        if isinstance(node, FloatLiteral):
            return node.value
        if isinstance(node, BoolLiteral):
            return node.value
        if isinstance(node, Id):
            symbol = next((symbol for symbol in self.sym if symbol.name == node.name), None)
            if symbol is None:
                raise NameError(f"undeclared identifier: {node.name}")
            return self.storage[node.name]
        if isinstance(node, BinExpr):
            left, right = self._evaluate(node.e1), self._evaluate(node.e2)
            op = node.op[0] if node.op in {"+.", "-.", "*.", "/."} else node.op
            if op == "+": return left + right
            if op == "-": return left - right
            if op == "*": return left * right
            if op == "/": return left / right if self.float_division or node.op.endswith(".") else int(left / right)
            if op == ">": return left > right
            if op == "<": return left < right
            if op == ">=": return left >= right
            if op == "<=": return left <= right
            if op == "==": return left == right
            if op == "!=": return left != right
        raise TypeError(f"unsupported expression: {node!r}")

    def run_declarations(self, declarations):
        symbols = []
        for declaration, frame in declarations:
            symbols.append(self.visitVarDecl(declaration, frame))
        return "\n".join(self.emit.output)
