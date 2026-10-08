from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Program:
    decl: List[VarDecl]


class Type:
    pass


class IntType(Type):
    def __repr__(self) -> str:
        return "IntType"


class FloatType(Type):
    def __repr__(self) -> str:
        return "FloatType"


@dataclass
class VarDecl:
    variable: Id
    varType: Type


@dataclass
class Id:
    name: str

    def __repr__(self) -> str:
        return self.name


for _cls in (Program, VarDecl, Id):
    _cls.__repr__ = lambda self: _repr_dataclass(self)


def _repr_dataclass(value: object) -> str:
    if isinstance(value, Program):
        return f"Program({value.decl!r})"
    if isinstance(value, VarDecl):
        return f"VarDecl({value.variable!r},{value.varType!r})"
    if isinstance(value, Id):
        return f"Id({value.name})"
    return repr(value)
