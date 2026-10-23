import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from common.runtime import BoolLiteral, CallStmt, If, IntLiteral


def true_case():
    return [If(BoolLiteral(True), CallStmt("putInt", [IntLiteral(10)]), CallStmt("putInt", [IntLiteral(20)]))]


def false_case():
    return [If(BoolLiteral(False), CallStmt("putInt", [IntLiteral(10)]), CallStmt("putInt", [IntLiteral(20)]))]


TESTS = [TestCase("if true", "b'10'", true_case), TestCase("if false with else", "b'20'", false_case)]


if __name__ == "__main__":
    module_name = "answer" if "--answer" in sys.argv else "solution"
    module = __import__(module_name)
    tests = TESTS + ([TestCase("deliberate mismatch", "b'never'", true_case)] if "--demo-failure" in sys.argv else [])
    raise SystemExit(0 if run_tests("ABSTRACT 3 - visitIf", tests, module.solve) else 1)
