# AST 4 - Program

Grammar: `program: vardecl+ EOF;` voi `vardecl: ids COLON typ;`.

Implement `visitProgram` va flatten danh sach cac declaration. Mot vardecl co the sinh nhieu `VarDecl`, vi vay khong duoc de ket qua la list of lists.
