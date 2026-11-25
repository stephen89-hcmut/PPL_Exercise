# JVM-CodeGeneration 6 - short-circuit visitBinExpr

## Đề bài

Hoàn thành `StudentEmitter.emitANDOR(self, op, left_code, right_code, frame)` và `StudentCodeGeneration.visitBinExpr(self, ctx, o)`. Visitor trả về `(code, type)` cho các toán tử `+`, `-`, `*`, `/`, `>`, `>=`, `<`, `<=`, `==`, `!=`, `&&`, `||`. Các phép số học phải chọn lệnh integer/float tương ứng và chuyển `IntType` sang `FloatType` khi một vế là float; `/` cho kết quả `FloatType`. So sánh và phép logic trả về `BoolType`.

Hai phép logic phải dùng short-circuit: `&&` nhảy qua vế phải khi vế trái false; `||` nhảy qua vế phải khi vế trái true. Kết quả logic được biểu diễn trên stack bằng `iconst_0` hoặc `iconst_1`. Harness đã cung cấp `generate(node)` để sinh mã literal và đệ quy xử lý biểu thức con. Phương thức emitter nhận toán tử, mã của hai vế, và frame để cấp nhãn.

## Expected Output

Runner kiểm tra mã lệnh arithmetic, ép kiểu số, branch cho từng phép so sánh, và branch short-circuit của cả hai phép logic. Ví dụ: `5 + 3` sinh `iadd`; `2 + 3.0` sinh chuyển đổi `i2f` cùng `fadd`; `false && true` sinh nhánh `ifeq` trước mã của vế phải.

## Run

Windows PowerShell:

```powershell
py VM-CodeGeneration/exercise_06_visit_binexpr_short_circuit/main.py
py VM-CodeGeneration/exercise_06_visit_binexpr_short_circuit/main.py --answer
```

Linux/macOS:

```bash
python3 VM-CodeGeneration/exercise_06_visit_binexpr_short_circuit/main.py
python3 VM-CodeGeneration/exercise_06_visit_binexpr_short_circuit/main.py --answer
```

Bỏ `--answer` để chạy skeleton trong `solution.py`.
