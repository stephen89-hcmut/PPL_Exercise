# VM-CodeGeneration

Năm bài tập được tạo từ PDF `[CC03]JVM&Code Programming`:

1. `visitIntLiteral`
2. `visitFloatLiteral`
3. `visitBinExpr` cho toán tử integer/float typed
4. `visitId` cho local/global symbol lookup
5. `visitBinExpr` cho mixed numeric types và relational operators

Mỗi bài có `description.md`, `solution.py`, `answer.py` và `main.py`.
Sinh viên chỉ sửa `solution.py`; `answer.py` là reference answer. Runtime
nhỏ trong `common/runtime.py` mô phỏng protocol `CodeGeneration`, `Emitter`,
`Frame`, `Type` và AST để test chạy độc lập mà không cần cài Jasmin.

## Run

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe VM-CodeGeneration\run_all.py
.\.venv\Scripts\python.exe VM-CodeGeneration\run_all.py --answer
.\.venv\Scripts\python.exe VM-CodeGeneration\exercise_05_visit_binexpr_mixed\main.py --demo-failure
```

Linux/macOS:

```bash
.venv/bin/python VM-CodeGeneration/run_all.py
.venv/bin/python VM-CodeGeneration/run_all.py --answer
.venv/bin/python VM-CodeGeneration/exercise_05_visit_binexpr_mixed/main.py --demo-failure
```
