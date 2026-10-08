import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from solution import solve as student_solve
import answer

TESTS = [TestCase('"a + 3"', "BinOp(+, Var(a), Num(3))", ("a+3",)), TestCase('"a * (b + 2)"', "BinOp(*, Var(a), BinOp(+, Var(b), Num(2)))", ("a*(b+2)",))]

if __name__ == "__main__":
    selected = answer.solve if "--answer" in sys.argv else student_solve
    raise SystemExit(0 if run_tests("AST 5 - Recursive expression", TESTS, selected) else 1)
