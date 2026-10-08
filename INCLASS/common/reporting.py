from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable


@dataclass(frozen=True)
class TestCase:
    name: str
    expected: str
    args: tuple


def run_tests(title: str, tests: Iterable[TestCase], solve: Callable[..., object]) -> bool:
    print(f"\n{title}")
    print(f"{'Test':<46} {'Expected':<42} {'Got':<42} Status")
    print("-" * 145)
    all_passed = True
    for index, test in enumerate(tests, start=1):
        try:
            got = repr(solve(*test.args))
            passed = got == test.expected
            reason = "" if passed else f"mismatch: expected {test.expected}, got {got}"
        except Exception as error:
            got = f"<error: {type(error).__name__}: {error}>"
            passed = False
            reason = f"{type(error).__name__}: {error}"
        status = "PASS" if passed else "FAIL"
        print(f"{index:02d} {test.name:<43} {test.expected:<42} {got:<42} {status}")
        if reason:
            print(f"   Reason: {reason}")
        all_passed = all_passed and passed
    print(f"Summary: {'PASS' if all_passed else 'FAIL'}")
    return all_passed
