from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.reporting import TestCase, run_tests
from solution import double_higher_order as student_higher_order
from solution import double_lst_comp as student_lst_comp
from solution import double_recursive as student_recursive

TESTS = [
    TestCase("double_lst_comp([5, 7, 12, -4])", "[10, 14, 24, -8]", ([5, 7, 12, -4],)),
    TestCase("double_lst_comp([])", "[]", ([],)),
    TestCase("double_lst_comp([0, -3])", "[0, -6]", ([0, -3],)),
]


def run_method(name, student, answer):
    tests = [TestCase(test.name.replace("double_lst_comp", name), test.expected, test.args) for test in TESTS]
    return run_tests(f"{name}", tests, answer if "--answer" in sys.argv else student)


if __name__ == "__main__":
    selected = [
        ("double_lst_comp", student_lst_comp, __import__("answer").double_lst_comp),
        ("double_recursive", student_recursive, __import__("answer").double_recursive),
        ("double_higher_order", student_higher_order, __import__("answer").double_higher_order),
    ]
    success = all(run_method(name, student, answer) for name, student, answer in selected)
    raise SystemExit(0 if success else 1)
