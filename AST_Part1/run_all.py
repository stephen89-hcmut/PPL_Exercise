from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXERCISES = [
    ROOT / "exercise_01_height" / "main.py",
    ROOT / "exercise_02_non_terminal_count" / "main.py",
    ROOT / "exercise_03_ast_generation_recursive" / "main.py",
    ROOT / "exercise_04_ast_generation_repeated" / "main.py",
]


def main() -> int:
    failed = False
    for exercise in EXERCISES:
        result = subprocess.run([sys.executable, str(exercise), *sys.argv[1:]], cwd=ROOT.parent)
        failed = failed or result.returncode != 0
    print("\nAST Part 1 summary: " + ("FAIL" if failed else "PASS"))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
