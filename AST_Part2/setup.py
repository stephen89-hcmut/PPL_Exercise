from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
JAR = Path(os.environ.get("ANTLR_JAR", ROOT.parent / "ANTLR-4.13.2-complete.jar")).expanduser()
GRAMMAR_DIR = ROOT / "grammar"
GENERATED_DIR = ROOT / "generated"
GRAMMARS = [
    "MPExprRecursive",
    "MPExprRepeated",
    "MPTypeRecursive",
    "MPTypeRepeated",
]


def main() -> None:
    if not JAR.exists():
        raise FileNotFoundError(f"ANTLR jar not found: {JAR}")
    for grammar_name in GRAMMARS:
        output_dir = GENERATED_DIR / grammar_name
        if output_dir.exists():
            shutil.rmtree(output_dir)
        output_dir.mkdir(parents=True)
        subprocess.run(
            ["java", "-jar", str(JAR), "-Dlanguage=Python3", "-visitor", "-o", str(output_dir), str(GRAMMAR_DIR / f"{grammar_name}.g4")],
            check=True,
            cwd=ROOT,
        )
        (output_dir / "__init__.py").touch()
    print(f"Generated parsers in {GENERATED_DIR}")


if __name__ == "__main__":
    main()
