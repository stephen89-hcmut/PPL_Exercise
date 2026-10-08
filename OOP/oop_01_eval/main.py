from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests

module_name = "answer" if "--answer" in sys.argv else "solution"
module = __import__(module_name)

x1 = module.IntLit(11)
x2 = module.FloatLit(2.0)
x3 = module.BinExp(module.IntLit(1), "+", module.IntLit(1))
x4 = module.UnExp("-", module.IntLit(1))
x5 = module.BinExp(module.UnExp("-", module.IntLit(1)), "+", module.BinExp(module.IntLit(4), "*", module.FloatLit(2.0)))
x6 = module.UnExp("-", module.BinExp(module.FloatLit(4.0), "*", module.IntLit(2)))

TESTS = [
    TestCase("x1.eval()", "11", lambda: x1.eval()),
    TestCase("x2.eval()", "2.0", lambda: x2.eval()),
    TestCase("x3.eval()", "2", lambda: x3.eval()),
    TestCase("x4.eval()", "-1", lambda: x4.eval()),
    TestCase("x5.eval()", "7.0", lambda: x5.eval()),
    TestCase("x6.eval()", "-8.0", lambda: x6.eval()),
]

raise SystemExit(0 if run_tests("OOP 1 - Expression eval", TESTS) else 1)
