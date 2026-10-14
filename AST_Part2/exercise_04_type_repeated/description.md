# Type AST Generation - Recursive Array Rule

## Đề bài

Cho grammar MP:

```text
program: mptype EOF;
arraytype: primtype dimen | arraytype dimen;
mptype: primtype | arraytype;
primtype: INTTYPE | FLOATTYPE;
dimen: '[' num '..' num ']';
num: '-'? INTLIT;
```

Hãy hoàn thành `ASTGeneration` trong `solution.py`. Mỗi dimension tạo một `RangeType`; nhiều dimension phải được gộp vào `UnionType` theo thứ tự xuất hiện, và kiểu phần tử giữ nguyên là `IntType` hoặc `FloatType`.

## Expected Output

| Input                                 | Expected                                                                                         |
| ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `real [-3..0][-10..-1]`               | `ArrayType(UnionType(RangeType(-3,0),RangeType(-10,-1)),FloatType)`                              |
| `integer[1..3]`                       | `ArrayType(RangeType(1,3),IntType)`                                                              |
| `integer [1..100][-5..20][100..3000]` | `ArrayType(UnionType(UnionType(RangeType(1,100),RangeType(-5,20)),RangeType(100,3000)),IntType)` |

## Run

```bash
python AST_Part2/setup.py
python AST_Part2/exercise_04_type_repeated/main.py
python AST_Part2/exercise_04_type_repeated/main.py --answer
python AST_Part2/exercise_04_type_repeated/main.py --demo-failure
```

Bỏ `--answer` để chạy skeleton sinh viên.
