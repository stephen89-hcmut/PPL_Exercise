from __future__ import annotations

from abc import ABC


class Exp(ABC):
    def eval(self):
        return None

    def printPrefix(self):
        return None

    def printPostfix(self):
        return None


class BinExp(Exp):
    def __init__(self, left, op, right):
        self.left, self.op, self.right = left, op, right

    def eval(self):
        return None

    def printPrefix(self):
        return None

    def printPostfix(self):
        return None


class UnExp(Exp):
    def __init__(self, op, operand):
        self.op, self.operand = op, operand

    def eval(self):
        return None

    def printPrefix(self):
        return None

    def printPostfix(self):
        return None


class IntLit(Exp):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return None

    def printPrefix(self):
        return None

    def printPostfix(self):
        return None


class FloatLit(Exp):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return None

    def printPrefix(self):
        return None

    def printPostfix(self):
        return None
