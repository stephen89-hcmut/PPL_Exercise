# Bài 3 - Functional Programming: double

## Đề bài

Viết ba hàm trong `solution.py`, mỗi hàm trả về danh sách mới trong đó mỗi phần tử bằng hai lần phần tử tương ứng của `lst`:

```python
def double_lst_comp(lst): ...
def double_recursive(lst): ...
def double_higher_order(lst): ...
```

Ba cách cài đặt lần lượt phải dùng list comprehension, đệ quy và higher-order function. Không sửa tên hàm hoặc tham số.

## Expected Output

| Test | Expected |
| --- | --- |
| `double_lst_comp([5, 7, 12, -4])` | `[10, 14, 24, -8]` |
| `double_lst_comp([])` | `[]` |
| `double_lst_comp([0, -3])` | `[0, -6]` |

Runner áp dụng cùng expected values cho `double_recursive` và `double_higher_order`.

## Run

```bash
.venv/bin/python INCLASS/functional_03_double/main.py
.venv/bin/python INCLASS/functional_03_double/main.py --answer
```

Lệnh đầu chạy các skeleton trong `solution.py`; `--answer` chạy ba implementation tham chiếu.
