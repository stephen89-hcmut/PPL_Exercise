# AST 3 - VarDecl

## Đề bài

Cho grammar:

``antlr vardecl: ids COLON typ; ids: ID (CM ID)*; typ: INTTYPE | FLOATTYPE; ``

Các node AST gồm `VarDecl(name, typ)`, `IntType` và `FloatType`. Hãy hoàn thành `visitVardecl`, `visitIds` và `visitTyp` trong `ASTGeneration`. Một declaration có nhiều ID phải sinh ra một danh sách `VarDecl`, mỗi ID dùng cùng kiểu dữ liệu. Giữ nguyên visitor base class, method names và skeleton trong `solution.py`.

## Expected Output

| Input       | Expected                                       |
| ----------- | ---------------------------------------------- |
| `x,y:int` | `[VarDecl(x, IntType), VarDecl(y, IntType)]` |
| `z:float` | `[VarDecl(z, FloatType)]`                    |

## Run

Từ thư mục repository root, trước tiên chạy `.\.venv\Scripts\python.exe INCLASS\setup.py` để generate parser. Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe INCLASS\setup.py
.\.venv\Scripts\python.exe INCLASS\ast_03_vardecl\main.py
.\.venv\Scripts\python.exe INCLASS\ast_03_vardecl\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python INCLASS/setup.py
.venv/bin/python INCLASS/ast_03_vardecl/main.py
.venv/bin/python INCLASS/ast_03_vardecl/main.py --answer
```

Lệnh đầu chạy skeleton sinh viên; `--answer` chạy lời giải tham chiếu.
