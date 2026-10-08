from __future__ import annotations

from abc import ABC


class Exp(ABC):
    def eval(self):
        return None


class BinExp(Exp):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def eval(self):
        return None


class UnExp(Exp):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

    def eval(self):
        return None


class IntLit(Exp):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return None


class FloatLit(Exp):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return None
