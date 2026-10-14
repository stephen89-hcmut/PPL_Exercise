from __future__ import annotations

from dataclasses import dataclass


class Expr:
    pass


@dataclass
class Binary(Expr):
    op: str
    left: Expr
    right: Expr

    def __repr__(self) -> str:
        return f"Binary({self.op},{self.left!r},{self.right!r})"


@dataclass
class Id(Expr):
    value: str

    def __repr__(self) -> str:
        return f"Id({self.value})"


@dataclass
class IntLiteral(Expr):
    value: int

    def __repr__(self) -> str:
        return f"IntLiteral({self.value})"


@dataclass
class BooleanLiteral(Expr):
    value: bool

    def __repr__(self) -> str:
        return f"BooleanLiteral({self.value})"


class Type:
    pass


class CompoundType(Type):
    pass


@dataclass
class UnionType(CompoundType):
    firstType: Type
    secondType: Type

    def __repr__(self) -> str:
        return f"UnionType({self.firstType!r},{self.secondType!r})"


@dataclass
class ArrayType(CompoundType):
    indexType: Type
    eleType: Type

    def __repr__(self) -> str:
        return f"ArrayType({self.indexType!r},{self.eleType!r})"


class PrimType(Type):
    pass


class IntType(PrimType):
    def __repr__(self) -> str:
        return "IntType"


class FloatType(PrimType):
    def __repr__(self) -> str:
        return "FloatType"


@dataclass
class RangeType(PrimType):
    lowbound: int
    highbound: int

    def __repr__(self) -> str:
        return f"RangeType({self.lowbound},{self.highbound})"


@dataclass
class TypeId:
    name: str

    def __repr__(self) -> str:
        return self.name
