# Question 1 — `visitIntLiteral`

Assume `IntLiteral` has an integer field named `value`. `CodeGeneration` has
an `emit` field containing an `Emitter`, and the `Frame` is in `o.frame`.

Write `visitIntLiteral(self, ctx, o)`. Return a pair containing Jasmin code
that loads `ctx.value` onto the operand stack and an instance of the matching
type subclass, `IntType`. Use
`self.emit.emitPUSHICONST(ctx.value, o.frame)` to produce the code.

The assessment examples are `IntLiteral(5)`, `IntLiteral(217)`,
`IntLiteral(-1)`, `IntLiteral(371846)`, and `IntLiteral(2345)`. Their reported
results are `b'5'`, `b'217'`, `b'-1'`, `b'371846'`, and `b'2345'`.

The local runner displays the evaluated value without the assessment site's
`b'…'` wrapper.

## Run

```bash
python3 SEQUENCE/exercise_01_visit_int_literal/main.py
python3 SEQUENCE/exercise_01_visit_int_literal/main.py --answer
```
