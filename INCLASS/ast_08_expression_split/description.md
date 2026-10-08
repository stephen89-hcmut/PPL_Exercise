# AST 8 - Expression grammar split operator rules

Grammar tach rieng `addop` va `mulop`. Implement `visitExp`, `visitAddop`, `visitTerm`, `visitMulop` va tao AST left-associative. Test `a * b / c` phai cho `BinOp(/, BinOp(*, Var(a), Var(b)), Var(c))`.
