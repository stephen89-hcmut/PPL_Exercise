import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from Type_Part1.common.reporting import TestCase, run_tests
from Type_Part1.common.type2_nodes import (
    Assign, CallStmt, FloatLit, FuncDecl, Id, IntLit, Program,
    TypeCannotBeInferred, TypeMismatchInStatement, UndeclaredIdentifier,
    VarDecl,
)
import solution


TESTS = [
    TestCase("matching call", "None",
             Program([VarDecl("x"), FuncDecl("foo", [VarDecl("p")], [], [
                 Assign(Id("p"), IntLit(1))
             ])], [Assign(Id("x"), IntLit(3)), CallStmt("foo", [Id("x")])])),
    TestCase("argument mismatch",
             'TypeMismatchInStatement: CallStmt("foo",[Id("x")])',
             Program([VarDecl("x"), FuncDecl("foo", [VarDecl("p")], [], [
                 Assign(Id("p"), FloatLit(2.0))
             ])], [Assign(Id("x"), IntLit(3)), CallStmt("foo", [Id("x")])])),
    TestCase("undeclared function", "UndeclaredIdentifier: foo2",
             Program([VarDecl("x")], [CallStmt("foo2", [])])),
    TestCase("wrong arity", 'TypeMismatchInStatement: CallStmt("foo",[])',
             Program([FuncDecl("foo", [VarDecl("p")], [], [])], [CallStmt("foo", [])])),
    TestCase("unresolved parameter",
             'TypeCannotBeInferred: CallStmt("foo",[IntLit(3), Id("x")])',
             Program([VarDecl("x"), FuncDecl("foo", [VarDecl("a"), VarDecl("b")], [], [])],
                     [CallStmt("foo", [IntLit(3), Id("x")])])),
    TestCase("function redeclaration",
             'Redeclared: FuncDecl("x",[VarDecl("y")],[],[])',
             Program([VarDecl("x"), FuncDecl("x", [VarDecl("y")], [], [])], [])),
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
    return run_tests("Type Part 2 Exercise 2 - Function inference", tests,
                     lambda tree: solve(checker, tree))


raise SystemExit(0 if main() else 1)
