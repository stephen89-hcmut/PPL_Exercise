# Bai 3 - ASTGeneration voi grammar de quy

## Muc tieu

Sinh AST tu grammar co danh sach declaration va identifier viet bang production de quy.

Sinh vien implement cac method dang `return None` trong `solution.py`. Runner
mac dinh dung code sinh vien; them `--answer` de xem dap an tham khao.

Visitor tao cac node `Program`, `VarDecl`, `Id`, `IntType` va `FloatType`. `visitIds` tra ve danh sach Id, sau do `visitVardecl` tao mot VarDecl cho moi Id.

## Chay

```bash
.venv/bin/python AST_Part1/exercise_03_ast_generation_recursive/main.py
```
