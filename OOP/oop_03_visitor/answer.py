from __future__ import annotations

from abc import ABC


class Exp(ABC):
    def accept(self, visitor):
        raise NotImplementedError


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
        left, right = ctx.left.accept(self), ctx.right.accept(self)
        return {"+": left + right, "-": left - right, "*": left * right, "/": left / right}[ctx.op]

    def visitUnExp(self, ctx):
        value = ctx.operand.accept(self)
        return value if ctx.op == "+" else -value

    def visitIntLit(self, ctx):
        return ctx.val

    def visitFloatLit(self, ctx):
        return ctx.val


class PrintPrefix:
    def visitBinExp(self, ctx):
        return f"{ctx.op} {ctx.left.accept(self)} {ctx.right.accept(self)}"

    def visitUnExp(self, ctx):
        return f"{ctx.op}. {ctx.operand.accept(self)}"

    def visitIntLit(self, ctx):
        return str(ctx.val)

    def visitFloatLit(self, ctx):
        return str(ctx.val)


class PrintPostfix:
    def visitBinExp(self, ctx):
        return f"{ctx.left.accept(self)} {ctx.right.accept(self)} {ctx.op}"

    def visitUnExp(self, ctx):
        return f"{ctx.operand.accept(self)} {ctx.op}."

    def visitIntLit(self, ctx):
        return str(ctx.val)

    def visitFloatLit(self, ctx):
        return str(ctx.val)
