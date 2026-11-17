# Question 5 — mixed `visitBinExpr`

Assume `BinExpr` has `op`, `e1`, and `e2`. The supported operators are
`+`, `-`, `*`, `/`, `>`, `<`, `>=`, `<=`, `!=`, and `==`; operands may be
`IntType` or `FloatType`, with no type errors. `+`, `-`, and `*` return
`IntType` when both operands are integers and `FloatType` otherwise. `/`
always returns `FloatType`. Relational operators return `BoolType`.

Write `visitBinExpr(self, ctx, o)` to return Jasmin code and the result type.
Visit both operands, choose the numeric operation type, promote integer
operand code with `emitI2F` when the operation type is float, then use
`emitREOP`, `emitADDOP`, or `emitMULOP` as appropriate. The local runner
represents Boolean results as integers, matching the assessment's `putInt`
examples (`1` for true and `0` for false).

Assessment examples include `5 > 3 → b'1'`, `(5 - 3) * 3.0 → b'6.0'`,
`-1.0 + 1.0 → b'0.0'`, `2 * (10.0 - 2) → b'16.0'`,
`(9 - 3) / 3 → b'2.0'`, `2 >= (10.0 - 2) → b'0'`,
`2 == (10.0 / 5) → b'1'`, and `2 != (4 - 2) → b'0'`.

## Run

```bash
python3 SEQUENCE/exercise_05_visit_binexpr_mixed/main.py
python3 SEQUENCE/exercise_05_visit_binexpr_mixed/main.py --answer
```
