from dataclasses import dataclass

@dataclass(frozen=True)
class IfCase:
    pass

@dataclass(frozen=True)
class WhileCase:
    pass

@dataclass(frozen=True)
class ForCase:
    pass

CASES = [
    ("if (a > b) a = 1; else a = 2", IfCase()),
    ("while (a < 10) a = a + 1", WhileCase()),
    ("for (a = 1; a < 10; a++) b = b + 1", ForCase()),
]
