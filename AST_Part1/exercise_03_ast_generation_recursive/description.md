# Bai 3 - ASTGeneration voi grammar de quy



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

and AST classes as follows:

class Program:#decl:list(VarDecl)

class Type(ABC): pass

class IntType(Type): pass

class FloatType(Type): pass

class VarDecl: #variable:Id; varType: Type

class Id: #name:str

Please modify the bodies of ASTGeneration's methods to generate the AST of a MP input.

## Muc tieu

Sinh AST tu grammar co danh sach declaration va identifier viet bang production de quy.

Sinh vien implement cac method dang `return None` trong `solution.py`. Runner
mac dinh dung code sinh vien; them `--answer` de xem dap an tham khao.

Visitor tao cac node `Program`, `VarDecl`, `Id`, `IntType` va `FloatType`. `visitIds` tra ve danh sach Id, sau do `visitVardecl` tao mot VarDecl cho moi Id.

## Run

Từ thư mục PPL_Exercise, trước tiên chạy `python3 AST_Part1/setup.py` để generate parser. Trên Windows PowerShell:

```powershell
python3 AST_Part1/setup.py
python3 AST_Part1/exercise_03_ast_generation_recursive/main.py
python3 AST_Part1/exercise_03_ast_generation_recursive/main.py --answer
```

Trên Linux/macOS:

```bash
python3 AST_Part1/setup.py
python3 AST_Part1/exercise_03_ast_generation_recursive/main.py
python3 AST_Part1/exercise_03_ast_generation_recursive/main.py --answer
```

Lệnh đầu chạy skeleton sinh viên; `--answer` chạy lời giải tham chiếu.