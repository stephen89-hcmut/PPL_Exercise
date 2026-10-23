# ABSTRACT

Năm bài này chuyển toàn bộ 5 câu trong PDF `[CC03] Abstract Programming
Code` thành exercise Python độc lập:

1. `visitId`: đọc/ghi biến cục bộ và toàn cục.
2. `visitAssign`: sinh phép gán theo thứ tự RHS trước LHS.
3. `visitIf`: sinh nhánh if/else và nhãn thoát.
4. `visitWhile`: sinh vòng lặp cùng nhãn break/continue.
5. `visitFor`: sinh khởi tạo, cận, cập nhật và nhãn vòng lặp.

Sinh viên chỉ sửa `solution.py`; `answer.py` chứa lời giải tham chiếu. Mỗi
bài có runner riêng, cột `Test | Expected | Got | Status`, `--answer`, và
`--demo-failure` để xem một lỗi mismatch có chủ đích.

## Run

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe ABSTRACT\run_all.py
.\.venv\Scripts\python.exe ABSTRACT\run_all.py --answer
```

Linux/macOS:

```bash
.venv/bin/python ABSTRACT/run_all.py
.venv/bin/python ABSTRACT/run_all.py --answer
.venv/bin/python ABSTRACT/exercise_01_visit_id/main.py --demo-failure
```
