# Abstract 3 - visitIf

## Đề bài

Hoàn thành `visitIf(self, ctx, o)` cho AST `If(expr, tstmt, estmt)`.
`estmt` có thể là `None`. Duyệt điều kiện với `Access(..., False)`, sinh
nhãn else/exit khi có nhánh else, và sinh nhãn exit khi không có else.

## Expected Output

| Input | Expected |
| --- | --- |
| `if (true) putInt(10) else putInt(20)` | `b'10'` |
| `if (false) putInt(10) else putInt(20)` | `b'20'` |

## Run

Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe ABSTRACT\exercise_03_visit_if\main.py
.\.venv\Scripts\python.exe ABSTRACT\exercise_03_visit_if\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python ABSTRACT/exercise_03_visit_if/main.py
.venv/bin/python ABSTRACT/exercise_03_visit_if/main.py --answer
```
