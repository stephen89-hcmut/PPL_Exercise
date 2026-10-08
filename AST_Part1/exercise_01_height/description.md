# Bai 1 - Height

## Muc tieu

Viet visitor tinh height cua parse tree cho grammar `MPRecursive.g4`.

Mo file `solution.py` va implement phan dang de trong class `Height`. Chay
runner khong co `--answer` de xem ket qua bai lam; `--answer` chi dung de xem
dap an tham khao.

Quy uoc: terminal co height 1; node khong co con co height 1; node co con co height `1 + max(height(child))`.

## Grammar

```text
program: vardecls EOF;
vardecls: vardecl vardecltail;
vardecltail: vardecl vardecltail | ;
vardecl: mptype ids ';';
mptype: INTTYPE | FLOATTYPE;
ids: ID ',' ids | ID;
```

## Chay

```bash
.venv/bin/python AST_Part1/exercise_01_height/main.py
```

Bai co test cho ca `program` va cac rule con `mptype`, `ids`, `vardecl`, `vardecls`.
