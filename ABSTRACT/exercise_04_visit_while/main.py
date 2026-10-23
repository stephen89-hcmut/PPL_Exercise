import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from common.runtime import Assign, BinExpr, Block, CallStmt, Id, IntLiteral, While


def make_program():
    return [
        Assign(Id("x"), IntLiteral(0)),
        While(BinExpr("<", Id("x"), IntLiteral(10)), Block([
            CallStmt("putInt", [Id("x")]),
            Assign(Id("x"), BinExpr("+", Id("x"), IntLiteral(1))),
        ])),
    ]


TESTS = [TestCase("while with loop condition", "b'0123456789'", make_program)]


if __name__ == "__main__":
    module_name = "answer" if "--answer" in sys.argv else "solution"
    module = __import__(module_name)
    tests = TESTS + ([TestCase("deliberate mismatch", "b'never'", make_program)] if "--demo-failure" in sys.argv else [])
    raise SystemExit(0 if run_tests("ABSTRACT 4 - visitWhile", tests, module.solve) else 1)
