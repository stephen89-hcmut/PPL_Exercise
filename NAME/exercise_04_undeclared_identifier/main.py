import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from NAME.common.ast_nodes import ConstDecl, FloatType, FuncDecl, Id, IntLit, IntType, Program, VarDecl
from NAME.common.reporting import TestCase, run_tests
import solution


TESTS = [
    TestCase("undeclared in function", "UndeclaredIdentifier: z",
             Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("m", FloatType()),
             VarDecl("b", IntType()), VarDecl("d", FloatType())],
             ([ConstDecl("c", IntLit(3)), FuncDecl("foo", [VarDecl("x", IntType())],
             ([VarDecl("y", IntType()), VarDecl("z", IntType())], [Id("y"), Id("x"),
             Id("foo"), Id("c"), Id("m"), Id("a")]))], [Id("foo"), Id("d"), Id("z")]))])),
    TestCase("undeclared d", "UndeclaredIdentifier: d",
             Program([VarDecl("a", IntType()), ConstDecl("b", IntLit(3)),
             FuncDecl("c", [], ([], [IntLit(1), Id("a"), Id("d"), Id("b")]))])),
    TestCase("undeclared q", "UndeclaredIdentifier: q",
             Program([VarDecl("b", IntType()), FuncDecl("a", [VarDecl("m", FloatType()),
             VarDecl("b", IntType()), VarDecl("n", FloatType())],
             ([ConstDecl("c", IntLit(3)), VarDecl("d", IntType())],
             [Id("a"), Id("b"), Id("c"), Id("d"), IntLit(3), Id("m"), Id("q"), Id("n")]))])),
    TestCase("global and local references valid", "None",
             Program([VarDecl("t", IntType()), FuncDecl("a", [VarDecl("m", FloatType()),
             VarDecl("b", IntType()), VarDecl("d", FloatType())],
             ([ConstDecl("c", IntLit(3)), FuncDecl("foo", [VarDecl("x", IntType())],
             ([VarDecl("y", IntType()), VarDecl("z", IntType())],
             [Id("y"), Id("x"), Id("foo"), Id("c"), Id("m"), Id("a"), Id("t")]))],
             [Id("foo"), Id("d")]))])),
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
    return run_tests("NAME Exercise 4 - UndeclaredIdentifier", TESTS, lambda tree: solve(checker, tree))


raise SystemExit(0 if main() else 1)
