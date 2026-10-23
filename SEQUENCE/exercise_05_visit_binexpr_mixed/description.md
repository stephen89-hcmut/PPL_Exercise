# Sequence 5 - mixed visitBinExpr

## Đề bài

Hoàn thành `visitBinExpr(self, ctx, o)` với `+`, `-`, `*`, `/`, `>`, `<`,
`>=`, `<=`, `!=`, `==`. Nếu một toán hạng là float thì ép toán hạng còn lại
sang `FloatType`; phép `/` luôn trả về `FloatType`. Các phép so sánh trả về
`BoolType`, còn `+`, `-`, `*`, `/` trả về kiểu số tương ứng.

## Expected Output

| Input | Expected |
| --- | --- |
| `5 > 3` | `True` |
| `(5 - 3) * 3.0` | `6.0` |
| `-1.0 + 1.0` | `0.0` |
| `2 * (10.0 - 2)` | `16.0` |
| `(9 - 3) / 3` | `2.0` |
| `2 >= (10.0 - 2)` | `False` |
| `2 == (10.0 / 5)` | `True` |
| `2 != (4 - 2)` | `False` |

## Run

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe SEQUENCE\exercise_05_visit_binexpr_mixed\main.py
.\.venv\Scripts\python.exe SEQUENCE\exercise_05_visit_binexpr_mixed\main.py --answer
```

Linux/macOS:

```bash
.venv/bin/python SEQUENCE/exercise_05_visit_binexpr_mixed/main.py
.venv/bin/python SEQUENCE/exercise_05_visit_binexpr_mixed/main.py --answer
```
