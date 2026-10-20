from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable


@dataclass(frozen=True)
class TestCase:
    name: str
    expected: str
    value: object


def run_tests(title: str, tests: Iterable[TestCase], solve: Callable[[object], object]) -> bool:
    print(f"\n{title}")
    print(f"{'Test':<30} {'Expected':<60} {'Got':<60} Status")
    print("-" * 165)
    passed_all = True
    for index, test in enumerate(tests, 1):
        try:
            got = str(solve(test.value))
            passed = got == test.expected
            reason = "" if passed else f"mismatch: expected {test.expected!r}, got {got!r}"
        except Exception as error:
            got = f"{type(error).__name__}: {error}"
            passed = False
            reason = f"{type(error).__name__}: {error}"
        print(f"{index:02d} {test.name:<27} {test.expected:<60} {got:<60} {'PASS' if passed else 'FAIL'}")
        if reason:
            print(f"   Reason: {reason}")
        passed_all = passed_all and passed
    print(f"Summary: {'PASS' if passed_all else 'FAIL'}")
    return passed_all
