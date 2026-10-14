# OOP 3 - Visitor pattern

## Đề bài

Thay vì thêm method mới vào các lớp biểu thức cho mỗi tác vụ, hãy dùng Visitor pattern. Các lớp `Exp`, `BinExp`, `UnExp`, `IntLit` và `FloatLit` phải cung cấp cơ chế:

```python
x.accept(Eval())
x.accept(PrintPrefix())
x.accept(PrintPostfix())
```

Trong đó:

- `Eval` tính giá trị biểu thức.
- `PrintPrefix` trả về biểu diễn prefix.
- `PrintPostfix` trả về biểu diễn postfix.

Hãy hoàn thành các method `accept` và các method `visitBinExp`, `visitUnExp`, `visitIntLit`, `visitFloatLit` trong ba visitor ở `solution.py`. Không được dùng `type()` hoặc `isinstance()`; dispatch phải thực hiện qua double dispatch của Visitor pattern. Không thay đổi constructor và tên public API.

## Expected Output

| Test | Expected |
| --- | --- |
| `x1.accept(Eval())` với `IntLit(1)` | `1` |
| `x1` prefix/postfix | `1 \| 1` |
| `x2.accept(Eval())` với `FloatLit(2.0)` | `2.0` |
| `x2` prefix/postfix | `2.0 \| 2.0` |
| `x3` visitors với `1 + 1` | `2 \| + 1 1 \| 1 1 +` |
| `x4` visitors với `-1` | `-1 \| -. 1 \| 1 -.` |
| `x5` visitors với `-1 + 4 * 2.0` | `7.0 \| + -. 1 * 4 2.0 \| 1 -. 4 2.0 * +` |

## Run

```bash
.venv/bin/python OOP/oop_03_visitor/main.py
.venv/bin/python OOP/oop_03_visitor/main.py --answer
```

Lệnh đầu chạy skeleton sinh viên; `--answer` chạy reference answer. Runner kiểm tra đồng thời evaluation, prefix và postfix.
