from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.reporting import TestCase, run_tests
from solution import solve as student_solve


TESTS = [
    TestCase("a := b := 4", "Binary(:=,Id(a),Binary(:=,Id(b),IntLiteral(4)))"),
    TestCase("a += b -= a and (b > 3)", "Binary(+=,Id(a),Binary(-=,Id(b),Binary(and,Id(a),Binary(>,Id(b),IntLiteral(3)))))"),
    TestCase("a or b and True", "Binary(and,Binary(or,Id(a),Id(b)),BooleanLiteral(True))"),
]


if __name__ == "__main__":
    tests = TESTS + ([TestCase("a := 1", "wrong")] if "--demo-failure" in sys.argv else [])
    solve = student_solve
    if "--answer" in sys.argv:
        from answer import solve
    raise SystemExit(0 if run_tests("Exercise 1 - Expression AST (recursive grammar)", tests, solve) else 1)
