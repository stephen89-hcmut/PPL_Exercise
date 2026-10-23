from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TestCase:
    name: str
    expected: str
    factory: object


def run_tests(title: str, tests: list[TestCase], solve) -> bool:
    print(f"\n{title}")
    print(f"{'Test':<50} {'Expected':<14} {'Got':<14} Status")
    print("-" * 90)
    passed_all = True
    for number, test in enumerate(tests, 1):
        try:
            got = repr(solve(test.factory()))
            passed = got == test.expected
            reason = "" if passed else f"mismatch: expected {test.expected}, got {got}"
        except Exception as error:
            got = f"<error: {type(error).__name__}: {error}>"
            passed = False
            reason = f"{type(error).__name__}: {error}"
        print(f"{number:02d} {test.name:<47} {test.expected:<14} {got:<14} {'PASS' if passed else 'FAIL'}")
        if reason:
            print(f"   Reason: {reason}")
        passed_all &= passed
    print(f"Summary: {'PASS' if passed_all else 'FAIL'}")
    return passed_all
