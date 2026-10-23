import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from common.runtime import Block, CallStmt, For, Id, IntLiteral


def make_program():
    return [For(Id("x"), IntLiteral(0), IntLiteral(10), IntLiteral(2), Block([
        CallStmt("putInt", [Id("x")]),
    ]))]


TESTS = [TestCase("for with initialization, bound and update", "b'0246810'", make_program)]


if __name__ == "__main__":
    module_name = "answer" if "--answer" in sys.argv else "solution"
    module = __import__(module_name)
    tests = TESTS + ([TestCase("deliberate mismatch", "b'never'", make_program)] if "--demo-failure" in sys.argv else [])
    raise SystemExit(0 if run_tests("ABSTRACT 5 - visitFor", tests, module.solve) else 1)
