import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from common.runtime import FloatType, IntType, Frame, VarDecl


def declarations():
    frame = Frame()
    return [
        (VarDecl("x", IntType()), None),
        (VarDecl("x", FloatType()), frame),
        (VarDecl("y", IntType()), frame),
        (VarDecl("z", FloatType()), frame),
    ]


def expected(_):
    return ".field static x I\n.var 0 is x F from start to end\n.var 1 is y I from start to end\n.var 2 is z F from start to end"


TESTS = [TestCase("global and local declarations", repr(expected(None)), declarations)]

if __name__ == "__main__":
    module = __import__("answer" if "--answer" in sys.argv else "solution")
    tests = TESTS + ([TestCase("deliberate mismatch", repr("wrong"), declarations)] if "--demo-failure" in sys.argv else [])
    raise SystemExit(0 if run_tests("SEQUENCE 6 - visitVarDecl", tests, module.solve) else 1)
