# Type checking expressions

## Đề bài

Hoàn thành `StaticCheck` trong `solution.py` bằng Visitor pattern. AST gồm:

```python
class BinOp(Exp):  # op, e1, e2; + - * / && || > < == !=
class UnOp(Exp):   # op, e; - !
class IntLit(Exp): # val: int
class FloatLit(Exp): # val: float
class BoolLit(Exp): # val: bool
```

Quy tắc kiểu:

- `+`, `-`, `*` nhận `int` hoặc `float`, trả về `float` nếu có toán hạng
  `float`, ngược lại trả `int`.
- `/` nhận `int` hoặc `float` và luôn trả `float`.
- `!`, `&&`, `||` chỉ nhận `bool` và trả `bool`.
- `>`, `<`, `==`, `!=` nhận hai toán hạng cùng kiểu và trả `bool`.
- Unary `-` nhận `int` hoặc `float` và giữ nguyên kiểu.

Khi vi phạm, ném `TypeMismatchInExpression` với sub-expression trong cùng
nhất chứa lỗi. Không đổi tên class hoặc method trong skeleton.

## Expected Output

| Input | Expected |
| --- | --- |
| `BinOp("+",IntLit(3),IntLit(2))` | `int` |
| `BinOp("*",IntLit(3),FloatLit(3.4))` | `float` |
| `BinOp("/",IntLit(8),IntLit(2))` | `float` |
| `BinOp("&&",BoolLit(True),BoolLit(False))` | `bool` |
| `BinOp("==",IntLit(3),IntLit(3))` | `bool` |
| `BinOp("+",IntLit(3),BoolLit(True))` | `Type Mismatch In Expression: BinOp("+",IntLit(3),BoolLit(True))` |
| `BinOp(">",IntLit(3),FloatLit(2.1))` | `Type Mismatch In Expression: BinOp(">",IntLit(3),FloatLit(2.1))` |
| `UnOp("-",BoolLit(True))` | `Type Mismatch In Expression: UnOp("-",BoolLit(True))` |

## Run

Từ thư mục repository root.

Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe Type_Part1\exercise_01_expression_types\main.py
.\.venv\Scripts\python.exe Type_Part1\exercise_01_expression_types\main.py --answer
.\.venv\Scripts\python.exe Type_Part1\exercise_01_expression_types\main.py --demo-failure
```

Trên Linux/macOS:

```bash
.venv/bin/python Type_Part1/exercise_01_expression_types/main.py
.venv/bin/python Type_Part1/exercise_01_expression_types/main.py --answer
.venv/bin/python Type_Part1/exercise_01_expression_types/main.py --demo-failure
```

Bỏ `--answer` để chạy skeleton sinh viên.
