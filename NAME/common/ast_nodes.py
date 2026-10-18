from __future__ import annotations

from dataclasses import dataclass


class Node:
    def accept(self, visitor, arg=None):
        method = getattr(visitor, "visit" + type(self).__name__)
        return method(self, arg)


class Decl(Node):
    pass


class Type(Node):
    pass


class IntType(Type):
    def __repr__(self):
        return "IntType()"


class FloatType(Type):
    def __repr__(self):
        return "FloatType()"


class Lit(Node):
    pass


@dataclass
class IntLit(Lit):
    val: int

    def __repr__(self):
        return f"IntLit({self.val})"


@dataclass
class Id(Node):
    name: str

    def __repr__(self):
        return f'Id("{self.name}")'


@dataclass
class VarDecl(Decl):
    name: str
    typ: Type

    def __repr__(self):
        return f'VarDecl("{self.name}",{self.typ!r})'


@dataclass
class ConstDecl(Decl):
    name: str
    val: Lit

    def __repr__(self):
        return f'ConstDecl("{self.name}",{self.val!r})'


@dataclass
class FuncDecl(Decl):
    name: str
    param: list[VarDecl]
    body: object

    def __repr__(self):
        return f'FuncDecl("{self.name}",{self.param!r},{self.body!r})'


@dataclass
class Program(Node):
    decl: list[Decl]

    def __repr__(self):
        return f"Program({self.decl!r})"


class RedeclaredDeclaration(Exception):
    pass


class RedeclaredVariable(Exception):
    pass


class RedeclaredConstant(Exception):
    pass


class RedeclaredFunction(Exception):
    pass


class UndeclaredIdentifier(Exception):
    pass
