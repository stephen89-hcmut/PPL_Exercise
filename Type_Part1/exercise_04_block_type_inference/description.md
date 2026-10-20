# Block-scoped type inference

## Đề bài

Hoàn thành `StaticCheck` để xử lý `Program(decl, stmts)`, `Block(decl,
stmts)`, `Assign(lhs, rhs)`, `BinOp`, `UnOp`, literals và `Id`.

Khai báo `VarDecl` ban đầu chưa biết kiểu. Quy tắc:

- `+`, `-`, `*`, `/` dùng `int`; `+.`, `-.`, `*.`, `/.` dùng `float`.
- `>`, `=` dùng `int`; `>.`, `=.` dùng `float`.
- `!`, `&&`, `||`, `>b`, `=b` dùng `bool`.
- `i2f` nhận `int`, trả `float`; `floor` nhận `float`, trả `int`.
- Gán hai vế phải cùng kiểu; nếu một `Id` chưa biết kiểu thì suy luận từ vế
  còn lại. Nếu cả hai đều chưa biết, ném `TypeCannotBeInferred`.
- Scope của `Block` che scope ngoài nhưng không được phép khai báo trùng trong
  cùng scope. Lỗi dùng `Redeclared(declaration)`.
- ID không khai báo ném `UndeclaredIdentifier(name)`. Lỗi biểu thức dùng
  `TypeMismatchInExpression(expression)` và lỗi câu lệnh dùng
  `TypeMismatchInStatement(statement)`.

## Expected Output

Các test chính gồm suy luận `int`, scope block, redeclaration, ID chưa khai
báo, biểu thức sai kiểu, phép gán sai kiểu và trường hợp không thể suy luận.

| Input | Expected |
| --- | --- |
| `Program([VarDecl("x")],[Assign(Id("x"),IntLit(3))])` | `None` |
| Block có `VarDecl("y")` và gán `x` qua `y` | `None` |
| Block có hai `VarDecl("y")` | `Redeclared: VarDecl("y")` |
| `Assign(Id("x"),Id("y"))` khi cả hai chưa biết kiểu | `TypeCannotBeInferred: Assign(Id("x"),Id("y"))` |
| `Assign(Id("x"),Id("z"))` khi `z` chưa khai báo | `UndeclaredIdentifier: z` |
| `BinOp("-",Id("t"),Id("x"))` với `t:float`, `x:int` | `TypeMismatchInExpression` |

## Run

Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe Type_Part1\exercise_03_block_type_inference\main.py
.\.venv\Scripts\python.exe Type_Part1\exercise_03_block_type_inference\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python Type_Part1/exercise_03_block_type_inference/main.py
.venv/bin/python Type_Part1/exercise_03_block_type_inference/main.py --answer
```

Bỏ `--answer` để chạy skeleton sinh viên.
