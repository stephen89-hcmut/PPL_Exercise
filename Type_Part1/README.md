# Type_Part1

Năm bài tập dựa trên `[CC03] Type Programming Code 1` và
`[CC03] Type Programming 2`:

1. `exercise_01_expression_types`: suy diễn kiểu cho biểu thức.
2. `exercise_02_program_types`: suy diễn kiểu với khai báo biến và tra cứu `Id`.
3. `exercise_03_program_type_inference`: suy diễn kiểu ở program-level.
4. `exercise_04_block_type_inference`: suy diễn kiểu trong block scope.
5. `exercise_05_function_type_inference`: suy diễn kiểu parameter và function call.

Sinh viên chỉ sửa `solution.py`. `answer.py` là lời giải tham chiếu; thêm
`--answer` khi chạy để kiểm tra đáp án. Mỗi runner in `Test`, `Expected`,
`Got`, `Status` và `Reason`, đồng thời tiếp tục chạy sau lỗi.

## Run

Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe Type_Part1\run_all.py --answer
```

Linux/macOS:

```bash
.venv/bin/python Type_Part1/run_all.py --answer
```

Bỏ `--answer` để chạy skeleton.
