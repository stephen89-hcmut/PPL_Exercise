from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXERCISES = [
    ROOT / "oop_01_eval" / "main.py",
    ROOT / "oop_02_print_prefix" / "main.py",
    ROOT / "oop_03_visitor" / "main.py",
]

failed = False
for exercise in EXERCISES:
    result = subprocess.run([sys.executable, str(exercise), *sys.argv[1:]], cwd=ROOT.parent)
    failed = failed or result.returncode != 0
print(f"\nOOP summary: {'FAIL' if failed else 'PASS'}")
raise SystemExit(1 if failed else 0)
