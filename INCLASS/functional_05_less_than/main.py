from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.reporting import TestCase, run_tests
from solution import lessThan_higher_order as student_higher_order
from solution import lessThan_lst_comp as student_lst_comp
from solution import lessThan_recursive as student_recursive
import answer

BASE = [
    TestCase("lessThan(50, [1, 55, 6, 2])", "[1, 6, 2]", (50, [1, 55, 6, 2])),
    TestCase("lessThan(1, [1, 0, -2])", "[0, -2]", (1, [1, 0, -2])),
    TestCase("lessThan(0, [])", "[]", (0, [])),
]


def main():
    methods = [("lessThan_lst_comp", student_lst_comp, answer.lessThan_lst_comp), ("lessThan_recursive", student_recursive, answer.lessThan_recursive), ("lessThan_higher_order", student_higher_order, answer.lessThan_higher_order)]
    success = True
    for name, student, reference in methods:
        tests = [TestCase(test.name.replace("lessThan", name), test.expected, test.args) for test in BASE]
        success = run_tests(name, tests, reference if "--answer" in sys.argv else student) and success
    return success


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
