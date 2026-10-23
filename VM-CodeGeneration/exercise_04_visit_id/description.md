# JVM-CodeGeneration 4 - visitId

## Đề bài

Hoàn thành `visitId(self, ctx, o)` để đọc giá trị identifier. Tìm symbol
theo thứ tự từ môi trường gần nhất ra ngoài; với `Index` dùng
`emitREADVAR`, với `CName` dùng `emitGETSTATIC`. Trả về `(code, s.mtype)`.

## Expected Output

| Input | Expected |
| --- | --- |
| `Id("a")` | `12` |
| `Id("z")` | `22` |
| `Id("x")` | `12.5` |
| `Id("y")` | `1.25` |
| `Id("n")` | `1.222` |
| `Id("m")` | `12220` |

## Run

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe SEQUENCE\exercise_04_visit_id\main.py
.\.venv\Scripts\python.exe SEQUENCE\exercise_04_visit_id\main.py --answer
```

Linux/macOS:

```bash
.venv/bin/python SEQUENCE/exercise_04_visit_id/main.py
.venv/bin/python SEQUENCE/exercise_04_visit_id/main.py --answer
```
