# Bài 7: Biểu thức - Question 7 (Grammar lặp gộp toán tử)

## Đề bài

Thay grammar biểu thức bằng dạng vòng lặp:

```antlr
grammar X;
exp: term ((ADDOP|SUBOP) term)*;
term: (factor (MULOP|DIVOP))* factor;
factor: ID | INTLIT | '(' exp ')';
```

Skeleton cần implement:

```python
class ASTGeneration(XVisitor):
	def visitExp(self, ctx: XParser.ExpContext):
		return None

	def visitTerm(self, ctx: XParser.TermContext):
		return None
```

Hãy tự tạo AST left-associative khi duyệt các operator trong loop. Có thể dùng
visitor mặc định cho `factor` hoặc bổ sung method cần thiết để xử lý `ID`,
`INTLIT` và biểu thức trong ngoặc.

## Expected Output

| Input | Expected Output | Got khi kết hợp phải sai |
|---|---|---|
| `1 - 2 - 3` | `BinOp(-, BinOp(-, Num(1), Num(2)), Num(3))` | `BinOp(-, Num(1), BinOp(-, Num(2), Num(3)))` |
| `a * b / c` | `BinOp(/, BinOp(*, Var(a), Var(b)), Var(c))` | Cây phải được xây từ trái sang phải |

## Run

Chạy skeleton sinh viên:

```bash
.venv/bin/python INCLASS/ast_07_expression_loop/main.py
```

Chạy đáp án tham khảo:

```bash
.venv/bin/python INCLASS/ast_07_expression_loop/main.py --answer
```
