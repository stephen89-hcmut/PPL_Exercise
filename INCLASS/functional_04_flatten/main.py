from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common.reporting import TestCase, run_tests
from solution import flatten_higher_order as student_higher_order
from solution import flatten_lst_comp as student_lst_comp
from solution import flatten_recursive as student_recursive
import answer

BASE = [
    TestCase("flatten([[1, 2, 3], ['a', 'b', 'c']])", "[1, 2, 3, 'a', 'b', 'c']", ([[1, 2, 3], ['a', 'b', 'c']],)),
    TestCase("flatten([])", "[]", ([],)),
    TestCase("flatten([[1.1], [2.1, 3.1]])", "[1.1, 2.1, 3.1]", ([[1.1], [2.1, 3.1]],)),
]


def main():
    methods = [("flatten_lst_comp", student_lst_comp, answer.flatten_lst_comp), ("flatten_recursive", student_recursive, answer.flatten_recursive), ("flatten_higher_order", student_higher_order, answer.flatten_higher_order)]
    success = True
    for name, student, reference in methods:
        tests = [TestCase(test.name.replace("flatten", name), test.expected, test.args) for test in BASE]
        success = run_tests(name, tests, reference if "--answer" in sys.argv else student) and success
    return success


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
