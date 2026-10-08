from __future__ import annotations

from abc import ABC


class Exp(ABC):
    def eval(self):
        raise NotImplementedError

    def printPrefix(self):
        raise NotImplementedError

    def printPostfix(self):
        raise NotImplementedError


class BinExp(Exp):
    def __init__(self, left, op, right):
        self.left, self.op, self.right = left, op, right

    def eval(self):
        left, right = self.left.eval(), self.right.eval()
        return {"+": left + right, "-": left - right, "*": left * right, "/": left / right}[self.op]

    def printPrefix(self):
        return f"{self.op} {self.left.printPrefix()} {self.right.printPrefix()}"

    def printPostfix(self):
        return f"{self.left.printPostfix()} {self.right.printPostfix()} {self.op}"


class UnExp(Exp):
    def __init__(self, op, operand):
        self.op, self.operand = op, operand

    def eval(self):
        value = self.operand.eval()
        return value if self.op == "+" else -value

    def printPrefix(self):
        return f"{self.op}. {self.operand.printPrefix()}"

    def printPostfix(self):
        return f"{self.operand.printPostfix()} {self.op}."


class IntLit(Exp):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return self.val

    def printPrefix(self):
        return str(self.val)

    def printPostfix(self):
        return str(self.val)


class FloatLit(Exp):
    def __init__(self, val):
        self.val = val

    def eval(self):
        return self.val

    def printPrefix(self):
        return str(self.val)

    def printPostfix(self):
        return str(self.val)
