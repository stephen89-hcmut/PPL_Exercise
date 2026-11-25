import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from common.reporting import TestCase, run_tests
from common.runtime import BinExpr, BoolLiteral, FloatLiteral, IntLiteral

TESTS = [
    TestCase("integer addition emits iadd", "True", lambda: BinExpr("+", IntLiteral(5), IntLiteral(3))),
    TestCase("integer subtraction emits isub", "True", lambda: BinExpr("-", IntLiteral(5), IntLiteral(3))),
    TestCase("integer multiplication emits imul", "True", lambda: BinExpr("*", IntLiteral(5), IntLiteral(3))),
    TestCase("integer division promotes to float", "True", lambda: BinExpr("/", IntLiteral(6), IntLiteral(3))),
    TestCase("mixed addition promotes to float", "True", lambda: BinExpr("+", IntLiteral(2), FloatLiteral(3.0))),
    TestCase("greater-than comparison", "True", lambda: BinExpr(">", IntLiteral(5), IntLiteral(3))),
    TestCase("greater-or-equal comparison", "True", lambda: BinExpr(">=", IntLiteral(5), IntLiteral(5))),
    TestCase("less-than comparison", "True", lambda: BinExpr("<", IntLiteral(2), IntLiteral(3))),
    TestCase("less-or-equal comparison", "True", lambda: BinExpr("<=", IntLiteral(2), IntLiteral(3))),
    TestCase("equal comparison", "True", lambda: BinExpr("==", IntLiteral(3), IntLiteral(3))),
    TestCase("not-equal comparison", "True", lambda: BinExpr("!=", IntLiteral(3), IntLiteral(4))),
    TestCase("&& branches before evaluating right operand", "True", lambda: BinExpr("&&", BoolLiteral(False), BoolLiteral(True))),
    TestCase("|| branches before evaluating right operand", "True", lambda: BinExpr("||", BoolLiteral(True), BoolLiteral(False))),
]

def solve_case(node, module):
    code, typ = module.solve(node)
    if node.op in ("&&", "||"):
        return type(typ).__name__ == "BoolType" and ("ifeq " in code if node.op == "&&" else "ifne " in code)
    if node.op in (">", ">=", "<", "<=", "==", "!="):
        branch = {">": "if_icmpgt", ">=": "if_icmpge", "<": "if_icmplt",
                  "<=": "if_icmple", "==": "if_icmpeq", "!=": "if_icmpne"}[node.op]
        return type(typ).__name__ == "BoolType" and branch in code
    if isinstance(node.e1, IntLiteral) and isinstance(node.e2, FloatLiteral):
        return "i2f" in code and "fadd" in code and type(typ).__name__ == "FloatType"
    mnemonic = {"+": "iadd", "-": "isub", "*": "imul", "/": "fdiv"}[node.op]
    wanted_type = "FloatType" if node.op == "/" else "IntType"
    return mnemonic in code and type(typ).__name__ == wanted_type

if __name__ == "__main__":
    module = __import__("answer" if "--answer" in sys.argv else "solution")
    raise SystemExit(0 if run_tests("VM-CodeGeneration 6 - short-circuit visitBinExpr", TESTS, lambda n: solve_case(n, module)) else 1)
