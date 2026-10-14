# AST 1 - ids voi grammar de quy

## Đề bài

Cho grammar:

```antlr
start: ids EOF;
ids: ID CM ids | ID;
```

Hãy hoàn thành `visitIds` trong `ASTGeneration`, là subclass của visitor do ANTLR sinh ra. Method phải trả về danh sách lexeme của tất cả `ID` theo đúng thứ tự xuất hiện. Với alternative đệ quy, một `IdsContext` có thể chứa một `ID` và một `ctx.ids()` con.

Skeleton hiện tại giữ nguyên method và để trống phần thân; chỉ sửa `solution.py` theo yêu cầu bài tập.

## Expected Output

| Input     | Expected            |
| --------- | ------------------- |
| `a,b,c` | `['a', 'b', 'c']` |
| `x`     | `['x']`           |

## Run

Từ thư mục repository root:

```bash
.venv/bin/python INCLASS/ast_01_ids_recursive/main.py
.venv/bin/python INCLASS/ast_01_ids_recursive/main.py --answer
```

Lệnh đầu chạy skeleton sinh viên; `--answer` chạy lời giải tham chiếu.
