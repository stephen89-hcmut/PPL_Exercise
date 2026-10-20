import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from Type_Part1.common.reporting import TestCase, run_tests
from Type_Part1.common.type2_nodes import (
    Assign, Block, BoolLit, FloatLit, Id, IntLit, Program, Redeclared,
    TypeCannotBeInferred, TypeMismatchInExpression, TypeMismatchInStatement,
    UndeclaredIdentifier, VarDecl, BinOp, UnOp,
)
import solution


TESTS = [
    TestCase("infer integer assignment", "None",
             Program([VarDecl("x")], [Assign(Id("x"), IntLit(3))])),
    TestCase("infer through block", "None",
             Program([VarDecl("x")], [
                 Assign(Id("x"), IntLit(3)),
                 Block([VarDecl("y")], [Assign(Id("x"), Id("y")),
                                        Assign(Id("y"), IntLit(4))]),
             ])),
    TestCase("block redeclaration", 'Redeclared: VarDecl("y")',
             Program([VarDecl("x")], [
                 Block([VarDecl("y"), VarDecl("x"), VarDecl("y")], [])
             ])),
    TestCase("unresolved assignment", "TypeCannotBeInferred: Assign(Id(\"x\"),Id(\"y\"))",
             Program([VarDecl("x"), VarDecl("y")], [Assign(Id("x"), Id("y"))])),
    TestCase("undeclared identifier", "UndeclaredIdentifier: z",
             Program([VarDecl("x")], [Assign(Id("x"), Id("z"))])),
    TestCase("expression mismatch",
             'TypeMismatchInExpression: BinOp("-",Id("t"),Id("x"))',
             Program([VarDecl("x"), VarDecl("t")], [
                 Assign(Id("x"), IntLit(3)),
                 Assign(Id("t"), FloatLit(3.0)),
                 Assign(Id("t"), BinOp("-", Id("t"), Id("x"))),
             ])),
    TestCase("statement mismatch",
             'TypeMismatchInStatement: Assign(Id("y"),BoolLit(True))',
             Program([VarDecl("x")], [
                 Assign(Id("x"), IntLit(3)),
                 Block([VarDecl("y")], [Assign(Id("y"), IntLit(1)),
                                        Assign(Id("y"), BoolLit(True))]),
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
    return run_tests("Type Part 2 Exercise 1 - Block inference", tests,
                     lambda tree: solve(checker, tree))


raise SystemExit(0 if main() else 1)
