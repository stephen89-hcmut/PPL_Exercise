# Huong dan su dung PPL Exercises

Project gom hai nhom bai tap:

- `AST_Part1`: parse tree Height, NonTerminalCount va AST generation MP.
- `INCLASS`: Functional Programming va AST/Expression.

## 1. Yeu cau

- Python 3.10 tro len.
- Java de chay ANTLR tool.
- Ket noi Internet lan dau de tai ANTLR complete jar.

Runtime Python duoc khai bao trong `requirements.txt`:

```text
antlr4-python3-runtime==4.13.2
```

## 2. Cai dat

Tai thu muc project:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python AST_Part1/setup.py
.venv/bin/python INCLASS/setup.py
```

`setup.py` tai `antlr-4.13.2-complete.jar` neu file chua ton tai, sau do generate parser Python vao `AST_Part1/generated/`. Co the doi version bang:

```bash
ANTLR_VERSION=4.13.2 .venv/bin/python AST_Part1/setup.py
```

Hoac dat duong dan jar bang bien `ANTLR_JAR` trong moi truong cua ban va dieu chinh script neu can dung jar noi bo.

## 3. Chay bai tap

Chay tat ca dap an tham khao:

```bash
.venv/bin/python AST_Part1/run_all.py --answer
```

Chay tat ca skeleton de xem cac test dang cho:

```bash
.venv/bin/python AST_Part1/run_all.py
```

Chay tung bai:

```bash
.venv/bin/python AST_Part1/exercise_01_height/main.py
.venv/bin/python AST_Part1/exercise_02_non_terminal_count/main.py
.venv/bin/python AST_Part1/exercise_03_ast_generation_recursive/main.py
.venv/bin/python AST_Part1/exercise_04_ast_generation_repeated/main.py
```

Chay dap an tham khao cua tung bai AST_Part1 bang cach them `--answer`:

```bash
.venv/bin/python AST_Part1/exercise_01_height/main.py --answer
.venv/bin/python AST_Part1/exercise_02_non_terminal_count/main.py --answer
.venv/bin/python AST_Part1/exercise_03_ast_generation_recursive/main.py --answer
.venv/bin/python AST_Part1/exercise_04_ast_generation_repeated/main.py --answer
```

Moi dong report co dang `Test`, `Expected`, `Got`, `PASS`/`FAIL`. Neu parser loi, report in `ParseError`; neu ket qua khac expected, report in reason mismatch va van chay test tiep theo.

De xem mot test fail mau:

```bash
.venv/bin/python AST_Part1/exercise_01_height/main.py --demo-failure
```

## 4. INCLASS

Chay toan bo dap an tham khao:

```bash
.venv/bin/python INCLASS/run_all.py --answer
```

Chay skeleton cho sinh vien:

```bash
.venv/bin/python INCLASS/run_all.py
```

Chay rieng mot bai:

```bash
.venv/bin/python INCLASS/functional_03_double/main.py --answer
.venv/bin/python INCLASS/ast_07_expression_loop/main.py --answer
```

Danh sach lenh chay tung bai INCLASS:

```bash
# Functional Programming
.venv/bin/python INCLASS/functional_03_double/main.py --answer
.venv/bin/python INCLASS/functional_04_flatten/main.py --answer
.venv/bin/python INCLASS/functional_05_less_than/main.py --answer
.venv/bin/python INCLASS/functional_06_compose/main.py --answer

# AST va Expression
.venv/bin/python INCLASS/ast_01_ids_recursive/main.py --answer
.venv/bin/python INCLASS/ast_02_ids_loop/main.py --answer
.venv/bin/python INCLASS/ast_03_vardecl/main.py --answer
.venv/bin/python INCLASS/ast_04_program/main.py --answer
.venv/bin/python INCLASS/ast_05_expression_recursive/main.py --answer
.venv/bin/python INCLASS/ast_06_expression_precedence/main.py --answer
.venv/bin/python INCLASS/ast_07_expression_loop/main.py --answer
.venv/bin/python INCLASS/ast_08_expression_split/main.py --answer
```

De chay skeleton cho sinh vien, bo `--answer` khoi lenh tuong ung.

Moi bai INCLASS co `description.md`, `solution.py`, `answer.py` va `main.py`.
Sinh vien chi sua `solution.py`; `answer.py` la dap an tham khao. Report co
cac cot `Test`, `Expected`, `Got`, `PASS`/`FAIL` va `Reason`.

Functional exercises gom `double`, `flatten`, `lessThan` va `compose`. AST
exercises gom lexeme recursive/loop, `VarDecl`, `Program`, expression
precedence va left-associativity.

Quy uoc compose: `compose(f, g)(x)` ap dung `f` truoc roi den `g`, nen
`compose(double, increase)(3)` cho `7`.

Voi grammar expression loop, phai tao AST left-associative bang accumulator.
Vi du `1 - 2 - 3` la
`BinOp(-, BinOp(-, Num(1), Num(2)), Num(3))`.

## 5. Noi dung bon bai AST_Part1

1. **Height**: tinh chieu cao parse tree. Terminal co height 1; node co con co height bang 1 cong max height cua cac con. Bai nay cho phep chon start rule de kiem tra `program`, `mptype`, `ids`, `vardecl` va `vardecls`.
2. **NonTerminalCount**: dem tat ca `ParserRuleContext`, khong dem terminal token.
3. **ASTGeneration recursive**: dung grammar co `vardecltail` va `ids` de quy.
4. **ASTGeneration repeated**: dung grammar co `vardecl+` va `( ',' ID )*`.

Hai bai AST cung tao cac node `Program`, `VarDecl`, `Id`, `IntType`, `FloatType`. Vi du:

```text
int a;float b;
Program([VarDecl(Id(a),IntType), VarDecl(Id(b),FloatType)])
```

## 6. Mo rong test

Mo file `main.py` cua bai tuong ung va them `TestCase(source, expected)`. Voi Height, co the truyen them start rule:

```python
TestCase("a,b,c", "4", "ids")
```

Sau khi sua grammar, chay lai `AST_Part1/setup.py` de generate parser moi.

## 7. Cau truc

- `AST_Part1/grammar`: grammar ANTLR.
- `AST_Part1/generated`: parser generated, khong commit vao git.
- `AST_Part1/common`: parse utility, AST model va test reporter.
- `AST_Part1/exercise_*`: solution, test runner va mo ta tung bai.
- `INCLASS/grammar`: grammar ANTLR cho cac bai AST.
- `INCLASS/generated`: parser generated, khong commit vao git.
- `INCLASS/common`: reporter, AST nodes va parser utility.
- `INCLASS/functional_*`, `INCLASS/ast_*`: skeleton, answer, test va description.
- `INCLASS/run_all.py`: runner tong cho cac bai INCLASS.
- `OOP`: ba bai OOP ve arithmetic expression va Visitor pattern.
