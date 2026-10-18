import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from NAME.common.ast_nodes import ConstDecl, FloatType, IntLit, IntType, Program, VarDecl
from NAME.common.reporting import TestCase, run_tests

import solution


TESTS = [
    TestCase("distinct declarations", "['a', 'b', 'c']",
             Program([VarDecl("a", IntType()), ConstDecl("b", IntLit(3)), VarDecl("c", FloatType())])),
    TestCase("duplicate variable", "RedeclaredDeclaration: a",
             Program([VarDecl("a", IntType()), ConstDecl("b", IntLit(3)), VarDecl("a", FloatType())])),
    TestCase("duplicate constant", "RedeclaredDeclaration: b",
             Program([VarDecl("b", IntType()), ConstDecl("b", IntLit(3)), VarDecl("a", FloatType())])),
    TestCase("constant and variable duplicate", "RedeclaredDeclaration: c",
             Program([VarDecl("a", IntType()), ConstDecl("c", IntLit(3)), VarDecl("c", FloatType())])),
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
    tests = TESTS
    if "--demo-failure" in sys.argv:
        tests = tests + [TestCase("deliberate mismatch", "wrong", Program([]))]
    return run_tests("NAME Exercise 1 - RedeclaredDeclaration", tests, lambda tree: solve(checker, tree))


raise SystemExit(0 if main() else 1)
