# AST 4 - Program

## Đề bài

Cho grammar:

``antlr
program: vardecl+ EOF;
vardecl: ids COLON typ;
ids: ID (CM ID)*;
typ: INTTYPE | FLOATTYPE;
``

AST dùng `Program(decl)`, `VarDecl(name, typ)`, `IntType` và `FloatType`. Hãy hoàn thành `visitProgram` trong `ASTGeneration` để duyệt mọi declaration và flatten các danh sách `VarDecl` thành một danh sách duy nhất trong `Program`. Không được tạo list of lists. Các method/API và skeleton trong `solution.py` phải được giữ nguyên.

## Expected Output

| Input | Expected |
| --- | --- |
| `x,y:int z:float` | `Program([VarDecl(x, IntType), VarDecl(y, IntType), VarDecl(z, FloatType)])` |

## Run

Từ thư mục PPL_Exercise, trước tiên chạy `python3 INCLASS/setup.py` để generate parser. Trên Windows PowerShell:

```powershell
python3 INCLASS/setup.py
python3 INCLASS/ast_04_program/main.py
python3 INCLASS/ast_04_program/main.py --answer
```

Trên Linux/macOS:

```bash
python3 INCLASS/setup.py
python3 INCLASS/ast_04_program/main.py
python3 INCLASS/ast_04_program/main.py --answer
```

Lệnh đầu chạy skeleton sinh viên; `--answer` chạy lời giải tham chiếu.