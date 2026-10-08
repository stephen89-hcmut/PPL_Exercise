# Bài 8: Biểu thức - Grammar lặp tách rule toán tử

## Đề bài

Cho grammar có các rule operator riêng:

```antlr
grammar X;
exp: term (addop term)*;
addop: ADDOP|SUBOP;
term: (factor mulop)* factor;
mulop: MULOP|DIVOP;
factor: ID | INTLIT | '(' exp ')';
```

Hãy implement các method của `ASTGeneration`:

```python
class ASTGeneration(XVisitor):
	def visitExp(self, ctx: XParser.ExpContext):
		return None

	def visitAddop(self, ctx: XParser.AddopContext):
		return None

	def visitTerm(self, ctx: XParser.TermContext):
		return None

	def visitMulop(self, ctx: XParser.MulopContext):
		return None
```

Khi duyệt loop, phải tạo AST left-associative và lấy operator thông qua
`visitAddop`/`visitMulop`.

## Expected Output

| Input | Expected Output |
|---|---|
| `a * b / c` | `BinOp(/, BinOp(*, Var(a), Var(b)), Var(c))` |
| `a + b - c` | `BinOp(-, BinOp(+, Var(a), Var(b)), Var(c))` |

## Run

Chạy skeleton sinh viên:

```bash
.venv/bin/python INCLASS/ast_08_expression_split/main.py
```

Chạy đáp án tham khảo:

```bash
.venv/bin/python INCLASS/ast_08_expression_split/main.py --answer
```
