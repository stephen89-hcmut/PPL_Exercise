from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable


@dataclass(frozen=True)
class TestCase:
    name: str
    expected: str
    call: Callable[[], object]


def run_tests(title: str, tests: Iterable[TestCase]) -> bool:
    print(f"\n{title}")
    print(f"{'Test':<55} {'Expected':<32} {'Got':<32} Status")
    print("-" * 130)
    success = True
    for index, test in enumerate(tests, start=1):
        try:
            got_value = test.call()
            got = str(got_value)
            passed = got == test.expected
            reason = "" if passed else f"mismatch: expected {test.expected!r}, got {got!r}"
        except Exception as error:
            got = f"<error: {type(error).__name__}: {error}>"
            passed = False
            reason = f"{type(error).__name__}: {error}"
        status = "PASS" if passed else "FAIL"
        print(f"{index:02d} {test.name:<52} {test.expected:<32} {got:<32} {status}")
        if reason:
            print(f"   Reason: {reason}")
        success = success and passed
    print(f"Summary: {'PASS' if success else 'FAIL'}")
    return success
