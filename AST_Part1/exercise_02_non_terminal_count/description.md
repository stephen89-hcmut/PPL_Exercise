# Bai 2 - NonTerminalCount



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

Please modify the bodies of NonTerminalCount's methods to count the internal nodes in the parse tree.

## Muc tieu

Dem so internal nodes trong parse tree. Moi `ParserRuleContext` duoc dem mot lan; terminal token khong duoc dem.

Sinh vien implement class `NonTerminalCount` trong `solution.py`. Runner mac
dinh chay skeleton; them `--answer` de chay dap an tham khao.

## Expected mau

`int a;` cho ket qua 6, `int a,b;` cho 7, sau do la 10, 11 va 13 theo cac test trong de.

## Run

Từ thư mục repository root, trước tiên chạy `.\.venv\Scripts\python.exe AST_Part1\setup.py` để generate parser. Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe AST_Part1\setup.py
.\.venv\Scripts\python.exe AST_Part1\exercise_02_non_terminal_count\main.py
.\.venv\Scripts\python.exe AST_Part1\exercise_02_non_terminal_count\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python AST_Part1/setup.py
.venv/bin/python AST_Part1/exercise_02_non_terminal_count/main.py
.venv/bin/python AST_Part1/exercise_02_non_terminal_count/main.py --answer
```

Lệnh đầu chạy skeleton sinh viên; `--answer` chạy lời giải tham chiếu.