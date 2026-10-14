# Bài 6 - Functional Programming: compose

## Đề bài

Viết hai hàm nhận một số function và trả về function composition:

```python
def compose_recursive(*args): ...
def compose_higher_order(*args): ...
```

Quy ước của bài là các function được áp dụng từ trái sang phải trong danh sách đối số. Vì vậy `compose(double, increase)(3)` nghĩa là `increase(double(3))`. Có thể dùng đệ quy cho hàm thứ nhất và higher-order function hoặc `reduce` cho hàm thứ hai. Giữ nguyên chữ ký `*args`.

## Expected Output

| Test | Expected |
| --- | --- |
| `compose_recursive(double, increase)(3)` | `7` |
| `compose_recursive(square, increase, double)(2)` | `10` |

Runner áp dụng cùng expected values cho `compose_higher_order`.

## Run

```bash
.venv/bin/python INCLASS/functional_06_compose/main.py
.venv/bin/python INCLASS/functional_06_compose/main.py --answer
```

Không có `--answer` chạy skeleton sinh viên; `--answer` chạy reference answer.
