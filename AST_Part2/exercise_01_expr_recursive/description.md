# Expression AST Generation - Recursive Grammar

## Đề bài

Cho grammar MP:

```text
program: exp EOF;
exp: term ASSIGN exp | term;
term: factor COMPARE factor | factor;
factor: factor ANDOR operand | operand;
operand: ID | INTLIT | BOOLIT | '(' exp ')';
```

Hãy hoàn thành các phương thức của `ASTGeneration` trong `solution.py` để sinh AST. Các node cần dùng là `Binary(op, left, right)`, `Id(value)`, `IntLiteral(value)` và `BooleanLiteral(value)`. Giữ nguyên tên lớp, visitor base class và chữ ký phương thức; không đặt lời giải vào skeleton.

## Expected Output

| Input                       | Expected                                                                              |
| --------------------------- | ------------------------------------------------------------------------------------- |
| `a := b := 4`             | `Binary(:=,Id(a),Binary(:=,Id(b),IntLiteral(4)))`                                   |
| `a += b -= a and (b > 3)` | `Binary(+=,Id(a),Binary(-=,Id(b),Binary(and,Id(a),Binary(>,Id(b),IntLiteral(3)))))` |
| `a or b and True`         | `Binary(and,Binary(or,Id(a),Id(b)),BooleanLiteral(True))`                           |

## Run

```bash
python AST_Part2/setup.py
python AST_Part2/exercise_01_expr_recursive/main.py
python AST_Part2/exercise_01_expr_recursive/main.py --answer
python AST_Part2/exercise_01_expr_recursive/main.py --demo-failure
```

Bỏ `--answer` để chạy skeleton sinh viên.
