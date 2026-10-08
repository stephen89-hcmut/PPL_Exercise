from __future__ import annotations

from dataclasses import dataclass


class Expr:
    pass


@dataclass
class Num(Expr):
    val: int

    def __repr__(self) -> str:
        return f"Num({self.val})"


@dataclass
class Var(Expr):
    name: str

    def __repr__(self) -> str:
        return f"Var({self.name})"


@dataclass
class BinOp(Expr):
    op: str
    left: Expr
    right: Expr

    def __repr__(self) -> str:
        return f"BinOp({self.op}, {self.left!r}, {self.right!r})"


@dataclass
class UnOp(Expr):
    op: str
    arg: Expr

    def __repr__(self) -> str:
        return f"UnOp({self.op}, {self.arg!r})"


class Decl:
    pass


class Type:
    pass


class IntType(Type):
    def __repr__(self) -> str:
        return "IntType"


class FloatType(Type):
    def __repr__(self) -> str:
        return "FloatType"


@dataclass
class VarDecl(Decl):
    name: str
    typ: Type

    def __repr__(self) -> str:
        return f"VarDecl({self.name}, {self.typ!r})"


@dataclass
class Program(Decl):
    decl: list[VarDecl]

    def __repr__(self) -> str:
        return f"Program({self.decl!r})"
