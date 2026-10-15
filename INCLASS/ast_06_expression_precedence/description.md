# Bài 6: Biểu thức - Phân tích cây đệ quy

## Đề bài

Sử dụng grammar đệ quy và cấu trúc AST của Bài 5. Implement các method của
`ASTGeneration` để tạo đúng AST lồng nhau cho biểu thức toán học.

AST phải phản ánh đúng precedence và associativity: phép nhân/chia được xử lý
trước phép cộng/trừ, còn các phép cùng mức phải giữ cấu trúc mà grammar quy định.
Skeleton sử dụng lại Bài 5:

``python
class ASTGeneration(XVisitor):
	def visitExp(self, ctx: XParser.ExpContext):
		return None

	def visitTerm(self, ctx: XParser.TermContext):
		return None

	def visitFactor(self, ctx: XParser.FactorContext):
		return None
``

## Expected Output

| Input | Expected Output | Got khi xử lý sai precedence |
|---|---|---|
| `a + 3 * b - 2` | `BinOp(-, BinOp(+, Var(a), BinOp(*, Num(3), Var(b))), Num(2))` | `BinOp(+, Var(a), BinOp(-, BinOp(*, Num(3), Var(b)), Num(2)))` |

## Run

Từ thư mục repository root, trước tiên chạy `.\.venv\Scripts\python.exe INCLASS\setup.py` để generate parser. Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe INCLASS\setup.py
.\.venv\Scripts\python.exe INCLASS\ast_06_expression_precedence\main.py
.\.venv\Scripts\python.exe INCLASS\ast_06_expression_precedence\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python INCLASS/setup.py
.venv/bin/python INCLASS/ast_06_expression_precedence/main.py
.venv/bin/python INCLASS/ast_06_expression_precedence/main.py --answer
```

Lệnh đầu chạy skeleton sinh viên; `--answer` chạy lời giải tham chiếu.