# NAME Exercise 4 - UndeclaredIdentifier

## Đề bài

AST của bài gồm:

```python
class Program:       # decl: List[Decl]
class VarDecl(Decl): # name: str, typ: Type
class ConstDecl(Decl): # name: str, val: Lit
class FuncDecl(Decl):
    # name: str, param: List[VarDecl],
    # body: Tuple(List[Decl], List[Expr])
class IntLit(Lit):   # val: int
class Id(Expr):      # name: str
```

Exception:

```python
class RedeclaredVariable(Exception):  # name: str
class RedeclaredConstant(Exception):  # name: str
class RedeclaredFunction(Exception):  # name: str
class UndeclaredIdentifier(Exception): # name: str
```

Hãy hoàn thành `StaticCheck` để vừa kiểm tra redeclaration vừa kiểm tra
identifier usage. Program tạo scope ngoài cùng. Mỗi `FuncDecl` phải được thêm
vào scope hiện tại, sau đó tạo scope mới chứa parameters và declarations trong
body. Khi duyệt expression trong function, lookup theo thứ tự scope trong ra
ngoài: local body/parameter trước, sau đó enclosing function, cuối cùng là
global scope. Identifier có trong bất kỳ scope đang hoạt động là hợp lệ.

Nếu declaration trùng trong current scope, ném exception tương ứng với loại
declaration thứ hai. Không được coi shadowing ở scope con là redeclaration.
`IntLit` không cần lookup. `Id` không tìm thấy ở mọi scope phải ném
`UndeclaredIdentifier(ctx.name)`. Duyệt declaration và expression theo đúng
thứ tự xuất hiện trong body để lỗi đầu tiên giống đề PDF. Không sửa tên class,
method, tham số hoặc exception.

## Expected Output

| Test input | Expected |
| --- | --- |
| function dùng `z` chưa khai báo | `UndeclaredIdentifier: z` |
| `Program([VarDecl("a"), ConstDecl("b"), FuncDecl("c",..., [Id("d")])])` | `UndeclaredIdentifier: d` |
| function dùng `q` chưa khai báo | `UndeclaredIdentifier: q` |
| function dùng local, parameter, nested function và global hợp lệ | `None` |

## Run

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe NAME\exercise_04_undeclared_identifier\main.py
.\.venv\Scripts\python.exe NAME\exercise_04_undeclared_identifier\main.py --answer
```

Linux/macOS:

```bash
.venv/bin/python NAME/exercise_04_undeclared_identifier/main.py
.venv/bin/python NAME/exercise_04_undeclared_identifier/main.py --answer
```

Mỗi runner chỉ chạy test của exercise này. Dùng `--answer` để xem kết quả
reference; bỏ tùy chọn này để sinh viên implement skeleton.
