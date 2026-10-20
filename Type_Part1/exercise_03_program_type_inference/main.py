import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from Type_Part1.common.reporting import TestCase, run_tests
from Type_Part1.common.type2_nodes import (
    Assign, BinOp, BoolLit, FloatLit, Id, IntLit, Program, TypeCannotBeInferred,
    TypeMismatchInExpression, TypeMismatchInStatement, UndeclaredIdentifier,
    VarDecl, UnOp,
)
import solution


TESTS = [
    TestCase("infer integer", "None",
             Program([VarDecl("x")], [Assign(Id("x"), IntLit(3))])),
    TestCase("infer from arithmetic", "None",
             Program([VarDecl("x")], [
                 Assign(Id("x"), BinOp("+", IntLit(3), IntLit(4)))
             ])),
    TestCase("infer boolean", "None",
             Program([VarDecl("x"), VarDecl("y"), VarDecl("z")], [
                 Assign(Id("z"), BinOp("&&", Id("x"), Id("y")))
             ])),
    TestCase("unresolved identifiers",
             'TypeCannotBeInferred: Assign(Id("x"),Id("y"))',
             Program([VarDecl("x"), VarDecl("y")], [Assign(Id("x"), Id("y"))])),
    TestCase("bad expression",
             'TypeMismatchInExpression: BinOp("+",IntLit(3),BoolLit(True))',
             Program([VarDecl("x")], [
                 Assign(Id("x"), BinOp("+", IntLit(3), BoolLit(True)))
             ])),
    TestCase("bad assignment",
             'TypeMismatchInStatement: Assign(Id("x"),FloatLit(3.0))',
             Program([VarDecl("x")], [
                 Assign(Id("x"), IntLit(3)),
                 Assign(Id("x"), FloatLit(3.0)),
             ])),
    TestCase("undeclared identifier", "UndeclaredIdentifier: t",
             Program([VarDecl("x")], [Assign(Id("x"), Id("t"))])),
    TestCase("conversion operators", "None",
             Program([VarDecl("x"), VarDecl("y")], [
                 Assign(Id("x"), IntLit(3)),
                 Assign(Id("y"), UnOp("i2f", Id("x"))),
             ])),
]


def solve(checker, tree):
    try:
        return str(tree.accept(checker.StaticCheck()))
    except Exception as error:
        return f"{type(error).__name__}: {error}"


def main():
    tests = TESTS
    if "--demo-failure" in sys.argv:
        tests += [TestCase("deliberate mismatch", "wrong", Program([], []))]
    checker = solution
    if "--answer" in sys.argv:
        import answer
        checker = answer
    return run_tests("Type Part 1 Exercise 3 - Program inference", tests,
                     lambda tree: solve(checker, tree))


raise SystemExit(0 if main() else 1)
