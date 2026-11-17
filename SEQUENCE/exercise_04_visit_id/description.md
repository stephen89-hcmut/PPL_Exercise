# Question 4 — `visitId`

Assume `Id` has a string field `name`. `o.frame` is the current `Frame`, and
`o.sym` is the symbol list. The list is ordered from the innermost environment
to the global environment. Each `Symbol` has `name`, `mtype`, and `value`;
`value` is either `Index(int)` for a local variable or `CName(str)` for a
global variable.

Write `visitId(self, ctx, o)`. Find the first matching symbol and return a
pair containing code that reads its value onto the operand stack and its
type. For a local variable, call `emitREADVAR(name, mtype, index, o.frame)`;
for a global variable, call `emitGETSTATIC(className/name, mtype, o.frame)`.
The supplied answer also handles the `o.isLeft` write case with
`emitWRITEVAR` or `emitPUTSTATIC`.

Examples from the assessment include `a → b'12'`, `z → b'1222'`,
`x → b'12.5'`, `y → b'1.25'`, `n → b'1.222'`, and local `m → b'12220'`.
The local runner prints the underlying value without the assessment site's
byte-string wrapper.

## Run

```bash
python3 SEQUENCE/exercise_04_visit_id/main.py
python3 SEQUENCE/exercise_04_visit_id/main.py --answer
```
