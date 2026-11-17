# JVM-CodeGeneration 2 - visitFloatLiteral

## Đề bài

Hoàn thành `visitFloatLiteral(self, ctx, o)` cho AST
`FloatLiteral(value)`. Dùng `emitPUSHFCONST(ctx.value, o.frame)` và trả về
`(code, FloatType())`.

## Expected Output

| Input                     | Expected    |
| ------------------------- | ----------- |
| `FloatLiteral(5.0)` | `b'5.0'` |
| `FloatLiteral(2.17)` | `b'2.17'` |
| `FloatLiteral(-1.0)` | `b'-1.0'` |
| `FloatLiteral(37.1846)` | `b'37.1846'` |
| `FloatLiteral(234.5)` | `b'234.5'` |

## Run

Windows PowerShell:

```powershell
python3 VM-CodeGeneration/exercise_02_visit_float_literal/main.py
python3 VM-CodeGeneration/exercise_02_visit_float_literal/main.py --answer
```

Linux/macOS:

```bash
python3 VM-CodeGeneration/exercise_02_visit_float_literal/main.py
python3 VM-CodeGeneration/exercise_02_visit_float_literal/main.py --answer
```
