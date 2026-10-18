import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from NAME.common.ast_nodes import ConstDecl, FloatType, IntLit, IntType, Program, VarDecl
from NAME.common.reporting import TestCase, run_tests
import solution


TESTS = [
    TestCase("variable repeated", "RedeclaredVariable: a",
             Program([VarDecl("a", IntType()), ConstDecl("b", IntLit(3)), VarDecl("a", FloatType())])),
    TestCase("constant repeated", "RedeclaredConstant: b",
             Program([VarDecl("b", IntType()), ConstDecl("b", IntLit(3)), VarDecl("a", FloatType())])),
    TestCase("constant then variable", "RedeclaredVariable: c",
             Program([VarDecl("a", IntType()), ConstDecl("c", IntLit(3)), VarDecl("c", FloatType())])),
    TestCase("no duplicate", "None",
             Program([VarDecl("a", IntType()), ConstDecl("b", IntLit(3)), VarDecl("c", FloatType())])),
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
    return run_tests("NAME Exercise 2 - Declaration kinds", TESTS, lambda tree: solve(checker, tree))


raise SystemExit(0 if main() else 1)
