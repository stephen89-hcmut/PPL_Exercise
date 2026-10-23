# Sequence 1 - visitIntLiteral

## Đề bài

Hoàn thành `visitIntLiteral(self, ctx, o)` cho AST `IntLiteral(value)`.
Method phải dùng `emitPUSHICONST(ctx.value, o.frame)` và trả về cặp
`(code, IntType())`.

## Expected Output

| Input | Expected |
| --- | --- |
| `IntLiteral(5)` | `5` |
| `IntLiteral(217)` | `217` |
| `IntLiteral(-1)` | `-1` |
| `IntLiteral(371846)` | `371846` |
| `IntLiteral(2345)` | `2345` |

## Run

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe SEQUENCE\exercise_01_visit_int_literal\main.py
.\.venv\Scripts\python.exe SEQUENCE\exercise_01_visit_int_literal\main.py --answer
```

Linux/macOS:

```bash
.venv/bin/python SEQUENCE/exercise_01_visit_int_literal/main.py
.venv/bin/python SEQUENCE/exercise_01_visit_int_literal/main.py --answer
```
