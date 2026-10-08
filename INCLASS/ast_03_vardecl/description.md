# AST 3 - VarDecl

Grammar: `vardecl: ids COLON typ; ids: ID (CM ID)*; typ: INTTYPE | FLOATTYPE;`.

Implement `visitVardecl`, `visitIds`, `visitTyp`. Declaration `x,y:int` sinh ra hai `VarDecl` objects.
