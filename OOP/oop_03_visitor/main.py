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
    TestCase("x1.accept(Eval())", "1", lambda: x1.accept(module.Eval())),
    TestCase("x1 prefix/postfix", "1 | 1", lambda: f"{x1.accept(module.PrintPrefix())} | {x1.accept(module.PrintPostfix())}"),
    TestCase("x2.accept(Eval())", "2.0", lambda: x2.accept(module.Eval())),
    TestCase("x2 prefix/postfix", "2.0 | 2.0", lambda: f"{x2.accept(module.PrintPrefix())} | {x2.accept(module.PrintPostfix())}"),
    TestCase("x3 visitors", "2 | + 1 1 | 1 1 +", lambda: f"{x3.accept(module.Eval())} | {x3.accept(module.PrintPrefix())} | {x3.accept(module.PrintPostfix())}"),
    TestCase("x4 visitors", "-1 | -. 1 | 1 -.", lambda: f"{x4.accept(module.Eval())} | {x4.accept(module.PrintPrefix())} | {x4.accept(module.PrintPostfix())}"),
    TestCase("x5 visitors", "7.0 | + -. 1 * 4 2.0 | 1 -. 4 2.0 * +", lambda: f"{x5.accept(module.Eval())} | {x5.accept(module.PrintPrefix())} | {x5.accept(module.PrintPostfix())}"),
]

raise SystemExit(0 if run_tests("OOP 3 - Visitor pattern", TESTS) else 1)
