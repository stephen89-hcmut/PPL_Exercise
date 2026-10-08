from __future__ import annotations

import os
import shutil
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VERSION = os.environ.get("ANTLR_VERSION", "4.13.2")
JAR = Path(os.environ["ANTLR_JAR"]).expanduser() if os.environ.get("ANTLR_JAR") else ROOT.parent / f"ANTLR-{VERSION}-complete.jar"
GRAMMAR_DIR = ROOT / "grammar"
GENERATED_DIR = ROOT / "generated"


def main() -> None:
    if not JAR.exists():
        if os.environ.get("ANTLR_JAR"):
            raise FileNotFoundError(f"ANTLR_JAR does not exist: {JAR}")
        url = f"https://www.antlr.org/download/antlr-{VERSION}-complete.jar"
        print(f"Downloading {url}")
        urllib.request.urlretrieve(url, JAR)
    for grammar in GRAMMAR_DIR.glob("*.g4"):
        name = grammar.stem
        output = GENERATED_DIR / name
        if output.exists():
            shutil.rmtree(output)
        output.mkdir(parents=True)
        subprocess.run(["java", "-jar", str(JAR), "-Dlanguage=Python3", "-visitor", "-o", str(output), str(grammar)], check=True, cwd=ROOT)
        (output / "__init__.py").touch()
    print(f"Generated parsers in {GENERATED_DIR}")


if __name__ == "__main__":
    main()
