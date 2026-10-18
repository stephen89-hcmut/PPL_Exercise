from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXERCISES = sorted(
    path / "main.py"
    for path in ROOT.iterdir()
    if path.is_dir() and path.name != "common" and (path / "main.py").exists()
)

failed = False
for exercise in EXERCISES:
    result = subprocess.run([sys.executable, str(exercise), *sys.argv[1:]], cwd=ROOT.parent)
    failed = failed or result.returncode != 0
print(f"\nNAME summary: {'FAIL' if failed else 'PASS'}")
raise SystemExit(1 if failed else 0)
