from __future__ import annotations

from dataclasses import dataclass, field


class IntType:
    def __repr__(self) -> str:
        return "IntType"


class BoolType:
    def __repr__(self) -> str:
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
class Access:
    frame: "Frame"
    sym: list[Symbol]
    isLeft: bool


@dataclass
class Ref:
    storage: dict[str, int | bool]
    name: str

    def get(self):
        return self.storage[self.name]

    def set(self, value) -> None:
        self.storage[self.name] = value


class Emitter:
    def __init__(self) -> None:
        self.output: list[str] = []

    def printout(self, value) -> None:
        if callable(value):
            value()
        elif value is not None:
            self.output.append(str(value))

    def emitREADVAR(self, name, *_):
        return f"READVAR({name})"

    def emitWRITEVAR(self, name, *_):
        return f"WRITEVAR({name})"

    def emitGETSTATIC(self, name, *_):
        return f"GETSTATIC({name})"

    def emitPUTSTATIC(self, name, *_):
        return f"PUTSTATIC({name})"

    def emitIFFALSE(self, label, *_):
        return f"IFFALSE({label})"

    def emitIFTRUE(self, label, *_):
        return f"IFTRUE({label})"

    def emitGOTO(self, label, *_):
        return f"GOTO({label})"

    def emitLABEL(self, label, *_):
        return f"LABEL({label})"

    def emitREOP(self, op, *_):
        return op

    def emitADDOP(self, op, *_):
        return op


class Frame:
    def __init__(self) -> None:
        self._label = 0
        self._loops: list[tuple[str, str]] = []

    def getNewLabel(self) -> str:
        self._label += 1
        return f"L{self._label}"

    def enterLoop(self) -> None:
        self._loops.append((self.getNewLabel(), self.getNewLabel()))

    def exitLoop(self) -> None:
        self._loops.pop()

    def getBreakLabel(self) -> str:
        return self._loops[-1][0]

    def getContinueLabel(self) -> str:
        return self._loops[-1][1]


@dataclass
class Id:
    name: str


@dataclass
class IntLiteral:
    value: int


@dataclass
class BoolLiteral:
    value: bool


@dataclass
class BinExpr:
    op: str
    left: object
    right: object


@dataclass
class Assign:
    lhs: Id
    rhs: object


@dataclass
class CallStmt:
    name: str
    args: list[object] = field(default_factory=list)


@dataclass
class Block:
    stmts: list[object]


@dataclass
class If:
    expr: object
    tstmt: object
    estmt: object | None


@dataclass
class While:
    expr: object
    stmt: object


@dataclass
class For:
    idx: Id
    ini: object
    end: object
    upd: object
    stmt: object


@dataclass
class Break:
    pass


@dataclass
class Continue:
    pass


class _Signal(Exception):
    pass


class BreakSignal(_Signal):
    pass


class ContinueSignal(_Signal):
    pass


class CodeGeneration:
    """Small executable model of the visitor protocol used in the PDF."""

    def __init__(self, symbols: list[Symbol] | None = None) -> None:
        self.emit = Emitter()
        self.frame = Frame()
        self.sym = symbols or []
        self.storage: dict[str, int | bool] = {}

    def visitId(self, ctx, o):  # pragma: no cover - exercise hook
        raise NotImplementedError

    def visitAssign(self, ctx, o):
        lhs = self.visitId(ctx.lhs, Access(self.frame, self.sym, True))[0]
        lhs.set(self.expression(ctx.rhs))

    def visitIf(self, ctx, o):  # pragma: no cover - exercise hook
        raise NotImplementedError

    def visitWhile(self, ctx, o):  # pragma: no cover - exercise hook
        raise NotImplementedError

    def visitFor(self, ctx, o):  # pragma: no cover - exercise hook
        raise NotImplementedError

    def resolve(self, name: str) -> Symbol:
        for symbol in self.sym:
            if symbol.name == name:
                return symbol
        symbol = Symbol(name, IntType(), CName("Program"))
        self.sym.append(symbol)
        return symbol

    def expression(self, node, left=False):
        if isinstance(node, Id):
            return self.visitId(node, Access(self.frame, self.sym, left))[0]
        if isinstance(node, IntLiteral):
            return node.value
        if isinstance(node, BoolLiteral):
            return node.value
        if isinstance(node, BinExpr):
            left_value = self.expression(node.left)
            right_value = self.expression(node.right)
            return {
                "+": lambda: left_value + right_value,
                "-": lambda: left_value - right_value,
                "*": lambda: left_value * right_value,
                "<": lambda: left_value < right_value,
                ">": lambda: left_value > right_value,
                "<=": lambda: left_value <= right_value,
                ">=": lambda: left_value >= right_value,
                "==": lambda: left_value == right_value,
            }[node.op]()
        raise TypeError(f"unsupported expression: {node!r}")

    def statement(self, node) -> None:
        if isinstance(node, Assign):
            self.visitAssign(node, self)
        elif isinstance(node, CallStmt):
            if node.name == "putInt":
                self.emit.printout(self.expression(node.args[0]))
        elif isinstance(node, Block):
            for statement in node.stmts:
                self.statement(statement)
        elif isinstance(node, If):
            self.visitIf(node, self)
        elif isinstance(node, While):
            self.visitWhile(node, self)
        elif isinstance(node, For):
            self.visitFor(node, self)
        elif isinstance(node, Break):
            raise BreakSignal
        elif isinstance(node, Continue):
            raise ContinueSignal
        else:
            raise TypeError(f"unsupported statement: {node!r}")

    def run(self, statements: list[object]) -> bytes:
        for statement in statements:
            self.statement(statement)
        return "".join(self.emit.output).encode()
