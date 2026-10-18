import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from NAME.common.ast_nodes import ConstDecl, FloatType, FuncDecl, IntLit, IntType, Program, VarDecl
from NAME.common.reporting import TestCase, run_tests
import solution


TESTS = [
    TestCase("function repeats global variable", "RedeclaredFunction: a",
             Program([VarDecl("a", IntType()), ConstDecl("b", IntLit(3)), FuncDecl("a", [], [])])),
    TestCase("body repeats constant", "RedeclaredVariable: c",
             Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("a", FloatType())],
             [ConstDecl("c", IntLit(3)), VarDecl("b", IntType()), VarDecl("c", IntType())])])),
    TestCase("parameter repeats parameter", "RedeclaredVariable: m",
             Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("m", FloatType()),
             VarDecl("b", IntType()), VarDecl("m", FloatType())], [])])),
    TestCase("body repeats function", "RedeclaredFunction: d",
             Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("m", FloatType()),
             VarDecl("b", IntType()), VarDecl("d", FloatType())],
             [ConstDecl("c", IntLit(3)), FuncDecl("d", [], [])])])),
    TestCase("nested function parameter repeats local", "RedeclaredVariable: x",
             Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("m", FloatType()),
             VarDecl("b", IntType()), VarDecl("d", FloatType())],
             [ConstDecl("c", IntLit(3)), FuncDecl("foo", [VarDecl("x", IntType())],
             [VarDecl("x", IntType())])])])),
]


def solve(checker, tree):
    try:
        return checker.StaticCheck().visitProgram(tree, None)
    except Exception as error:
        return f"{type(error).__name__}: {error}"


def main():
    checker = solution
    if "--answer" in sys.argv:
        import answer
        checker = answer
    return run_tests("NAME Exercise 3 - Nested scopes", TESTS, lambda tree: solve(checker, tree))


raise SystemExit(0 if main() else 1)
