from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests

module = __import__("answer" if "--answer" in sys.argv else "solution")
x1 = module.IntLit(1)
x2 = module.FloatLit(2.0)
x3 = module.BinExp(module.IntLit(1), "+", module.IntLit(1))
x4 = module.UnExp("-", module.IntLit(1))
x5 = module.BinExp(module.UnExp("-", module.IntLit(1)), "+", module.BinExp(module.IntLit(4), "*", module.FloatLit(2.0)))

TESTS = [
    TestCase("x1.printPrefix()", "1", lambda: x1.printPrefix()),
    TestCase("x2.printPrefix()", "2.0", lambda: x2.printPrefix()),
    TestCase("x3.printPrefix()", "+ 1 1", lambda: x3.printPrefix()),
    TestCase("x4.printPrefix()", "-. 1", lambda: x4.printPrefix()),
    TestCase("x5.printPrefix()", "+ -. 1 * 4 2.0", lambda: x5.printPrefix()),
    TestCase("x5.printPostfix()", "1 -. 4 2.0 * +", lambda: x5.printPostfix()),
]

raise SystemExit(0 if run_tests("OOP 2 - Prefix and postfix", TESTS) else 1)
