from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXERCISES = sorted(path / "main.py" for path in ROOT.iterdir() if path.is_dir() and path.name != "common" and (path / "main.py").exists())


def main() -> int:
    failed = False
    for exercise in EXERCISES:
        result = subprocess.run([sys.executable, str(exercise), *sys.argv[1:]], cwd=ROOT.parent)
        failed = failed or result.returncode != 0
    print(f"\nINCLASS summary: {'FAIL' if failed else 'PASS'}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
