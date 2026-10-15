# AST 2 - ids voi grammar vong lap

## Đề bài

Cho grammar:

``antlr ids: ID (CM ID)*; ``

Hãy hoàn thành `visitIds` trong `ASTGeneration` để trả về danh sách lexeme `ID` theo đúng thứ tự. Tất cả ID nằm trong cùng một `IdsContext`, vì vậy không dùng lời gọi đệ quy `ctx.ids()` như ở Bài 1. Skeleton phải giữ nguyên API và chỉ chứa phần sinh viên cần cài đặt.

## Expected Output

| Input     | Expected            |
| --------- | ------------------- |
| `a,b,c` | `['a', 'b', 'c']` |
| `x,y`   | `['x', 'y']`      |

## Run

Từ thư mục repository root, trước tiên chạy `.\.venv\Scripts\python.exe INCLASS\setup.py` để generate parser. Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe INCLASS\setup.py
.\.venv\Scripts\python.exe INCLASS\ast_02_ids_loop\main.py
.\.venv\Scripts\python.exe INCLASS\ast_02_ids_loop\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python INCLASS/setup.py
.venv/bin/python INCLASS/ast_02_ids_loop/main.py
.venv/bin/python INCLASS/ast_02_ids_loop/main.py --answer
```

Lệnh đầu chạy skeleton sinh viên; `--answer` chạy lời giải tham chiếu.
