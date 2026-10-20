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

## NAME

`NAME` chứa bốn bài theo toàn bộ câu hỏi trong PDF
`source/[CC03] Name Programming Code_ Attempt review _ BK-LMS.pdf`:

1. `exercise_01_redeclared_declaration`: một exception chung cho duplicate.
2. `exercise_02_redeclared_kind`: phân biệt variable và constant.
3. `exercise_03_redeclared_nested`: function scope và nested redeclaration.
4. `exercise_04_undeclared_identifier`: lookup theo scope và undeclared ID.

Chạy reference answers trên Windows:

```powershell
.\.venv\Scripts\python.exe NAME\run_all.py --answer
```

Chạy trên Linux/macOS:

```bash
.venv/bin/python NAME/run_all.py --answer
```

Mỗi folder exercise có `description.md`, `solution.py`, `answer.py` và
`main.py`; sinh viên chỉ sửa `solution.py`.

## Type_Part1

`Type_Part1` được tạo từ PDF `[CC03] Type Programming Code 1` và
`[CC03] Type Programming 2`, gồm năm bài: kiểm tra kiểu biểu thức, chương
trình có khai báo biến, block scope và function call. Chạy reference answers:

```powershell
.\.venv\Scripts\python.exe Type_Part1\run_all.py --answer
```

```bash
.venv/bin/python Type_Part1/run_all.py --answer
```

Bỏ `--answer` để chạy skeleton sinh viên. Xem thêm
`Type_Part1/README.md` và `Type_Part1/Guid.md`.
