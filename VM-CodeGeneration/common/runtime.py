from __future__ import annotations

from dataclasses import dataclass


class IntType:
    def __repr__(self): return "IntType"


class FloatType:
    def __repr__(self): return "FloatType"


class BoolType:
    def __repr__(self): return "BoolType"


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
    """Small subset of the course Frame API used by these exercises."""

    def __init__(self):
        self.next_index = 0
        self.label = 0

    def getNewIndex(self):
        index = self.next_index
        self.next_index += 1
        return index

    def getNewLabel(self):
        label = self.label
        self.label += 1
        return label


class Emitter:
    """Emit Jasmin instructions; each returned fragment can be concatenated."""

    @staticmethod
    def _type_code(typ):
        return "f" if isinstance(typ, FloatType) else "i"

    def emitPUSHICONST(self, value, frame):
        value = int(value)
        if -1 <= value <= 5:
            return f"iconst_{value}\n" if value >= 0 else "iconst_m1\n"
        if -128 <= value <= 127: return f"bipush {value}\n"
        if -32768 <= value <= 32767: return f"sipush {value}\n"
        return f"ldc {value}\n"

    def emitPUSHFCONST(self, value, frame):
        value = float(value)
        if value in (0.0, 1.0, 2.0): return f"fconst_{int(value)}\n"
        return f"ldc {value!r}\n"

    def emitADDOP(self, op, typ, frame):
        return f"{self._type_code(typ)}{'add' if op == '+' else 'sub'}\n"

    def emitMULOP(self, op, typ, frame):
        suffix = {"*": "mul", "/": "div"}[op]
        return f"{self._type_code(typ)}{suffix}\n"

    def emitI2F(self, frame):
        return "i2f\n"

    def emitREADVAR(self, name, typ, index, frame):
        return f"{self._type_code(typ)}load {index}\n"

    def emitGETSTATIC(self, name, typ, frame):
        descriptor = "F" if isinstance(typ, FloatType) else "I"
        field = name if "/" in name else f"Program/{name}"
        return f"getstatic {field} {descriptor}\n"

    def emitREOP(self, op, typ, frame):
        label_true = frame.getNewLabel()
        label_end = frame.getNewLabel()
        if isinstance(typ, FloatType):
            cmp = "fcmpl\n"
            branch = {">": "ifgt", "<": "iflt", ">=": "ifge", "<=": "ifle", "==": "ifeq", "!=": "ifne"}[op]
        else:
            cmp = ""
            branch = {">": "if_icmpgt", "<": "if_icmplt", ">=": "if_icmpge", "<=": "if_icmple", "==": "if_icmpeq", "!=": "if_icmpne"}[op]
        return (cmp + f"{branch} Label{label_true}\niconst_0\ngoto Label{label_end}\n"
                f"Label{label_true}:\niconst_1\nLabel{label_end}:\n")


class CodeGeneration:
    def __init__(self, symbols=None):
        self.emit = Emitter()
        self.frame = Frame()
        self.sym = symbols or []
        self.className = "Program"
        self.storage = {}

    def visit(self, node, o):
        method = getattr(self, "visit" + type(node).__name__, None)
        if method is None:
            raise TypeError(f"no visitor for {type(node).__name__}")
        return method(node, o)

    def visitIntLiteral(self, ctx, o): raise NotImplementedError
    def visitFloatLiteral(self, ctx, o): raise NotImplementedError
    def visitBinExpr(self, ctx, o): raise NotImplementedError
    def visitId(self, ctx, o): raise NotImplementedError
    def visitVarDecl(self, ctx, o): raise NotImplementedError

    def generate_expression(self, node):
        frame = Frame()
        return self.visit(node, type("O", (), {"frame": frame, "sym": self.sym})())

    def run_expression(self, node):
        code, result_type = self.generate_expression(node)
        return self.execute(code, result_type)

    def execute(self, code, result_type):
        """Execute the emitted JVM subset and capture the print result as bytes."""
        instructions = [line.strip() for line in code.splitlines() if line.strip()]
        labels = {line[:-1]: i for i, line in enumerate(instructions) if line.endswith(":")}
        stack, locals_ = [], {}
        symbols = {s.name: s for s in self.sym}
        pc = 0
        while pc < len(instructions):
            line = instructions[pc]
            pc += 1
            if line.endswith(":"): continue
            parts = line.split()
            op = parts[0]
            if op.startswith("iconst_"):
                stack.append(-1 if op == "iconst_m1" else int(op[-1]))
            elif op.startswith("fconst_"): stack.append(float(op[-1]))
            elif op in ("bipush", "sipush", "ldc"): stack.append(float(parts[1]) if "." in parts[1] else int(parts[1]))
            elif op in ("iload", "fload"):
                index = int(parts[1])
                symbol = next((s for s in self.sym if isinstance(s.value, Index) and s.value.value == index), None)
                stack.append(self.storage[symbol.name] if symbol else locals_[index])
            elif op == "getstatic":
                name = parts[1].split("/")[-1]
                stack.append(self.storage[name])
            elif op == "i2f": stack.append(float(stack.pop()))
            elif op in ("iadd", "fadd", "isub", "fsub", "imul", "fmul", "idiv", "fdiv"):
                b, a = stack.pop(), stack.pop()
                if op.endswith("add"): value = a + b
                elif op.endswith("sub"): value = a - b
                elif op.endswith("mul"): value = a * b
                elif op == "idiv": value = int(a / b)
                else: value = a / b
                stack.append(value)
            elif op == "fcmpl":
                b, a = stack.pop(), stack.pop()
                stack.append((a > b) - (a < b))
            elif op.startswith("if_icmp"):
                b, a = stack.pop(), stack.pop()
                cond = {"if_icmpgt": a > b, "if_icmplt": a < b, "if_icmpge": a >= b,
                        "if_icmple": a <= b, "if_icmpeq": a == b, "if_icmpne": a != b}[op]
                if cond: pc = labels[parts[1]] + 1
            elif op in ("ifgt", "iflt", "ifge", "ifle", "ifeq", "ifne"):
                value = stack.pop()
                cond = {"ifgt": value > 0, "iflt": value < 0, "ifge": value >= 0,
                        "ifle": value <= 0, "ifeq": value == 0, "ifne": value != 0}[op]
                if cond: pc = labels[parts[1]] + 1
            elif op == "goto": pc = labels[parts[1]] + 1
            else: raise ValueError(f"unsupported emitted instruction: {line}")
        value = stack[-1]
        if isinstance(result_type, BoolType): rendered = "true" if value else "false"
        elif isinstance(result_type, FloatType): rendered = str(float(value))
        else: rendered = str(int(value))
        return rendered.encode("utf-8")

    def run_declarations(self, declarations):
        raise NotImplementedError("declaration generation is outside these five expression exercises")
