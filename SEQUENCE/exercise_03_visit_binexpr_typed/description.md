# Question 3 — typed `visitBinExpr`

Assume `BinExpr` has fields `op` (`str`), `e1`, and `e2` (`Expr`). `Expr` is
the superclass of `BinExpr`, `IntLiteral`, and `FloatLiteral`. Operators are
`+`, `-`, `*`, `/`, `+.`, `-.`, `*.`, and `/.`. The first four take integer
operands; dotted operators take float operands. No type errors occur.

Write `visitBinExpr(self, ctx, o)` in `CodeGeneration`. Return a pair with
Jasmin code for the binary expression and an instance of the result type.
The `Frame` is in `o.frame`, and `self.emit` is an `Emitter`. Integer
operators return `IntType`; dotted operators return `FloatType`. Visit both
children using the same `o`, concatenate their code in evaluation order, and
append the matching arithmetic instruction from the emitter.

The examples cover `5 + 3`, `(5 - 3) * 3`, `-1.0 +. 1.0`,
`1.0 *. (10.0 -. 2.0)`, and `(5 - 3) / 3`. The assessment reports results
such as `b'8'`; the local runner omits the assessment site's `b'…'` wrapper.

## Run

```bash
python3 SEQUENCE/exercise_03_visit_binexpr_typed/main.py
python3 SEQUENCE/exercise_03_visit_binexpr_typed/main.py --answer
```
