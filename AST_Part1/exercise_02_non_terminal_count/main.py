from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.reporting import TestCase, run_tests
from solution import solve as student_solve


TESTS = [
    TestCase("int a;", "6"),
    TestCase("int a,b;", "7"),
    TestCase("int a;float b;", "10"),
    TestCase("int a,b;float c;", "11"),
    TestCase("int a,b;float c,d,e;", "13"),
]


if __name__ == "__main__":
    tests = TESTS + ([TestCase("int a;", "0")] if "--demo-failure" in sys.argv else [])
    if "--answer" in sys.argv:
        from answer import solve
    else:
        solve = student_solve
    raise SystemExit(0 if run_tests("Exercise 2 - Non-terminal Count", tests, solve) else 1)
