import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from solution import solve as student_solve
import answer

TESTS = [TestCase('"x, y : int"', "[VarDecl(x, IntType), VarDecl(y, IntType)]", ("x,y:int",)), TestCase('"z : float"', "[VarDecl(z, FloatType)]", ("z:float",))]

if __name__ == "__main__":
    selected = answer.solve if "--answer" in sys.argv else student_solve
    raise SystemExit(0 if run_tests("AST 3 - VarDecl", TESTS, selected) else 1)
