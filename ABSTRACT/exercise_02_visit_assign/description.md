# Abstract 2 - visitAssign

## Đề bài

Hoàn thành `visitAssign(self, ctx, o)`. Tạo `Access` với `isLeft=False` khi
duyệt RHS và `Access` với `isLeft=True` khi duyệt LHS. Phải phát sinh RHS
trước LHS rồi dùng `emit.printout` để ghi phép gán. Hai vế có cùng kiểu.

## Expected Output

| Input | Expected |
| --- | --- |
| `x = 15; x = x + 5; putInt(x)` | `b'20'` |

## Run

Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe ABSTRACT\exercise_02_visit_assign\main.py
.\.venv\Scripts\python.exe ABSTRACT\exercise_02_visit_assign\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python ABSTRACT/exercise_02_visit_assign/main.py
.venv/bin/python ABSTRACT/exercise_02_visit_assign/main.py --answer
```
