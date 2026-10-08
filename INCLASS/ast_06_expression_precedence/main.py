import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from solution import solve as student_solve
import answer

TESTS = [TestCase('"a + 3 * b - 2"', "BinOp(-, BinOp(+, Var(a), BinOp(*, Num(3), Var(b))), Num(2))", ("a+3*b-2",))]

if __name__ == "__main__":
    selected = answer.solve if "--answer" in sys.argv else student_solve
    raise SystemExit(0 if run_tests("AST 6 - Expression precedence", TESTS, selected) else 1)
