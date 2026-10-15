# OOP 1 - Arithmetic expression eval

## Đề bài

Xây dựng các lớp biểu diễn biểu thức số học:

``python
class Exp(ABC): ...
class BinExp(Exp):       # left, op, right; op in +, -, *, /
class UnExp(Exp):        # op in +, -; operand
class IntLit(Exp):       # val: int
class FloatLit(Exp):     # val: float
``

Hãy hoàn thành các method `eval()` trong `solution.py` để mỗi object trả về giá trị của biểu thức. Phép toán nhị phân phải đánh giá đệ quy hai operand; unary `+` giữ nguyên giá trị và unary `-` đổi dấu. Phép chia dùng semantics của Python. Giữ nguyên tên lớp, thuộc tính và constructor.

## Expected Output

| Test                                                     | Expected |
| -------------------------------------------------------- | -------- |
| `x1.eval()` với `IntLit(11)`                        | `11`   |
| `x2.eval()` với `FloatLit(2.0)`                     | `2.0`  |
| `x3.eval()` với `BinExp(IntLit(1), "+", IntLit(1))` | `2`    |
| `x4.eval()` với `UnExp("-", IntLit(1))`             | `-1`   |
| `x5.eval()` với `-1 + 4 * 2.0`                      | `7.0`  |
| `x6.eval()` với `-(4.0 * 2)`                        | `-8.0` |

## Run

Từ thư mục repository root: Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe OOP\oop_01_eval\main.py
.\.venv\Scripts\python.exe OOP\oop_01_eval\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python OOP/oop_01_eval/main.py
.venv/bin/python OOP/oop_01_eval/main.py --answer
```

Lệnh đầu chạy skeleton sinh viên; `--answer` chạy lời giải tham chiếu.