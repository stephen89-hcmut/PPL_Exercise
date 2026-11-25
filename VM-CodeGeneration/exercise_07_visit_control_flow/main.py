import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from cases import CASES

EXPECTED = [
    "iload_0\niload_1\nif_icmple L0\niconst_1\nistore_0\ngoto L1\nL0:\niconst_2\nistore_0\nL1:",
    "L0:\niload_0\nbipush 10\nif_icmpge L1\niload_0\niconst_1\niadd\nistore_0\ngoto L0\nL1:",
    "iconst_1\nistore_0\nL0:\niload_0\nbipush 10\nif_icmpge L1\niload_1\niconst_1\niadd\nistore_1\niinc 0 1\ngoto L0\nL1:",
]

if __name__ == "__main__":
    module = __import__("answer" if "--answer" in sys.argv else "solution")
    tests = [TestCase(name, repr(EXPECTED[i]), lambda case=case: module.solve(case))
             for i, (name, case) in enumerate(CASES)]
    raise SystemExit(0 if run_tests("VM-CodeGeneration 7 - control-flow Jasmin", tests, lambda value: value) else 1)
