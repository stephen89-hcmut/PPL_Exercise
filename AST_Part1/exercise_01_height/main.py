from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.reporting import TestCase, run_tests
from solution import solve as student_solve


TESTS = [
    TestCase("int a;", "5"),
    TestCase("int a,b;", "6"),
    TestCase("int a;float b;", "6"),
    TestCase("int a,b;float c;", "6"),
    TestCase("int a,b;float c,d,e;", "8"),
    TestCase("int", "2", "mptype"),
    TestCase("a", "2", "ids"),
    TestCase("a,b,c", "4", "ids"),
    TestCase("int a;", "3", "vardecl"),
    TestCase("int a,b,c;", "5", "vardecl"),
    TestCase("int a;float b;", "5", "vardecls"),
]


if __name__ == "__main__":
    tests = TESTS + ([TestCase("int a;", "0")] if "--demo-failure" in sys.argv else [])
    if "--answer" in sys.argv:
        from answer import solve
    else:
        solve = student_solve
    raise SystemExit(0 if run_tests("Exercise 1 - Parse Tree Height", tests, solve) else 1)
