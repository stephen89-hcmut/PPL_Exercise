# PPL AST Part 1

Project Python + ANTLR4 cho 4 bai tap parse tree va AST trong mon Principle of Programming Languages.

## Quick start

Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe AST_Part1\setup.py
.\.venv\Scripts\python.exe AST_Part1\run_all.py --answer
```

Linux/macOS:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python AST_Part1/setup.py
.venv/bin/python AST_Part1/run_all.py --answer
```

Lenh khong co `--answer` chay skeleton trong `solution.py` de sinh vien tu implement. Chi tiet cai dat, generate parser, cau truc project va cach doc report xem `Guid.md`.

Ví dụ chạy một bài INCLASS trên Windows:

```powershell
.\.venv\Scripts\python.exe INCLASS\setup.py
.\.venv\Scripts\python.exe INCLASS\ast_01_ids_recursive\main.py
```

Lệnh trên in các cột `Test`, `Expected`, `Got`, `Status` và `Reason` khi
test thất bại. Dùng `--answer` để chạy lời giải tham chiếu.
