from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.reporting import TestCase, run_tests
from solution import compose_higher_order as student_higher_order
from solution import compose_recursive as student_recursive
import answer


def double(value):
    return value * 2


def increase(value):
    return value + 1


def square(value):
    return value * value


def run_composed(factory, functions, value):
    return factory(*functions)(value)


BASE = [
    TestCase("compose(double, increase)(3)", "7", (double, increase, 3)),
    TestCase("compose(square, increase, double)(2)", "10", (square, increase, double, 2)),
]


def solve(factory, *args):
    *functions, value = args
    return run_composed(factory, functions, value)


def main():
    success = True
    for name, student, reference in [("compose_recursive", student_recursive, answer.compose_recursive), ("compose_higher_order", student_higher_order, answer.compose_higher_order)]:
        tests = [TestCase(test.name.replace("compose", name), test.expected, test.args) for test in BASE]
        selected = reference if "--answer" in sys.argv else student
        success = run_tests(name, tests, lambda *args: solve(selected, *args)) and success
    return success


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
