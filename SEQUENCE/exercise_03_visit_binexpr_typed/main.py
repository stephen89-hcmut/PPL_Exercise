import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from common.runtime import BinExpr, FloatLiteral, IntLiteral

TESTS = [
    TestCase("5 + 3", "8", lambda: BinExpr("+", IntLiteral(5), IntLiteral(3))),
    TestCase("(5 - 3) * 3", "6", lambda: BinExpr("*", BinExpr("-", IntLiteral(5), IntLiteral(3)), IntLiteral(3))),
    TestCase("-1.0 +. 1.0", "0.0", lambda: BinExpr("+.", FloatLiteral(-1.0), FloatLiteral(1.0))),
    TestCase("1.0 *. (10.0 -. 2.0)", "8.0", lambda: BinExpr("*.", FloatLiteral(1.0), BinExpr("-.", FloatLiteral(10.0), FloatLiteral(2.0)))),
    TestCase("(5 - 3) / 3", "0", lambda: BinExpr("/", BinExpr("-", IntLiteral(5), IntLiteral(3)), IntLiteral(3))),
]

if __name__ == "__main__":
    module = __import__("answer" if "--answer" in sys.argv else "solution")
    tests = TESTS + ([TestCase("deliberate mismatch", "0", lambda: BinExpr("+", IntLiteral(5), IntLiteral(3)))] if "--demo-failure" in sys.argv else [])
    raise SystemExit(0 if run_tests("SEQUENCE 3 - typed visitBinExpr", tests, module.solve) else 1)
