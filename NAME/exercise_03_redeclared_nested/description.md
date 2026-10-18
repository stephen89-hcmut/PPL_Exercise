# NAME Exercise 3 - Nested scope redeclaration

## Đề bài

AST mở rộng:

```python
class FuncDecl(Decl):
    # name: str, param: List[VarDecl], body: List[Decl]
```

Có ba loại exception:

```python
class RedeclaredVariable(Exception):  # name: str
class RedeclaredConstant(Exception):  # name: str
class RedeclaredFunction(Exception):  # name: str
```

`Program.decl` là scope ngoài cùng. Tên function được kiểm tra trong scope
chứa function; nếu trùng bất kỳ declaration nào ở scope đó, declaration thứ
hai là `RedeclaredFunction`. Khi vào function, tạo scope mới cho parameters và
body. Parameters và body declarations cùng nằm trong scope function, nên
parameter trùng parameter, parameter trùng local, local trùng local đều lỗi.
Tuy nhiên declaration trong function có thể trùng tên declaration ở scope
ngoài mà không phải lỗi, vì scope bên trong được phép shadow scope bên ngoài.

Nếu declaration trong body là `VarDecl`, lỗi là `RedeclaredVariable`; nếu là
`ConstDecl`, lỗi là `RedeclaredConstant`; nếu là `FuncDecl`, lỗi là
`RedeclaredFunction`. Function lồng nhau cũng tạo scope riêng cho parameters
và body. Không cần kiểm tra expression ở bài này; mục tiêu là scope và
redeclaration.

## Expected Output

| Test input | Expected |
| --- | --- |
| global `VarDecl("a")` rồi `FuncDecl("a",[],[])` | `RedeclaredFunction: a` |
| local `ConstDecl("c")` rồi `VarDecl("c")` | `RedeclaredVariable: c` |
| parameters `m, b, m` | `RedeclaredVariable: m` |
| local `VarDecl("d")` rồi nested `FuncDecl("d")` | `RedeclaredFunction: d` |
| nested function parameter `x` rồi local `VarDecl("x")` | `RedeclaredVariable: x` |

## Run

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe NAME\exercise_03_redeclared_nested\main.py
.\.venv\Scripts\python.exe NAME\exercise_03_redeclared_nested\main.py --answer
```

Linux/macOS:

```bash
.venv/bin/python NAME/exercise_03_redeclared_nested/main.py
.venv/bin/python NAME/exercise_03_redeclared_nested/main.py --answer
```

Runner chỉ in test của Exercise 3. `--answer` dùng lời giải tham chiếu; không
có tùy chọn này thì các method TODO trong `solution.py` được chạy.
