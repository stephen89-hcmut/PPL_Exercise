# Huong dan INCLASS

## Cau truc

- `functional_03_double` den `functional_06_compose`: bai functional programming.
- `ast_01_ids_recursive` den `ast_04_program`: lexeme va AST khai bao bien.
- `ast_05_expression_recursive` den `ast_08_expression_split`: AST bieu thuc, precedence va associativity.
- `common`: reporter, AST nodes va parser utility.
- `grammar`: grammar ANTLR4.

## Chay

Generate parser:

```bash
.venv/bin/python INCLASS/setup.py
```

Chay dap an tham khao:

```bash
.venv/bin/python INCLASS/run_all.py --answer
```

Chay code sinh vien:

```bash
.venv/bin/python INCLASS/run_all.py
```

Chay tung bai rieng:

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

Bo `--answer` de chay skeleton sinh vien. Sua `solution.py`, khong sua `answer.py`.

Functional:

- `functional_03_double`: list comprehension, recursive, higher-order.
- `functional_04_flatten`: flatten bang ba cach.
- `functional_05_less_than`: loc phan tu nho hon `n` bang ba cach.
- `functional_06_compose`: compose recursive va higher-order, theo thu tu trai sang phai.

AST:

- `ast_01_ids_recursive`: tham `ctx.ids()` de lay du lexeme.
- `ast_02_ids_loop`: lay tat ca token bang `ctx.ID()`.
- `ast_03_vardecl`: mot declaration co the tao nhieu `VarDecl`.
- `ast_04_program`: flatten list cac declaration.
- `ast_05_expression_recursive` va `ast_06_expression_precedence`: AST expression de quy va precedence.
- `ast_07_expression_loop`: tao AST left-associative trong loop.
- `ast_08_expression_split`: lay operator qua `visitAddop` va `visitMulop`.

Parser generated nam trong `generated/` va da duoc them vao `.gitignore`. Neu
sua grammar, chay lai `INCLASS/setup.py` truoc khi chay test.

## Quy uoc compose

`compose(f, g)(x)` ap dung `f` truoc, sau do ap dung `g`, nen `compose(double, increase)(3)` cho `7`.

## Quy uoc AST expression

AST dung `Num`, `Var`, `BinOp`. Grammar loop phai tu tao left-associative bang cach cap nhat accumulator trong moi vong lap. Grammar split dung `visitAddop` va `visitMulop` de lay operator text.
