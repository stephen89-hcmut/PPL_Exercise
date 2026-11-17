# SEQUENCE

Questions 1–5 are aligned with the real assessment prompts provided:

1. `visitIntLiteral` emits an integer constant and returns `IntType`.
2. `visitFloatLiteral` emits a float constant and returns `FloatType`.
3. `visitBinExpr` handles typed integer and float arithmetic operators and
   returns generated Jasmin code with the result type.
4. `visitId` resolves local and global symbols in innermost to outermost order.
5. `visitBinExpr` handles mixed numeric operations, promotions, and relations.

Question 6 remains an additional practice task from the earlier local set; its
assessment prompt was not provided.

Each question has `description.md`, `solution.py`, `answer.py`, and `main.py`.
Edit `solution.py`; `answer.py` contains the reference implementation. The
local runner evaluates expressions to make the expected result easy to read;
the assessment site wraps its output as bytes, for example `b'8'`.

## Run

Windows PowerShell:

```powershell
python3 SEQUENCE/run_all.py
python3 SEQUENCE/run_all.py --answer
```

Linux/macOS:

```bash
python3 SEQUENCE/run_all.py
python3 SEQUENCE/run_all.py --answer
```
