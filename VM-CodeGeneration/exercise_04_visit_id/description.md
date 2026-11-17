# JVM-CodeGeneration 4 - visitId

## Đề bài

Hoàn thành `visitId(self, ctx, o)` để đọc giá trị identifier. Tìm symbol
theo thứ tự từ môi trường gần nhất ra ngoài; với `Index` dùng
`emitREADVAR`, với `CName` dùng `emitGETSTATIC`. Trả về `(code, s.mtype)`.

## Expected Output

| Input       | Expected  |
| ----------- | --------- |
| `Id("a")` | `b'12'` |
| `Id("z")` | `b'22'` |
| `Id("x")` | `b'12.5'` |
| `Id("y")` | `b'1.25'` |
| `Id("n")` | `b'1.222'` |
| `Id("m")` | `b'12220'` |

## Run

Windows PowerShell:

```powershell
python3 VM-CodeGeneration/exercise_04_visit_id/main.py
python3 VM-CodeGeneration/exercise_04_visit_id/main.py --answer
```

Linux/macOS:

```bash
python3 VM-CodeGeneration/exercise_04_visit_id/main.py
python3 VM-CodeGeneration/exercise_04_visit_id/main.py --answer
```
