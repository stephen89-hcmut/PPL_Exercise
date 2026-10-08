import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from solution import solve as student_solve
import answer

TESTS = [TestCase('"1 - 2 - 3"', "BinOp(-, BinOp(-, Num(1), Num(2)), Num(3))", ("1-2-3",)), TestCase('"a * b / c"', "BinOp(/, BinOp(*, Var(a), Var(b)), Var(c))", ("a*b/c",))]

if __name__ == "__main__":
    selected = answer.solve if "--answer" in sys.argv else student_solve
    raise SystemExit(0 if run_tests("AST 7 - Loop expression", TESTS, selected) else 1)
