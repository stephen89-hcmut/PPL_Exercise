from __future__ import annotations

from dataclasses import dataclass


class Node:
    def accept(self, visitor, arg=None):
        return getattr(visitor, "visit" + type(self).__name__)(self, arg)


class Exp(Node):
    pass


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


class Type(Node):
    pass


class IntType(Type):
    def __repr__(self):
        return "IntType()"


class FloatType(Type):
    def __repr__(self):
        return "FloatType()"


class BoolType(Type):
    def __repr__(self):
        return "BoolType()"


@dataclass
class VarDecl(Node):
    name: str
    typ: Type

    def __repr__(self):
        return f'VarDecl("{self.name}",{self.typ!r})'


@dataclass
class Id(Exp):
    name: str

    def __repr__(self):
        return f'Id("{self.name}")'


@dataclass
class Program(Node):
    decl: list[VarDecl]
    exp: Exp

    def __repr__(self):
        return f"Program({self.decl!r},{self.exp!r})"


class TypeMismatchInExpression(Exception):
    def __init__(self, expression):
        self.expression = expression
        super().__init__(expression)

    def __str__(self):
        return f"Type Mismatch In Expression: {self.expression!r}"


class UndeclaredIdentifier(Exception):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

    def __str__(self):
        return f"Undeclared Identifier: {self.name}"


class RedeclaredDeclaration(Exception):
    pass
