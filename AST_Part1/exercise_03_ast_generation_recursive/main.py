from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.reporting import TestCase, run_tests
from solution import solve as student_solve


TESTS = [
    TestCase("int a;", "Program([VarDecl(Id(a),IntType)])"),
    TestCase("int a,b;", "Program([VarDecl(Id(a),IntType), VarDecl(Id(b),IntType)])"),
    TestCase("int a;float b;", "Program([VarDecl(Id(a),IntType), VarDecl(Id(b),FloatType)])"),
    TestCase("int a,b;float c;", "Program([VarDecl(Id(a),IntType), VarDecl(Id(b),IntType), VarDecl(Id(c),FloatType)])"),
    TestCase("int a,b;float c,d,e;", "Program([VarDecl(Id(a),IntType), VarDecl(Id(b),IntType), VarDecl(Id(c),FloatType), VarDecl(Id(d),FloatType), VarDecl(Id(e),FloatType)])"),
]


if __name__ == "__main__":
    tests = TESTS + ([TestCase("int a;", "wrong")] if "--demo-failure" in sys.argv else [])
    if "--answer" in sys.argv:
        from answer import solve
    else:
        solve = student_solve
    raise SystemExit(0 if run_tests("Exercise 3 - AST Generation (recursive grammar)", tests, solve) else 1)
