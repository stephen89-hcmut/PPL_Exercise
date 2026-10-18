# NAME Exercise 2 - Declaration-specific duplicate errors

## Đề bài

Dùng cùng AST với Exercise 1 nhưng phân loại lỗi:

```python
class RedeclaredVariable(Exception): # name: str
class RedeclaredConstant(Exception): # name: str
```

`Program.decl` là một scope. Khi `VarDecl(name, typ)` trùng tên với bất kỳ
khai báo trước đó trong scope, ném `RedeclaredVariable(name)`, vì khai báo thứ
hai là variable. Khi `ConstDecl(name, val)` trùng tên, ném
`RedeclaredConstant(name)`, vì khai báo thứ hai là constant. Vì vậy lỗi được
chọn theo loại của declaration thứ hai, không theo loại declaration đầu tiên.

Khai báo không trùng phải được ghi vào môi trường để các khai báo sau nhìn
thấy. Các visitor cho type và literal không được thêm tên. Không sửa public
API hoặc đổi cấu trúc AST.

## Expected Output

| Test input | Expected |
| --- | --- |
| `VarDecl("a"), ConstDecl("b",IntLit(3)), VarDecl("a")` | `RedeclaredVariable: a` |
| `VarDecl("b"), ConstDecl("b",IntLit(3)), VarDecl("a")` | `RedeclaredConstant: b` |
| `ConstDecl("c",IntLit(3)), VarDecl("c")` | `RedeclaredVariable: c` |
| `VarDecl("a"), ConstDecl("b",IntLit(3)), VarDecl("c")` | `None` |

## Run

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe NAME\exercise_02_redeclared_kind\main.py
.\.venv\Scripts\python.exe NAME\exercise_02_redeclared_kind\main.py --answer
```

Linux/macOS:

```bash
.venv/bin/python NAME/exercise_02_redeclared_kind/main.py
.venv/bin/python NAME/exercise_02_redeclared_kind/main.py --answer
```

`--answer` chạy reference implementation; bỏ tùy chọn này để chạy skeleton
trong `solution.py`.
