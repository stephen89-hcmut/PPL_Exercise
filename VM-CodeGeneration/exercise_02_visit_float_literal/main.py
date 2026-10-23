import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from common.runtime import FloatLiteral

TESTS = [
    TestCase("FloatLiteral(5.0)", "5.0", lambda: FloatLiteral(5.0)),
    TestCase("FloatLiteral(2.17)", "2.17", lambda: FloatLiteral(2.17)),
    TestCase("FloatLiteral(-1.0)", "-1.0", lambda: FloatLiteral(-1.0)),
    TestCase("FloatLiteral(37.1846)", "37.1846", lambda: FloatLiteral(37.1846)),
    TestCase("FloatLiteral(234.5)", "234.5", lambda: FloatLiteral(234.5)),
]

if __name__ == "__main__":
    module = __import__("answer" if "--answer" in sys.argv else "solution")
    tests = TESTS + ([TestCase("deliberate mismatch", "0.0", lambda: FloatLiteral(5.0))] if "--demo-failure" in sys.argv else [])
    raise SystemExit(0 if run_tests("VM-CodeGeneration 2 - visitFloatLiteral", tests, module.solve) else 1)
