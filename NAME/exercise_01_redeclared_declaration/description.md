# NAME Exercise 1 - RedeclaredDeclaration

## Đề bài

AST của ngôn ngữ:

```python
class Program:       # decl: List[Decl]
class Decl(ABC)
class VarDecl(Decl): # name: str, typ: Type
class ConstDecl(Decl): # name: str, val: Lit
class Type(ABC)
class IntType(Type)
class FloatType(Type)
class Lit(ABC)
class IntLit(Lit):   # val: int
```

Exception:

```python
class RedeclaredDeclaration(Exception):
    # name: str
```

Hãy hoàn thành class `StaticCheck` trong `solution.py` để duyệt toàn bộ danh
sách `Program.decl`. Mọi khai báo ở top-level dùng chung một namespace. Nếu
tên của `VarDecl` hoặc `ConstDecl` đã xuất hiện trước đó trong cùng chương
trình, phải ném `RedeclaredDeclaration(ctx.name)` cho khai báo thứ hai. Cả
trùng variable-variable, constant-constant và variable-constant đều là lỗi.

Các node `IntType`, `FloatType` và `IntLit` không tạo tên mới; visitor của
chúng chỉ cần giữ nguyên môi trường. Không đổi tên class, method, tham số,
AST hoặc exception. Sinh viên chỉ sửa các thân method trong `solution.py`.

## Expected Output

| Test input | Expected |
| --- | --- |
| `Program([VarDecl("a",IntType()), ConstDecl("b",IntLit(3)), VarDecl("c",FloatType())])` | `['a', 'b', 'c']` |
| `Program([VarDecl("a",IntType()), ConstDecl("b",IntLit(3)), VarDecl("a",FloatType())])` | `RedeclaredDeclaration: a` |
| `Program([VarDecl("b",IntType()), ConstDecl("b",IntLit(3)), VarDecl("a",FloatType())])` | `RedeclaredDeclaration: b` |
| `Program([VarDecl("a",IntType()), ConstDecl("c",IntLit(3)), VarDecl("c",FloatType())])` | `RedeclaredDeclaration: c` |

## Run

Từ repository root, trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe NAME\exercise_01_redeclared_declaration\main.py
.\.venv\Scripts\python.exe NAME\exercise_01_redeclared_declaration\main.py --answer
.\.venv\Scripts\python.exe NAME\exercise_01_redeclared_declaration\main.py --demo-failure
```

Trên Linux/macOS:

```bash
.venv/bin/python NAME/exercise_01_redeclared_declaration/main.py
.venv/bin/python NAME/exercise_01_redeclared_declaration/main.py --answer
.venv/bin/python NAME/exercise_01_redeclared_declaration/main.py --demo-failure
```

Không có `--answer` là skeleton sinh viên. Runner tiếp tục chạy các test sau
khi một test bị exception và in `Reason` cho từng lỗi.
