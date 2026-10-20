# Program-level type inference

## Đề bài

Hoàn thành `StaticCheck` cho `Program(decl, stmts)`, `VarDecl(name)`,
`Assign(lhs, rhs)`, `BinOp`, `UnOp`, literal và `Id`.

Kiểu của biến được suy luận từ lần sử dụng đầu tiên. Các quy tắc toán tử:

- `+`, `-`, `*`, `/` nhận và trả `int`.
- `+.`, `-.`, `*.`, `/.` nhận và trả `float`.
- `>`, `=` nhận `int`, trả `bool`; `>.`, `=.` nhận `float`, trả `bool`.
- `!`, `&&`, `||`, `>b`, `=b` nhận `bool`, trả `bool`.
- `i2f` nhận `int`, trả `float`; `floor` nhận `float`, trả `int`.

Assignment yêu cầu hai vế cùng kiểu, nếu không ném
`TypeMismatchInStatement`. ID chưa khai báo ném `UndeclaredIdentifier`.
Nếu hai phía đều chưa đủ thông tin để suy luận, ném
`TypeCannotBeInferred` với assignment. Biểu thức sai kiểu ném
`TypeMismatchInExpression`.

## Expected Output

| Input | Expected |
| --- | --- |
| `Program([VarDecl("x")],[Assign(Id("x"),IntLit(3))])` | `None` |
| Gán `x` bằng `BinOp("+",IntLit(3),IntLit(4))` | `None` |
| `Assign(Id("x"),Id("y"))` khi cả hai chưa biết | `TypeCannotBeInferred: Assign(Id("x"),Id("y"))` |
| `BinOp("+",IntLit(3),BoolLit(True))` | `TypeMismatchInExpression` |
| Gán `x:int` bằng `FloatLit(3.0)` | `TypeMismatchInStatement` |
| Dùng `Id("t")` chưa khai báo | `UndeclaredIdentifier: t` |
| Dùng `UnOp("i2f",Id("x"))` với `x:int` | `None` |

## Run

Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe Type_Part1\exercise_03_program_type_inference\main.py
.\.venv\Scripts\python.exe Type_Part1\exercise_03_program_type_inference\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python Type_Part1/exercise_03_program_type_inference/main.py
.venv/bin/python Type_Part1/exercise_03_program_type_inference/main.py --answer
```

Bỏ `--answer` để chạy skeleton sinh viên.
