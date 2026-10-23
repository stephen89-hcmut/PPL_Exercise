import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from common.runtime import Assign, BinExpr, CallStmt, Id, IntLiteral


def make_program():
    return [Assign(Id("x"), IntLiteral(15)), Assign(Id("x"), BinExpr("+", Id("x"), IntLiteral(5))), CallStmt("putInt", [Id("x")])]


TESTS = [TestCase("rhs then lhs assignment", "b'20'", make_program)]


if __name__ == "__main__":
    module_name = "answer" if "--answer" in sys.argv else "solution"
    module = __import__(module_name)
    tests = TESTS + ([TestCase("deliberate mismatch", "b'never'", make_program)] if "--demo-failure" in sys.argv else [])
    raise SystemExit(0 if run_tests("ABSTRACT 2 - visitAssign", tests, module.solve) else 1)
