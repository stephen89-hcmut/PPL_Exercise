# Abstract 4 - visitWhile

## Đề bài

Hoàn thành `visitWhile(self, ctx, o)` cho `While(expr, stmt)`. Gọi
`enterLoop()`/`exitLoop()`, tạo nhãn break và continue, phát sinh điều kiện,
nhảy ra khi điều kiện sai, chạy thân vòng lặp và quay lại nhãn continue. Các
`break` và `continue` bên trong vòng lặp phải dùng đúng nhãn của frame.

## Expected Output

| Input | Expected |
| --- | --- |
| `x=0; while (x<10) { putInt(x); x=x+1; }` | `b'0123456789'` |

## Run

Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe ABSTRACT\exercise_04_visit_while\main.py
.\.venv\Scripts\python.exe ABSTRACT\exercise_04_visit_while\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python ABSTRACT/exercise_04_visit_while/main.py
.venv/bin/python ABSTRACT/exercise_04_visit_while/main.py --answer
```
