# Huong dan OOP Exercises

## Cau truc

- `oop_01_eval`: `Exp`, `BinExp`, `UnExp`, `IntLit`, `FloatLit` va `eval()`.
- `oop_02_print_prefix`: mo rong classes voi `printPrefix()` va `printPostfix()`.
- `oop_03_visitor`: dung Visitor pattern voi `Eval`, `PrintPrefix`, `PrintPostfix`.
- `common/reporting.py`: test reporter dung chung.

Moi bai co `solution.py` la skeleton cho sinh vien, `answer.py` la dap an tham khao, `main.py` la runner doc lap va `description.md` la de bai.

## Chay tung bai

```bash
.venv/bin/python OOP/oop_01_eval/main.py --answer
.venv/bin/python OOP/oop_02_print_prefix/main.py --answer
.venv/bin/python OOP/oop_03_visitor/main.py --answer
```

Bo `--answer` de chay skeleton sinh vien:

```bash
.venv/bin/python OOP/oop_03_visitor/main.py
```

## Chay tat ca

```bash
.venv/bin/python OOP/run_all.py --answer
```

## AST formats

- Prefix binary: `op left right`.
- Prefix unary: `+. operand` hoac `-. operand`.
- Postfix binary: `left right op`.
- Postfix unary: `operand +.` hoac `operand -.`.

OOP 3 su dung double dispatch: moi node goi `visitor.visit<ClassName>(self)`. Khong dung `type()` hoac `isinstance()` trong phan visitor.
