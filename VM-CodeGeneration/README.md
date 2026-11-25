# VM-CodeGeneration

Bảy bài tập được tạo từ PDF và slide `[CC03]JVM&Code Programming`:

1. `visitIntLiteral`
2. `visitFloatLiteral`
3. `visitBinExpr` cho toán tử integer/float typed
4. `visitId` cho local/global symbol lookup
5. `visitBinExpr` cho mixed numeric types và relational operators
6. `visitBinExpr` cho arithmetic, relational, `&&`, `||` với short-circuit
7. Sinh Jasmin cho `if/else`, `while` và `for`

Mỗi bài có `description.md`, `solution.py`, `answer.py` và `main.py`.
Sinh viên chỉ sửa `solution.py`; `answer.py` là reference answer. Runtime
trong `common/runtime.py` cung cấp API `CodeGeneration`, `Emitter`, `Frame`,
`Type` và AST tương thích với các visitor trong đề. Runner sinh Jasmin
instruction, chạy tập instruction được dùng trong năm bài bằng VM nhỏ, rồi
so sánh output dạng bytes (ví dụ `b'8'`) mà không cần cài Jasmin.

## Run

Windows PowerShell:

```powershell
py VM-CodeGeneration/run_all.py
py VM-CodeGeneration/run_all.py --answer
py VM-CodeGeneration/exercise_05_visit_binexpr_mixed/main.py --demo-failure
py VM-CodeGeneration/exercise_06_visit_binexpr_short_circuit/main.py --answer
py VM-CodeGeneration/exercise_07_visit_control_flow/main.py --answer
```

Linux/macOS:

```bash
python3 VM-CodeGeneration/run_all.py
python3 VM-CodeGeneration/run_all.py --answer
python3 VM-CodeGeneration/exercise_05_visit_binexpr_mixed/main.py --demo-failure
python3 VM-CodeGeneration/exercise_06_visit_binexpr_short_circuit/main.py --answer
python3 VM-CodeGeneration/exercise_07_visit_control_flow/main.py --answer
```
