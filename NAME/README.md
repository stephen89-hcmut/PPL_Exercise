# NAME exercises

This group implements the four questions in
`source/[CC03] Name Programming Code_ Attempt review _ BK-LMS.pdf`.

| Exercise | PDF question | Focus |
| --- | --- | --- |
| `exercise_01_redeclared_declaration` | 1 | One exception for any duplicate declaration |
| `exercise_02_redeclared_kind` | 2 | Variable versus constant duplicate exceptions |
| `exercise_03_redeclared_nested` | 3 | Program/function scopes and duplicate declarations |
| `exercise_04_undeclared_identifier` | 4 | Scope lookup and undeclared identifiers |

Each exercise contains `description.md`, `solution.py`, `answer.py`, and
`main.py`. Students edit only `solution.py`. The reference implementation is
selected with `--answer`; `--demo-failure` adds a deliberate mismatch.

## Run

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe NAME\run_all.py --answer
.\.venv\Scripts\python.exe NAME\exercise_01_redeclared_declaration\main.py
```

Linux/macOS:

```bash
.venv/bin/python NAME/run_all.py --answer
.venv/bin/python NAME/exercise_01_redeclared_declaration/main.py
```
