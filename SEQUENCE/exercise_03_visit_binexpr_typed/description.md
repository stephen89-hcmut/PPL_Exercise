# Sequence 3 - typed visitBinExpr

## Đề bài

Hoàn thành `visitBinExpr(self, ctx, o)` cho các toán tử `+`, `-`, `*`, `/`,
`+.`, `-.`, `*.`, `/.`. Bốn toán tử đầu làm việc trên `IntType`; các toán
tử có dấu chấm làm việc trên `FloatType`. Trả về code biểu thức và kiểu kết
quả tương ứng.

## Expected Output

| Input | Expected |
| --- | --- |
| `5 + 3` | `8` |
| `(5 - 3) * 3` | `6` |
| `-1.0 +. 1.0` | `0.0` |
| `1.0 *. (10.0 -. 2.0)` | `8.0` |
| `(5 - 3) / 3` | `0` |

## Run

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe SEQUENCE\exercise_03_visit_binexpr_typed\main.py
.\.venv\Scripts\python.exe SEQUENCE\exercise_03_visit_binexpr_typed\main.py --answer
```

Linux/macOS:

```bash
.venv/bin/python SEQUENCE/exercise_03_visit_binexpr_typed/main.py
.venv/bin/python SEQUENCE/exercise_03_visit_binexpr_typed/main.py --answer
```
