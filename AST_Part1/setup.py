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


def download_jar() -> None:
    if JAR.exists():
        return
    if os.environ.get("ANTLR_JAR"):
        raise FileNotFoundError(f"ANTLR_JAR does not exist: {JAR}")
    url = f"https://www.antlr.org/download/antlr4-python3-runtime-{VERSION}.jar"
    # The official complete tool uses a different filename than the runtime package.
    url = f"https://www.antlr.org/download/antlr-{VERSION}-complete.jar"
    print(f"Downloading {url}")
    urllib.request.urlretrieve(url, JAR)


def generate(grammar_name: str, output_name: str) -> None:
    output_dir = GENERATED_DIR / output_name
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True)
    grammar = GRAMMAR_DIR / grammar_name
    command = [
        "java", "-jar", str(JAR), "-Dlanguage=Python3", "-visitor",
        "-o", str(output_dir), str(grammar),
    ]
    subprocess.run(command, check=True, cwd=ROOT)
    (output_dir / "__init__.py").touch()


def main() -> None:
    download_jar()
    generate("MPRecursive.g4", "recursive")
    generate("MPRepeated.g4", "repeated")
    print(f"Generated parsers in {GENERATED_DIR}")


if __name__ == "__main__":
    main()
