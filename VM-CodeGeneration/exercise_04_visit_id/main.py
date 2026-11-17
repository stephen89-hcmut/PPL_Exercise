import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from common.runtime import CName, FloatType, Id, Index, IntType, Symbol


def case(name, value, typ, local=False, shadow=False):
    location = Index(0) if local else CName("Program")
    symbols = [Symbol(name, typ, location)]
    if shadow:
        symbols.append(Symbol(name, typ, CName("Program")))
    return {"node": Id(name), "values": {name: value}, "symbols": symbols}


TESTS = [
    TestCase("global integer a", "b'12'", lambda: case("a", 12, IntType())),
    TestCase("global integer z", "b'22'", lambda: case("z", 22, IntType())),
    TestCase("global float x", "b'12.5'", lambda: case("x", 12.5, FloatType())),
    TestCase("global float y", "b'1.25'", lambda: case("y", 1.25, FloatType())),
    TestCase("global float n", "b'1.222'", lambda: case("n", 1.222, FloatType())),
    TestCase("local integer m", "b'12220'", lambda: case("m", 12220, IntType(), local=True)),
    TestCase("nearest local symbol shadows global", "b'7'", lambda: case("x", 7, IntType(), local=True, shadow=True)),
]

if __name__ == "__main__":
    module = __import__("answer" if "--answer" in sys.argv else "solution")
    tests = TESTS + ([TestCase("deliberate mismatch", "b'0'", lambda: case("a", 12, IntType()))] if "--demo-failure" in sys.argv else [])
    raise SystemExit(0 if run_tests("VM-CodeGeneration 4 - visitId", tests, module.solve) else 1)
