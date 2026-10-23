# Abstract 5 - visitFor

## Đề bài

Hoàn thành `visitFor(self, ctx, o)` cho `For(idx, ini, end, upd, stmt)`.
Sinh code khởi tạo chỉ số, kiểm tra cận, thân vòng lặp, nhãn continue và cập
nhật chỉ số. Gọi `enterLoop()`/`exitLoop()` để `break` và `continue` hoạt
động trong vòng lặp. Theo test của đề, cận `end` được bao gồm.

## Expected Output

| Input | Expected |
| --- | --- |
| `for (x=0; x<=10; x+=2) putInt(x)` | `b'0246810'` |

## Run

Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe ABSTRACT\exercise_05_visit_for\main.py
.\.venv\Scripts\python.exe ABSTRACT\exercise_05_visit_for\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python ABSTRACT/exercise_05_visit_for/main.py
.venv/bin/python ABSTRACT/exercise_05_visit_for/main.py --answer
```
