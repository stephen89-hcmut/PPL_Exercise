from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.reporting import TestCase, run_tests
from solution import solve as student_solve


TESTS = [
    TestCase("real [-3..0][-10..-1]", "ArrayType(UnionType(RangeType(-3,0),RangeType(-10,-1)),FloatType)"),
    TestCase("integer[1..3]", "ArrayType(RangeType(1,3),IntType)"),
    TestCase("integer [1..100][-5..20][100..3000]", "ArrayType(UnionType(UnionType(RangeType(1,100),RangeType(-5,20)),RangeType(100,3000)),IntType)"),
]


if __name__ == "__main__":
    tests = TESTS + ([TestCase("integer[1..3]", "wrong")] if "--demo-failure" in sys.argv else [])
    solve = student_solve
    if "--answer" in sys.argv:
        from answer import solve
    raise SystemExit(0 if run_tests("Exercise 3 - Type AST (recursive dimensions)", tests, solve) else 1)
