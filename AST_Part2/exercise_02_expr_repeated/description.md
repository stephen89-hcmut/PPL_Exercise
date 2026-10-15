# Expression AST Generation - Repeated Grammar

## Đề bài

Cho grammar MP:

``text
program: exp EOF;
exp: (term ASSIGN)* term;
term: factor COMPARE factor | factor;
factor: operand (ANDOR operand)*;
operand: ID | INTLIT | BOOLIT | '(' exp ')';
``

Hãy hoàn thành các phương thức của `ASTGeneration` trong `solution.py` để sinh AST. Dùng `Binary`, `Id`, `IntLiteral` và `BooleanLiteral` đúng theo grammar; các phép gán phải cho AST kết hợp phải, còn chuỗi `ANDOR` kết hợp trái.

## Expected Output

| Input                     | Expected                                                                            |
| ------------------------- | ----------------------------------------------------------------------------------- |
| `a := b := 4`             | `Binary(:=,Id(a),Binary(:=,Id(b),IntLiteral(4)))`                                   |
| `a += b -= a and (b > 3)` | `Binary(+=,Id(a),Binary(-=,Id(b),Binary(and,Id(a),Binary(>,Id(b),IntLiteral(3)))))` |
| `a or b and True`         | `Binary(and,Binary(or,Id(a),Id(b)),BooleanLiteral(True))`                           |

## Run

Từ thư mục repository root, trước tiên chạy `.\.venv\Scripts\python.exe AST_Part2\setup.py` để generate parser. Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe AST_Part2\setup.py
.\.venv\Scripts\python.exe AST_Part2\exercise_02_expr_repeated\main.py
.\.venv\Scripts\python.exe AST_Part2\exercise_02_expr_repeated\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python AST_Part2/setup.py
.venv/bin/python AST_Part2/exercise_02_expr_repeated/main.py
.venv/bin/python AST_Part2/exercise_02_expr_repeated/main.py --answer
```

Lệnh đầu chạy skeleton sinh viên; `--answer` chạy lời giải tham chiếu.