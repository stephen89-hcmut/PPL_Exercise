# AST Part 2 Guide

## Student workflow

1. Generate the parsers with the virtual-environment Python executable.
2. Open one exercise directory and implement the methods in `solution.py`.
3. Run the exercise-specific `main.py`.
4. Use `--answer` to compare with the reference implementation.
5. Use `--demo-failure` to inspect failure reporting.

The expected output strings are exact. The runner continues after exceptions and returns exit code 0 only when every selected case passes.

## Cross-platform commands

Windows PowerShell:

```powershell
py -m venv .venv
python3 -m pip install -r requirements.txt
python3 AST_Part2/setup.py
python3 AST_Part2/exercise_01_expr_recursive/main.py
python3 AST_Part2/exercise_01_expr_recursive/main.py --answer
```

Linux/macOS:

```bash
python3 -m venv .venv
python3 -m pip install -r requirements.txt
python3 AST_Part2/setup.py
python3 AST_Part2/exercise_01_expr_recursive/main.py
python3 AST_Part2/exercise_01_expr_recursive/main.py --answer
```
