import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from Type_Part1.common.ast_nodes import BinOp, BoolLit, FloatLit, IntLit, UnOp
from Type_Part1.common.reporting import TestCase, run_tests
import solution


TESTS = [
    TestCase("integer addition", "int", BinOp("+", IntLit(3), IntLit(2))),
    TestCase("mixed arithmetic", "float", BinOp("*", IntLit(3), FloatLit(3.4))),
    TestCase("division", "float", BinOp("/", IntLit(8), IntLit(2))),
    TestCase("boolean conjunction", "bool", BinOp("&&", BoolLit(True), BoolLit(False))),
    TestCase("same-type comparison", "bool", BinOp("==", IntLit(3), IntLit(3))),
    TestCase("bad arithmetic operand",
             'TypeMismatchInExpression: Type Mismatch In Expression: BinOp("+",IntLit(3),BoolLit(True))',
             BinOp("+", IntLit(3), BoolLit(True))),
    TestCase("innermost mismatch",
             'TypeMismatchInExpression: Type Mismatch In Expression: BinOp(">",IntLit(3),FloatLit(2.1))',
             BinOp("*", BinOp("+", IntLit(3), FloatLit(3.4)),
                   BinOp(">", IntLit(3), FloatLit(2.1)))),
    TestCase("bad unary operand",
             'TypeMismatchInExpression: Type Mismatch In Expression: UnOp("-",BoolLit(True))',
             UnOp("-", BoolLit(True))),
]


def solve(checker, tree):
    try:
        result = tree.accept(checker.StaticCheck())
        return result.__name__
    except Exception as error:
        return f"{type(error).__name__}: {error}"


def main():
    tests = TESTS
    if "--demo-failure" in sys.argv:
        tests += [TestCase("deliberate mismatch", "wrong", IntLit(1))]
    checker = solution
    if "--answer" in sys.argv:
        import answer
        checker = answer
    return run_tests("Type Part 1 Exercise 1 - Expression types", tests,
                     lambda tree: solve(checker, tree))


raise SystemExit(0 if main() else 1)
