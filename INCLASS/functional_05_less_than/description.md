# Bài 5 - Functional Programming: lessThan

## Đề bài

Viết ba hàm nhận `(n, lst)` và trả về các phần tử nhỏ hơn `n`, giữ nguyên thứ tự:

``python
def lessThan_lst_comp(n, lst): ...
def lessThan_recursive(n, lst): ...
def lessThan_higher_order(n, lst): ...
``

Ba cách cài đặt lần lượt dùng list comprehension, đệ quy và higher-order function. Điều kiện là `<`, không phải `<=`; không sửa public API trong `solution.py`.

## Expected Output

| Test | Expected |
| --- | --- |
| `lessThan_lst_comp(50, [1, 55, 6, 2])` | `[1, 6, 2]` |
| `lessThan_lst_comp(1, [1, 0, -2])` | `[0, -2]` |
| `lessThan_lst_comp(0, [])` | `[]` |

Runner áp dụng cùng expected values cho `lessThan_recursive` và `lessThan_higher_order`.

## Run

Từ thư mục repository root, trước tiên chạy `.\.venv\Scripts\python.exe INCLASS\setup.py` để generate parser. Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe INCLASS\setup.py
.\.venv\Scripts\python.exe INCLASS\functional_05_less_than\main.py
.\.venv\Scripts\python.exe INCLASS\functional_05_less_than\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python INCLASS/setup.py
.venv/bin/python INCLASS/functional_05_less_than/main.py
.venv/bin/python INCLASS/functional_05_less_than/main.py --answer
```

Lệnh đầu chạy skeleton sinh viên; `--answer` chạy lời giải tham chiếu.