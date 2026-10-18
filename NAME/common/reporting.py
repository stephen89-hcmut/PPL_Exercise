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
    print(f"{'Test':<28} {'Expected':<54} {'Got':<54} Status")
    print("-" * 150)
    all_passed = True
    for index, test in enumerate(tests, start=1):
        try:
            got = str(solve(test.value))
            passed = got == test.expected
            reason = "" if passed else f"mismatch: expected {test.expected!r}, got {got!r}"
        except Exception as error:
            got = f"{type(error).__name__}: {error}"
            passed = False
            reason = f"{type(error).__name__}: {error}"
        print(f"{index:02d} {test.name:<25} {test.expected:<54} {got:<54} {'PASS' if passed else 'FAIL'}")
        if reason:
            print(f"   Reason: {reason}")
        all_passed = all_passed and passed
    print(f"Summary: {'PASS' if all_passed else 'FAIL'}")
    return all_passed
