# Sequence 2 - visitFloatLiteral

## Đề bài

Hoàn thành `visitFloatLiteral(self, ctx, o)` cho AST
`FloatLiteral(value)`. Dùng `emitPUSHFCONST(ctx.value, o.frame)` và trả về
`(code, FloatType())`.

## Expected Output

| Input | Expected |
| --- | --- |
| `FloatLiteral(5.0)` | `5.0` |
| `FloatLiteral(2.17)` | `2.17` |
| `FloatLiteral(-1.0)` | `-1.0` |
| `FloatLiteral(37.1846)` | `37.1846` |
| `FloatLiteral(234.5)` | `234.5` |

## Run

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe SEQUENCE\exercise_02_visit_float_literal\main.py
.\.venv\Scripts\python.exe SEQUENCE\exercise_02_visit_float_literal\main.py --answer
```

Linux/macOS:

```bash
.venv/bin/python SEQUENCE/exercise_02_visit_float_literal/main.py
.venv/bin/python SEQUENCE/exercise_02_visit_float_literal/main.py --answer
```
