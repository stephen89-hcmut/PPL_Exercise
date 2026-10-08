# Bài 5: Biểu thức - Question 5 (Grammar đệ quy)

## Đề bài

Cho grammar biểu thức trong ANTLR4:

```antlr
grammar X;
exp: exp ADDOP term | exp SUBOP term | term;
term: factor MULOP term | factor DIVOP term | factor;
factor: ID | INTLIT | '(' exp ')';
```

Các lớp AST:

```python
class Expr(ABC): pass
class Num(Expr):  # val: int
class Var(Expr):  # name: str
class BinOp(Expr):  # op: str, left: Expr, right: Expr
class UnOp(Expr):  # op: str, arg: Expr
```

Hãy implement các method `visitExp`, `visitTerm`, `visitFactor` của class
`ASTGeneration`, là subclass của visitor được ANTLR4 generate, để sinh AST từ
biểu thức đầu vào. Cần xử lý số nguyên, biến và biểu thức trong ngoặc.

## Expected Output

| Input | Expected Output |
|---|---|
| `a + 3` | `BinOp(+, Var(a), Num(3))` |
| `a * (b + 2)` | `BinOp(*, Var(a), BinOp(+, Var(b), Num(2)))` |

## Run

Chạy skeleton sinh viên:

```bash
.venv/bin/python INCLASS/ast_05_expression_recursive/main.py
```

Chạy đáp án tham khảo:

```bash
.venv/bin/python INCLASS/ast_05_expression_recursive/main.py --answer
```
