# JVM-CodeGeneration 5 - mixed visitBinExpr

## Đề bài

Hoàn thành `visitBinExpr(self, ctx, o)` với `+`, `-`, `*`, `/`, `>`, `<`,
`>=`, `<=`, `!=`, `==`. Nếu một toán hạng là float thì ép toán hạng còn lại
sang `FloatType`; phép `/` luôn trả về `FloatType`. Các phép so sánh trả về
`BoolType`, còn `+`, `-`, `*`, `/` trả về kiểu số tương ứng.

## Expected Output

| Input               | Expected     |
| ------------------- | ------------ |
| `5 > 3`           | `b'True'`  |
| `(5 - 3) * 3.0`   | `b'6.0'`   |
| `-1.0 + 1.0`      | `b'0.0'`   |
| `2 * (10.0 - 2)`  | `b'16.0'`  |
| `(9 - 3) / 3`     | `b'2.0'`   |
| `2 >= (10.0 - 2)` | `b'False'` |
| `2 == (10.0 / 5)` | `b'True'`  |
| `2 != (4 - 2)`    | `b'False'` |

## Run

Windows PowerShell:

```powershell
python3 VM-CodeGeneration/exercise_05_visit_binexpr_mixed/main.py
python3 VM-CodeGeneration/exercise_05_visit_binexpr_mixed/main.py --answer
```

Linux/macOS:

```bash
python3 VM-CodeGeneration/exercise_05_visit_binexpr_mixed/main.py
python3 VM-CodeGeneration/exercise_05_visit_binexpr_mixed/main.py --answer
```
