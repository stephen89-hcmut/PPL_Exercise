from __future__ import annotations

from abc import ABC


class Exp(ABC):
    def eval(self):
        raise NotImplementedError


class BinExp(Exp):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()
        return {"+": lambda: left + right, "-": lambda: left - right, "*": lambda: left * right, "/": lambda: left / right}[self.op]()


class UnExp(Exp):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

    def eval(self):
        value = self.operand.eval()
        return value if self.op == "+" else -value


class IntLit(Exp):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return self.val


class FloatLit(Exp):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return self.val
