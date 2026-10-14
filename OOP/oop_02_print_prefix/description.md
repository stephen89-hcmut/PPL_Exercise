# OOP 2 - Prefix and postfix

## Đề bài

Mở rộng các lớp `Exp`, `BinExp`, `UnExp`, `IntLit` và `FloatLit` để cài đặt:

```python
printPrefix() -> str
printPostfix() -> str
```

Biểu thức nhị phân in operator trước hoặc sau hai operand. Unary `+` và `-` phải được in thành `+.` và `-.` để phân biệt với operator nhị phân. Các token trong chuỗi được ngăn cách bằng một dấu cách; literal được chuyển thành chuỗi bằng giá trị của nó. Giữ nguyên constructors và các method trong skeleton.

## Expected Output

| Test | Expected |
| --- | --- |
| `IntLit(1).printPrefix()` | `1` |
| `FloatLit(2.0).printPrefix()` | `2.0` |
| `BinExp(IntLit(1), "+", IntLit(1)).printPrefix()` | `+ 1 1` |
| `UnExp("-", IntLit(1)).printPrefix()` | `-. 1` |
| `x5.printPrefix()` với `-1 + 4 * 2.0` | `+ -. 1 * 4 2.0` |
| `x5.printPostfix()` với `-1 + 4 * 2.0` | `1 -. 4 2.0 * +` |

## Run

```bash
.venv/bin/python OOP/oop_02_print_prefix/main.py
.venv/bin/python OOP/oop_02_print_prefix/main.py --answer
```

Không có `--answer` chạy skeleton sinh viên; `--answer` chạy lời giải tham chiếu. Runner bài này kiểm tra cả prefix và postfix.
