from __future__ import annotations

from dataclasses import dataclass


class Node:
    def accept(self, visitor, arg=None):
        return getattr(visitor, "visit" + type(self).__name__)(self, arg)


class Stmt(Node):
    pass


class Exp(Node):
    pass


class Decl(Node):
    pass


@dataclass
class Program(Node):
    decl: list[Decl]
    stmts: list[Stmt]

    def __repr__(self):
        return f"Program({self.decl!r},{self.stmts!r})"


@dataclass
class VarDecl(Decl):
    name: str

    def __repr__(self):
        return f'VarDecl("{self.name}")'


@dataclass
class Block(Stmt):
    decl: list[VarDecl]
    stmts: list[Stmt]

    def __repr__(self):
        return f"Block({self.decl!r},{self.stmts!r})"


@dataclass
class Assign(Stmt):
    lhs: "Id"
    rhs: Exp

    def __repr__(self):
        return f"Assign({self.lhs!r},{self.rhs!r})"


@dataclass
class BinOp(Exp):
    op: str
    e1: Exp
    e2: Exp

    def __repr__(self):
        return f'BinOp("{self.op}",{self.e1!r},{self.e2!r})'


@dataclass
class UnOp(Exp):
    op: str
    e: Exp

    def __repr__(self):
        return f'UnOp("{self.op}",{self.e!r})'


@dataclass
class IntLit(Exp):
    val: int

    def __repr__(self):
        return f"IntLit({self.val})"


@dataclass
class FloatLit(Exp):
    val: float

    def __repr__(self):
        return f"FloatLit({self.val})"


@dataclass
class BoolLit(Exp):
    val: bool

    def __repr__(self):
        return f"BoolLit({self.val})"


@dataclass
class Id(Exp):
    name: str

    def __repr__(self):
        return f'Id("{self.name}")'


@dataclass
class FuncDecl(Decl):
    name: str
    param: list[VarDecl]
    local: list[Decl]
    stmts: list[Stmt]

    def __repr__(self):
        return f'FuncDecl("{self.name}",{self.param!r},{self.local!r},{self.stmts!r})'


@dataclass
class CallStmt(Stmt):
    name: str
    args: list[Exp]

    def __repr__(self):
        return f'CallStmt("{self.name}",{self.args!r})'


class IntType:
    def __repr__(self):
        return "int"


class FloatType:
    def __repr__(self):
        return "float"


class BoolType:
    def __repr__(self):
        return "bool"


class Redeclared(Exception):
    pass


class UndeclaredIdentifier(Exception):
    pass


class TypeMismatchInExpression(Exception):
    pass


class TypeMismatchInStatement(Exception):
    pass


class TypeCannotBeInferred(Exception):
    pass
