import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from common.runtime import IntLiteral

TESTS = [
    TestCase("IntLiteral(5)", "5", lambda: IntLiteral(5)),
    TestCase("IntLiteral(217)", "217", lambda: IntLiteral(217)),
    TestCase("IntLiteral(-1)", "-1", lambda: IntLiteral(-1)),
    TestCase("IntLiteral(371846)", "371846", lambda: IntLiteral(371846)),
    TestCase("IntLiteral(2345)", "2345", lambda: IntLiteral(2345)),
]

if __name__ == "__main__":
    module = __import__("answer" if "--answer" in sys.argv else "solution")
    tests = TESTS + ([TestCase("deliberate mismatch", "0", lambda: IntLiteral(5))] if "--demo-failure" in sys.argv else [])
    raise SystemExit(0 if run_tests("VM-CodeGeneration 1 - visitIntLiteral", tests, module.solve) else 1)
