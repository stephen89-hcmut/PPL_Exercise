import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from Type_Part1.common.ast_nodes import (
    BinOp, BoolType, FloatLit, FloatType, Id, IntLit, IntType, Program,
    UndeclaredIdentifier, VarDecl,
)
from Type_Part1.common.reporting import TestCase, run_tests
import solution


TESTS = [
    TestCase("declared integer", "int",
             Program([VarDecl("x", IntType())], BinOp("+", Id("x"), IntLit(1)))),
    TestCase("declared mixed arithmetic", "float",
             Program([VarDecl("x", IntType())], BinOp("+", Id("x"), FloatLit(3.4)))),
    TestCase("declared boolean", "bool",
             Program([VarDecl("ok", BoolType())], BinOp("&&", Id("ok"), Id("ok")))),
    TestCase("undeclared identifier", "UndeclaredIdentifier: Undeclared Identifier: y",
             Program([VarDecl("x", IntType())], BinOp("+", Id("x"), Id("y")))),
    TestCase("duplicate declaration", "RedeclaredDeclaration: x",
             Program([VarDecl("x", IntType()), VarDecl("x", FloatType())], IntLit(1))),
    TestCase("type mismatch in expression",
             'TypeMismatchInExpression: Type Mismatch In Expression: BinOp(">",IntLit(3),FloatLit(2.1))',
             Program([VarDecl("x", IntType())],
                     BinOp("*", BinOp("+", Id("x"), FloatLit(3.4)),
                           BinOp(">", IntLit(3), FloatLit(2.1)))),
             ),
]


def solve(checker, tree):
    try:
        return tree.accept(checker.StaticCheck()).__name__
    except Exception as error:
        return f"{type(error).__name__}: {error}"


def main():
    tests = TESTS
    if "--demo-failure" in sys.argv:
        tests += [TestCase("deliberate mismatch", "wrong",
                           Program([], IntLit(1)))]
    checker = solution
    if "--answer" in sys.argv:
        import answer
        checker = answer
    return run_tests("Type Part 1 Exercise 2 - Program types", tests,
                     lambda tree: solve(checker, tree))


raise SystemExit(0 if main() else 1)
