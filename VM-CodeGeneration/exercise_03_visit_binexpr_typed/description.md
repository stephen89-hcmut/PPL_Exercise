# JVM-CodeGeneration 3 - typed visitBinExpr

## Đề bài

Hoàn thành `visitBinExpr(self, ctx, o)` cho các toán tử `+`, `-`, `*`, `/`,
`+.`, `-.`, `*.`, `/.`. Bốn toán tử đầu nhận hai toán hạng `IntType`; các
toán tử có dấu chấm nhận hai toán hạng `FloatType`. Visitor của đề gốc trả về
một cặp gồm Jasmin code và kiểu kết quả.

Ví dụ của đề gốc:

```text
CallExpr(Id("putInt"), [BinExpr("+", IntLiteral(5), IntLiteral(3))])
=> b'8'
```

`b'8'` là output của chương trình sau khi chạy lời gọi `putInt`, không phải
giá trị trả về trực tiếp từ `visitBinExpr`. Bộ kiểm tra sinh Jasmin instruction cho biểu thức và chạy tập instruction
tương ứng bằng VM nhỏ đi kèm; output được capture dưới dạng bytes như ví dụ
gốc. VM nhỏ không cần cài Jasmin hoặc Java.

## Expected Output

| Input                    | Expected |
| ------------------------ | -------- |
| `5 + 3` | `b'8'` |
| `(5 - 3) * 3` | `b'6'` |
| `-1.0 +. 1.0` | `b'0.0'` |
| `1.0 *. (10.0 -. 2.0)` | `b'8.0'` |
| `(5 - 3) / 3` | `b'0'` |

## Run

Windows PowerShell:

```powershell
python3 VM-CodeGeneration/exercise_03_visit_binexpr_typed/main.py
python3 VM-CodeGeneration/exercise_03_visit_binexpr_typed/main.py --answer
```

Linux/macOS:

```bash
python3 VM-CodeGeneration/exercise_03_visit_binexpr_typed/main.py
python3 VM-CodeGeneration/exercise_03_visit_binexpr_typed/main.py --answer
```
