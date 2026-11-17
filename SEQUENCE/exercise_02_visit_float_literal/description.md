# Question 2 — `visitFloatLiteral`

Assume `FloatLiteral` has a float field named `value`. `CodeGeneration` has
an `emit` field containing an `Emitter`, and the `Frame` is in `o.frame`.

Write `visitFloatLiteral(self, ctx, o)`. Return a pair containing Jasmin code
that loads `ctx.value` onto the operand stack and an instance of the matching
type subclass, `FloatType`. Use
`self.emit.emitPUSHFCONST(ctx.value, o.frame)` to produce the code.

The assessment examples are `5.0`, `2.17`, `-1.0`, `37.1846`, and `234.5`;
their reported results are `b'5.0'`, `b'2.17'`, `b'-1.0'`, `b'37.1846'`, and
`b'234.5'`. The local runner omits the assessment site's `b'…'` wrapper.

## Run

```bash
python3 SEQUENCE/exercise_02_visit_float_literal/main.py
python3 SEQUENCE/exercise_02_visit_float_literal/main.py --answer
```
