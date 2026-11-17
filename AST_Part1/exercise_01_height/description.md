# Bai 1 - Height



Given the grammar of MP as follows:

program: vardecls EOF;

vardecls: vardecl vardecltail;

vardecltail: vardecl vardecltail | ;

vardecl: mptype ids ';' ;

mptype: INTTYPE | FLOATTYPE;

ids: ID ',' ids | ID;

INTTYPE: 'int';

FLOATTYPE: 'float';

ID: [a-z]+ ;

Please modify the bodies of Height's methods to return the height of the parse tree. Your code starts at line 10.

## Muc tieu

Viet visitor tinh height cua parse tree cho grammar `MPRecursive.g4`.

Mo file `solution.py` va implement phan dang de trong class `Height`. Chay
runner khong co `--answer` de xem ket qua bai lam; `--answer` chi dung de xem
dap an tham khao.

Quy uoc: terminal co height 1; node khong co con co height 1; node co con co height `1 + max(height(child))`.

## Grammar

``text
program: vardecls EOF;
vardecls: vardecl vardecltail;
vardecltail: vardecl vardecltail | ;
vardecl: mptype ids ';';
mptype: INTTYPE | FLOATTYPE;
ids: ID ',' ids | ID;
``

## Run

Từ thư mục PPL_Exercise, trước tiên chạy `python3 AST_Part1/setup.py` để generate parser. Trên Windows PowerShell:

```powershell
python3 AST_Part1/setup.py
python3 AST_Part1/exercise_01_height/main.py
python3 AST_Part1/exercise_01_height/main.py --answer
```

Trên Linux/macOS:

```bash
python3 AST_Part1/setup.py
python3 AST_Part1/exercise_01_height/main.py
python3 AST_Part1/exercise_01_height/main.py --answer
```

Lệnh đầu chạy skeleton sinh viên; `--answer` chạy lời giải tham chiếu.