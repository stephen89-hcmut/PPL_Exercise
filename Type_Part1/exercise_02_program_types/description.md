# Type checking a program

## Đề bài

Hoàn thành `StaticCheck` trong `solution.py` cho AST:

```python
class Program:  # decl: List[VarDecl], exp: Exp
class VarDecl:  # name: str, typ: Type
class IntType(Type)
class FloatType(Type)
class BoolType(Type)
class Id(Exp):  # name: str
```

Áp dụng các quy tắc biểu thức của Exercise 1. Môi trường kiểu được tạo từ
danh sách khai báo theo thứ tự. Nếu tên khai báo lặp lại trong cùng chương
trình, ném `RedeclaredDeclaration(name)`. Nếu `Id` không có trong môi trường,
ném `UndeclaredIdentifier(name)`. Kiểu của `Id` là kiểu trong `VarDecl`.

Không đổi public API, tên class hoặc method trong skeleton.

## Expected Output

| Input | Expected |
| --- | --- |
| `Program([VarDecl("x",IntType())],BinOp("+",Id("x"),IntLit(1)))` | `int` |
| `Program([VarDecl("x",IntType())],BinOp("+",Id("x"),FloatLit(3.4)))` | `float` |
| `Program([VarDecl("ok",BoolType())],BinOp("&&",Id("ok"),Id("ok")))` | `bool` |
| `Program([VarDecl("x",IntType())],BinOp("+",Id("x"),Id("y")))` | `Undeclared Identifier: y` |
| `Program([VarDecl("x",IntType()),VarDecl("x",FloatType())],IntLit(1))` | `RedeclaredDeclaration: x` |
| `Program([VarDecl("x",IntType())],BinOp("*",BinOp("+",Id("x"),FloatLit(3.4)),BinOp(">",IntLit(3),FloatLit(2.1)))` | `Type Mismatch In Expression: BinOp(">",IntLit(3),FloatLit(2.1))` |

## Run

Từ thư mục repository root.

Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe Type_Part1\exercise_02_program_types\main.py
.\.venv\Scripts\python.exe Type_Part1\exercise_02_program_types\main.py --answer
.\.venv\Scripts\python.exe Type_Part1\exercise_02_program_types\main.py --demo-failure
```

Trên Linux/macOS:

```bash
.venv/bin/python Type_Part1/exercise_02_program_types/main.py
.venv/bin/python Type_Part1/exercise_02_program_types/main.py --answer
.venv/bin/python Type_Part1/exercise_02_program_types/main.py --demo-failure
```

Bỏ `--answer` để chạy skeleton sinh viên.
