# JVM-CodeGeneration 7 - control-flow Jasmin

## Đề bài

Viết các visitor sinh phần thân Jasmin cho ba chương trình:

1. `if (a > b) a = 1; else a = 2`
2. `while (a < 10) a = a + 1`
3. `for (a = 1; a < 10; a++) b = b + 1`

Hoàn thành `visitIf(self, ctx, o)`, `visitWhile(self, ctx, o)` và `visitFor(self, ctx, o)`. Các nhánh và vòng lặp phải dùng nhãn, nhảy điều kiện, `goto`, load/store local và phép toán số nguyên đúng thứ tự. Bài kiểm tra so sánh phần thân method; class/method wrapper do chương trình bao ngoài cung cấp. Để làm rõ chỗ ảnh không chỉ định, dùng local slot 0 cho `a`, slot 1 cho `b`, bắt đầu nhãn từ `L0`, và dùng branch đối nghịch để nhảy ra khỏi thân khi điều kiện sai. Điều kiện for là `a < 10` nên không bao gồm 10.

## Expected Output

| Input | Expected Jasmin body |
| --- | --- |
| `if (a > b) a = 1; else a = 2` | `iload_0`, `iload_1`, `if_icmple L0`, nhánh gán 1, `goto L1`, nhánh gán 2 tại `L0`, kết thúc ở `L1` |
| `while (a < 10) a = a + 1` | nhãn đầu vòng, so sánh `a >= 10` để thoát, cộng 1, quay lại đầu vòng |
| `for (a = 1; a < 10; a++) b = b + 1` | khởi tạo slot 0, kiểm tra điều kiện, tăng slot 1 trong thân, `iinc 0 1`, quay lại đầu vòng |

Runner so sánh toàn bộ chuỗi Jasmin, bao gồm thứ tự lệnh và nhãn.

## Run

Windows PowerShell:

```powershell
py VM-CodeGeneration/exercise_07_visit_control_flow/main.py
py VM-CodeGeneration/exercise_07_visit_control_flow/main.py --answer
```

Linux/macOS:

```bash
python3 VM-CodeGeneration/exercise_07_visit_control_flow/main.py
python3 VM-CodeGeneration/exercise_07_visit_control_flow/main.py --answer
```

Bỏ `--answer` để chạy skeleton trong `solution.py`.
