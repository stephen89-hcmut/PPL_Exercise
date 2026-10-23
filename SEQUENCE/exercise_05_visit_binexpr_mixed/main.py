import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from common.runtime import BinExpr, FloatLiteral, IntLiteral

TESTS = [
    TestCase("5 > 3", "True", lambda: BinExpr(">", IntLiteral(5), IntLiteral(3))),
    TestCase("(5 - 3) * 3.0", "6.0", lambda: BinExpr("*", BinExpr("-", IntLiteral(5), IntLiteral(3)), FloatLiteral(3.0))),
    TestCase("-1.0 + 1.0", "0.0", lambda: BinExpr("+", FloatLiteral(-1.0), FloatLiteral(1.0))),
    TestCase("2 * (10.0 - 2)", "16.0", lambda: BinExpr("*", IntLiteral(2), BinExpr("-", FloatLiteral(10.0), IntLiteral(2)))),
    TestCase("(9 - 3) / 3", "2.0", lambda: BinExpr("/", BinExpr("-", IntLiteral(9), IntLiteral(3)), IntLiteral(3))),
    TestCase("2 >= (10.0 - 2)", "False", lambda: BinExpr(">=", IntLiteral(2), BinExpr("-", FloatLiteral(10.0), IntLiteral(2)))),
    TestCase("2 == (10.0 / 5)", "True", lambda: BinExpr("==", IntLiteral(2), BinExpr("/", FloatLiteral(10.0), IntLiteral(5)))),
    TestCase("2 != (4 - 2)", "False", lambda: BinExpr("!=", IntLiteral(2), BinExpr("-", IntLiteral(4), IntLiteral(2)))),
]

if __name__ == "__main__":
    module = __import__("answer" if "--answer" in sys.argv else "solution")
    tests = TESTS + ([TestCase("deliberate mismatch", "0", lambda: BinExpr(">", IntLiteral(5), IntLiteral(3)))] if "--demo-failure" in sys.argv else [])
    raise SystemExit(0 if run_tests("SEQUENCE 5 - mixed visitBinExpr", tests, module.solve) else 1)
