# AST Part 2

This part contains four ANTLR-based AST generation exercises:

1. Expression AST with recursive assignment and logical operators.
2. Expression AST with repeated grammar rules.
3. Type AST with recursive dimension aggregation.
4. Type AST with recursive array dimensions.

## Setup

Windows PowerShell:

```powershell
py -m venv .venv
python3 -m pip install -r requirements.txt
python3 AST_Part2/setup.py
```

Linux/macOS:

```bash
python3 -m pip install -r requirements.txt
python3 AST_Part2/setup.py
```

The setup command regenerates parser files under `AST_Part2/generated/`.

## Run

Run all reference tests:

```bash
python3 AST_Part2/run_all.py --answer
```

Run one exercise with the student skeleton:

```bash
python3 AST_Part2/exercise_01_expr_recursive/main.py
```

Use `--demo-failure` to see a deliberate FAIL row and its reason.

Windows PowerShell:

```powershell
python3 AST_Part2/run_all.py --answer
python3 AST_Part2/exercise_01_expr_recursive/main.py
```
