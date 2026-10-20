# Function type inference

## Đề bài

Hoàn thành `StaticCheck` cho `Program(decl, stmts)`, trong đó declaration có
thể là `VarDecl(name)` hoặc `FuncDecl(name, param, local, stmts)`. Statement
gồm `Assign(lhs, rhs)` và `CallStmt(name, args)`; expression gồm literal và
`Id`.

Function là một scope block. Kiểu parameter được suy luận từ các phép gán
trong thân hàm hoặc từ cách sử dụng hợp lệ. Quy tắc:

- Assignment yêu cầu hai vế cùng kiểu, nếu không ném
  `TypeMismatchInStatement(assign)`.
- ID chưa khai báo ném `UndeclaredIdentifier(name)`.
- Nếu kiểu không thể suy luận ném `TypeCannotBeInferred(statement)`.
- Trùng tên trong một scope ném `Redeclared(declaration)`.
- Call phải tìm thấy function, đúng số argument và kiểu từng argument phải
  khớp parameter. Nếu không, ném `UndeclaredIdentifier(name)`,
  `TypeMismatchInStatement(call)` hoặc `TypeCannotBeInferred(call)` tương ứng.

## Expected Output

| Input | Expected |
| --- | --- |
| Call đúng kiểu và đúng số lượng | `None` |
| Argument khác kiểu parameter | `TypeMismatchInStatement: CallStmt("foo",[Id("x")])` |
| Gọi `foo2` chưa khai báo | `UndeclaredIdentifier: foo2` |
| Sai số lượng argument | `TypeMismatchInStatement: CallStmt("foo",[])` |
| Parameter chưa thể suy luận | `TypeCannotBeInferred: CallStmt("foo",[IntLit(3),Id("x")])` |
| Trùng function với variable `x` | `Redeclared: FuncDecl("x",[VarDecl("y")],[],[])` |

## Run

Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe Type_Part1\exercise_04_function_type_inference\main.py
.\.venv\Scripts\python.exe Type_Part1\exercise_04_function_type_inference\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python Type_Part1/exercise_04_function_type_inference/main.py
.venv/bin/python Type_Part1/exercise_04_function_type_inference/main.py --answer
```

Bỏ `--answer` để chạy skeleton sinh viên.
