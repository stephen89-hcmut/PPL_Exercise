from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
EXERCISES = sorted(path / "main.py" for path in ROOT.glob("exercise_*") if (path / "main.py").exists())


def main() -> int:
    failed = False
    for exercise in EXERCISES:
        result = subprocess.run([sys.executable, str(exercise), *sys.argv[1:]], cwd=ROOT.parent)
        failed |= result.returncode != 0
    print(f"\nVM-CodeGeneration summary: {'FAIL' if failed else 'PASS'}")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())
