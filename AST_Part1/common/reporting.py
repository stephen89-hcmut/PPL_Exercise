from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable


@dataclass(frozen=True)
class TestCase:
    source: str
    expected: str
    start_rule: str = "program"


def run_tests(title: str, tests: Iterable[TestCase], solve: Callable[[str], object]) -> bool:
    print(f"\n{title}")
    print(f"{'Test':<28} {'Expected':<48} {'Got':<48} Status")
    print("-" * 140)
    all_passed = True

    for index, test in enumerate(tests, start=1):
        reason = ""
        try:
            got = str(solve(test.source, test.start_rule))
            passed = got == test.expected
            if not passed:
                reason = f"mismatch: expected {test.expected!r}, got {got!r}"
        except Exception as error:  # report one broken case without hiding later cases
            got = f"<error: {error}>"
            passed = False
            reason = f"{type(error).__name__}: {error}"

        status = "PASS" if passed else "FAIL"
        print(f"{index:02d} {test.source!r:<25} {test.expected!r:<48} {got!r:<48} {status}")
        if reason:
            print(f"   Reason: {reason}")
        all_passed = all_passed and passed

    print(f"Summary: {'PASS' if all_passed else 'FAIL'}")
    return all_passed
