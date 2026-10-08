# AST 2 - ids voi grammar vong lap

Grammar: `ids: ID (CM ID)*;`. Tat ca ID nam trong cung `IdsContext`, vi vay `visitIds` dung `ctx.ID()` va khong goi `ctx.ids()`.

Input `a,b,c` can cho `['a', 'b', 'c']`.
