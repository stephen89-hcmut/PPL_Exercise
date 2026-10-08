from __future__ import annotations

from abc import ABC


class Exp(ABC):
    def accept(self, visitor):
        return None


class BinExp(Exp):
    def __init__(self, left, op, right):
        self.left, self.op, self.right = left, op, right

    def accept(self, visitor):
        return visitor.visitBinExp(self)


class UnExp(Exp):
    def __init__(self, op, operand):
        self.op, self.operand = op, operand

    def accept(self, visitor):
        return visitor.visitUnExp(self)


class IntLit(Exp):
    def __init__(self, val):
        self.val = val

    def accept(self, visitor):
        return visitor.visitIntLit(self)


class FloatLit(Exp):
    def __init__(self, val):
        self.val = val

    def accept(self, visitor):
        return visitor.visitFloatLit(self)


class Eval:
    def visitBinExp(self, ctx):
        return None

    def visitUnExp(self, ctx):
        return None

    def visitIntLit(self, ctx):
        return None

    def visitFloatLit(self, ctx):
        return None


class PrintPrefix:
    def visitBinExp(self, ctx):
        return None

    def visitUnExp(self, ctx):
        return None

    def visitIntLit(self, ctx):
        return None

    def visitFloatLit(self, ctx):
        return None


class PrintPostfix:
    def visitBinExp(self, ctx):
        return None

    def visitUnExp(self, ctx):
        return None

    def visitIntLit(self, ctx):
        return None

    def visitFloatLit(self, ctx):
        return None
