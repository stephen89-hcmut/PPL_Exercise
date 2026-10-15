# Bài 4 - Functional Programming: flatten

## Đề bài

Viết ba hàm flatten danh sách các danh sách thành một danh sách phẳng:

``python
def flatten_lst_comp(lst): ...
def flatten_recursive(lst): ...
def flatten_higher_order(lst): ...
``

Ba hàm lần lượt dùng list comprehension, đệ quy và higher-order function. Giữ nguyên tên hàm, tham số và trả về danh sách mới.

## Expected Output

| Test | Expected |
| --- | --- |
| `flatten_lst_comp([[1, 2, 3], ['a', 'b', 'c']])` | `[1, 2, 3, 'a', 'b', 'c']` |
| `flatten_lst_comp([])` | `[]` |
| `flatten_lst_comp([[1.1], [2.1, 3.1]])` | `[1.1, 2.1, 3.1]` |

Runner áp dụng cùng expected values cho `flatten_recursive` và `flatten_higher_order`.

## Run

Từ thư mục repository root, trước tiên chạy `.\.venv\Scripts\python.exe INCLASS\setup.py` để generate parser. Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe INCLASS\setup.py
.\.venv\Scripts\python.exe INCLASS\functional_04_flatten\main.py
.\.venv\Scripts\python.exe INCLASS\functional_04_flatten\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python INCLASS/setup.py
.venv/bin/python INCLASS/functional_04_flatten/main.py
.venv/bin/python INCLASS/functional_04_flatten/main.py --answer
```

Lệnh đầu chạy skeleton sinh viên; `--answer` chạy lời giải tham chiếu.