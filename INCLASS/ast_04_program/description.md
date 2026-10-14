# AST 4 - Program

## Đề bài

Cho grammar:

```antlr
program: vardecl+ EOF;
vardecl: ids COLON typ;
ids: ID (CM ID)*;
typ: INTTYPE | FLOATTYPE;
```

AST dùng `Program(decl)`, `VarDecl(name, typ)`, `IntType` và `FloatType`. Hãy hoàn thành `visitProgram` trong `ASTGeneration` để duyệt mọi declaration và flatten các danh sách `VarDecl` thành một danh sách duy nhất trong `Program`. Không được tạo list of lists. Các method/API và skeleton trong `solution.py` phải được giữ nguyên.

## Expected Output

| Input | Expected |
| --- | --- |
| `x,y:int z:float` | `Program([VarDecl(x, IntType), VarDecl(y, IntType), VarDecl(z, FloatType)])` |

## Run

```bash
.venv/bin/python INCLASS/ast_04_program/main.py
.venv/bin/python INCLASS/ast_04_program/main.py --answer
```
Lệnh đầu chạy skeleton sinh viên; thêm `--answer` để chạy lời giải tham chiếu.
