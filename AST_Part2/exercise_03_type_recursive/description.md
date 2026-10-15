# Type AST Generation - Recursive Dimensions

## Đề bài

Cho grammar MP:

``text
program: mptype EOF;
mptype: primtype | arraytype;
arraytype: primtype dimens;
primtype: INTTYPE | FLOATTYPE;
dimens: dimen+;
dimen: '[' num '..' num ']';
num: '-'? INTLIT;
``

Hãy hoàn thành `ASTGeneration` trong `solution.py`. Kiểu nguyên thủy là `IntType` hoặc `FloatType`; mỗi khoảng là `RangeType(lowbound, highbound)`; nhiều khoảng phải được gộp trái thành `UnionType`, rồi tạo `ArrayType(indexType, eleType)`.

## Expected Output

| Input                                 | Expected                                                                                         |
| ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `real [-3..0][-10..-1]`               | `ArrayType(UnionType(RangeType(-3,0),RangeType(-10,-1)),FloatType)`                              |
| `integer[1..3]`                       | `ArrayType(RangeType(1,3),IntType)`                                                              |
| `integer [1..100][-5..20][100..3000]` | `ArrayType(UnionType(UnionType(RangeType(1,100),RangeType(-5,20)),RangeType(100,3000)),IntType)` |

## Run

Từ thư mục repository root, trước tiên chạy `.\.venv\Scripts\python.exe AST_Part2\setup.py` để generate parser. Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe AST_Part2\setup.py
.\.venv\Scripts\python.exe AST_Part2\exercise_03_type_recursive\main.py
.\.venv\Scripts\python.exe AST_Part2\exercise_03_type_recursive\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python AST_Part2/setup.py
.venv/bin/python AST_Part2/exercise_03_type_recursive/main.py
.venv/bin/python AST_Part2/exercise_03_type_recursive/main.py --answer
```

Lệnh đầu chạy skeleton sinh viên; `--answer` chạy lời giải tham chiếu.