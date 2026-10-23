from dataclasses import dataclass


@dataclass(frozen=True)
class TestCase:
    name: str
    expected: str
    factory: object


def run_tests(title, tests, solve):
    print(f"\n{title}")
    print(f"{'Test':<58} {'Expected':<18} {'Got':<18} Status")
    print("-" * 105)
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
        print(f"{number:02d} {test.name:<55} {test.expected:<18} {got:<18} {'PASS' if passed else 'FAIL'}")
        if reason:
            print(f"   Reason: {reason}")
        passed_all &= passed
    print(f"Summary: {'PASS' if passed_all else 'FAIL'}")
    return passed_all
