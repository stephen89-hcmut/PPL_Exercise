# Abstract 1 - visitId

## Đề bài

Hoàn thành `visitId(self, ctx, o)` của visitor `CodeGeneration`. `ctx.name`
là tên định danh; `o` là `Access(frame, sym, isLeft)`. Duyệt `sym` từ môi
trường gần nhất ra ngoài. Với biến cục bộ dùng thao tác đọc/ghi theo
`Index`; với biến toàn cục dùng thao tác `GETSTATIC`/`PUTSTATIC` theo
`CName`. Method phải trả về cặp `(code, type)`. Skeleton giữ nguyên trong
`solution.py`, còn `answer.py` là lời giải tham chiếu.

## Expected Output

| Input | Expected |
| --- | --- |
| `Assign(Id("x"), IntLiteral(10)); putInt(x)` | `b'10'` |

## Run

Từ repository root, trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe ABSTRACT\exercise_01_visit_id\main.py
.\.venv\Scripts\python.exe ABSTRACT\exercise_01_visit_id\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python ABSTRACT/exercise_01_visit_id/main.py
.venv/bin/python ABSTRACT/exercise_01_visit_id/main.py --answer
```

Bỏ `--answer` để chạy skeleton sinh viên.
