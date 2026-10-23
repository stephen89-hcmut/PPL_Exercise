# Sequence 6 - visitVarDecl

## Đề bài

Hoàn thành `visitVarDecl(self, ctx, o)` cho `VarDecl(name, typ)`. Nếu
`o.frame` là `None`, in directive `.field static` và trả về
`Symbol(name, typ, CName(self.className))`. Nếu là khai báo local, lấy index
mới từ frame, in directive `.var`, rồi trả về
`Symbol(name, typ, Index(index))`.

## Expected Output

```text
.field static x I
.var 0 is x F from start to end
.var 0 is y I from start to end
.var 1 is z F from start to end
```

## Run

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe SEQUENCE\exercise_06_visit_vardecl\main.py
.\.venv\Scripts\python.exe SEQUENCE\exercise_06_visit_vardecl\main.py --answer
```

Linux/macOS:

```bash
.venv/bin/python SEQUENCE/exercise_06_visit_vardecl/main.py
.venv/bin/python SEQUENCE/exercise_06_visit_vardecl/main.py --answer
```
