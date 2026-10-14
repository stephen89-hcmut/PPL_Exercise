from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable


@dataclass(frozen=True)
class TestCase:
    source: str
    expected: str
    start_rule: str = "program"


def run_tests(title: str, tests: Iterable[TestCase], solve: Callable[[str, str], object]) -> bool:
    print(f"\n{title}")
    print(f"{'Test':<28} {'Expected':<72} {'Got':<72} Status")
    print("-" * 190)
    all_passed = True
    for index, test in enumerate(tests, start=1):
        try:
            got = str(solve(test.source, test.start_rule))
            passed = got == test.expected
            reason = "" if passed else f"mismatch: expected {test.expected!r}, got {got!r}"
        except Exception as error:
            got = f"<error: {error}>"
            passed = False
            reason = f"{type(error).__name__}: {error}"
        print(f"{index:02d} {test.source!r:<25} {test.expected!r:<72} {got!r:<72} {'PASS' if passed else 'FAIL'}")
        if reason:
            print(f"   Reason: {reason}")
        all_passed = all_passed and passed
    print(f"Summary: {'PASS' if all_passed else 'FAIL'}")
    return all_passed
