---
name: ppl-exercise-generator
description: "Use when the user provides a programming-language exercise description, grammar, skeleton code, and Expected/Got test cases and wants a runnable educational exercise project with student TODOs, a reference answer, automated PASS/FAIL reporting, and documentation."
---

# PPL Exercise Generator

## Purpose

Generate educational programming-language exercises from three inputs:

1. Exercise description and grammar.
2. Student skeleton code.
3. Test cases and expected outputs, especially `Test`, `Expected`, and `Got` examples.

The output must let a student edit the skeleton, run tests, see PASS/FAIL and failure reasons, and compare against a reference answer without exposing the answer in the student file.

## Workflow

### Inspect

- Find the project root and preserve its existing language, framework, naming, and test conventions.
- If the workspace is empty, create a minimal runnable structure.
- Check the runtime, package manager, parser generator, and dependencies before editing.
- Resolve the project interpreter before running or documenting any command. Prefer an existing workspace environment such as `.venv/bin/python` (macOS/Linux) or `.venv\\Scripts\\python.exe` (Windows); otherwise use the repository's configured interpreter.
- Use the same resolved interpreter for package installation, parser generation, syntax checks, reference tests, student tests, and commands written in `description.md`. Do not assume the system `python` or `python3` has project dependencies.
- Verify imports for required runtime packages before executing generated code. For ANTLR Python projects, verify `antlr4` from `antlr4-python3-runtime` in the resolved interpreter.
- Never overwrite unrelated user changes.

### Cross-platform documentation commands

Every generated exercise `description.md` must use a `## Run` section with
both platform forms. For parser-based groups, document setup before the
individual runner:

````markdown
## Run

Từ thư mục repository root, trước tiên chạy `GROUP/setup.py` để generate
parser. Trên Windows PowerShell:

```powershell
.\.venv\Scripts\python.exe GROUP\setup.py
.\.venv\Scripts\python.exe GROUP\EXERCISE\main.py
.\.venv\Scripts\python.exe GROUP\EXERCISE\main.py --answer
```

Trên Linux/macOS:

```bash
.venv/bin/python GROUP/setup.py
.venv/bin/python GROUP/EXERCISE/main.py
.venv/bin/python GROUP/EXERCISE/main.py --answer
```

Lệnh đầu chạy skeleton sinh viên; `--answer` chạy lời giải tham chiếu.
````

For OOP exercises, omit the setup command and keep the two runner commands in
both platform blocks. Never document `.venv/bin/python` as a Windows command,
and never use bare `python` or `python3` when the project virtual environment
is available.

### Environment and dependency setup

Before editing or validation:

1. Detect the repository interpreter. If `.venv` exists, use its Python executable unless the repository explicitly specifies another environment.
2. Check the dependency file and test imports with that interpreter, for example:

  ```bash
  .venv/bin/python -c "import antlr4; print('antlr4 runtime: OK')"
  ```

3. If a required package is missing, install the repository dependency file into that same environment, for example:

  ```bash
  .venv/bin/python -m pip install -r requirements.txt
  ```

4. Re-run the import check before running tests. Never fix a project dependency by installing into an unrelated global Python environment without documenting that choice.
5. Put the resolved interpreter in every setup, generation, test, and individual-runner command documented for students. If no environment exists, document the exact interpreter and installation command used.

For generated-parser projects, also verify that the generated modules are present after parser generation and that the runtime import succeeds from the same interpreter. A successful Java/ANTLR generation step alone does not prove that Python can import the generated visitor.

### Extract the contract

Identify from the user input:

- Grammar productions, lexer tokens, and grammar variant.
- Required class names and method signatures.
- AST classes and exact constructor/repr requirements.
- Parse-tree metric conventions, including terminals, EOF, empty productions, and non-terminals.
- Every expected value from the supplied test output.
- Invalid-input behavior and required errors.

Treat supplied expected outputs as the exact behavioral contract.

### Create each exercise

For every exercise create:

- `description.md`: must follow the required documentation format below.
- `solution.py`: student skeleton only. Preserve the requested class, base class, method names, and parameters. Methods the student must implement must remain `return None` or the exact placeholder from the prompt. Do not leave hidden working helpers in the student file.
- `answer.py`: complete reference implementation used only for validation.
- `main.py`: isolated runner for this exercise only; support `--answer` for the reference implementation and `--demo-failure` for a deliberate mismatch.

Every exercise runner must be independently executable. Running one command such
as `python exercise_04/main.py` must print only that exercise's test cases. It
must not import, invoke, or print results from a sibling exercise or the root
runner. A root `run_all.py` may exist separately for running the complete suite.

For a group of exercises also create or reuse:

- Grammar files and parser generation setup.
- Shared parser/error utility.
- Shared AST model when applicable.
- Shared reporter.
- Root runner with correct exit codes.
- `README.md` and `Guid.md`.

### Required `description.md` format

Every exercise's `description.md` must contain these headings in this order:

```markdown
# <Exercise title>

## Đề bài
<The complete exercise requirement, grammar/API, constraints, and skeleton expectations.>

## Expected Output
<Every supplied input and its expected output, copied into readable examples or a table.>

## Run
<Commands to run this exercise alone, run the reference answer with --answer, and run the student skeleton.>
```

Rules:

- Keep the three headings exactly as `Đề bài`, `Expected Output`, and `Run`.
- `Đề bài` must include the task requirements and the relevant skeleton/API, not only a short summary.
- `Expected Output` must include all Expected values supplied by the user and the corresponding inputs. Do not omit cases that demonstrate a common failure.
- `Run` must contain commands for the isolated exercise runner. Include `--answer` when the project provides a reference answer and explain that removing it runs the student skeleton.
- Commands in `Run` must use the resolved project interpreter, not an unverified system command such as bare `python` or `python3`.
- Do not replace the required sections with only a link to another document. Additional sections may follow `Run`.

### Preserve skeleton semantics

- Keep class names, visitor base class, method names, and parameters.
- For ANTLR-generated Python, a grammar-specific visitor such as `MPRecursiveVisitor` or `MPRepeatedVisitor` is the infrastructure equivalent of `MPVisitor` in the prompt.
- Add only imports and minimal runner plumbing needed to execute the skeleton.
- If recursive grammar requires extra visitor methods not shown in the prompt, document why and include them as TODO methods rather than implementing them invisibly.
- Preserve user edits in the student file. Read the current file before editing and
  repair only the requested slice.
- Match the actual grammar variant used by the exercise. For example, a repeated
  grammar exposes `ctx.vardecl()` as a list; do not call a recursive-only rule such
  as `ctx.vardecls()` when it does not exist.

### Implement the reference answer

Implement `answer.py` from the grammar and contract, not by copying hidden logic into `solution.py`.

Common patterns:

- Height: follow the supplied recurrence exactly, including empty alternatives.
- Non-terminal count: count parser-rule contexts only when that is the stated contract.
- Recursive AST grammar: flatten recursive tail productions while preserving order.
- Repeated AST grammar: iterate repeated declaration contexts and identifier terminals.

Match exact AST output such as `Program([VarDecl(Id(a),IntType)])`.

### Reporter requirements

Print columns equivalent to `Test | Expected | Got | Status`.

- PASS only when normalized actual output equals expected.
- FAIL for mismatch, parser error, exception, or invalid output.
- Print a concise `Reason` with expected/actual mismatch or exception details.
- Continue after failures.
- Return exit code 0 only when all selected tests pass.
- An individual runner must report only its own tests and its own summary.
- Exceptions caused by an incomplete student implementation must be reported as
  `FAIL` with the exception type/message, without stopping later test cases.

### Validation

Run:

1. Syntax/compile checks.
2. Parser generation from source grammar.
3. Each reference runner with `--answer`; all supplied cases must pass.
4. Each student runner without `--answer`; skeleton cases should fail with useful Expected/Got/Reason output.
5. Root reference runner with `--answer`; confirm exit code 0.
6. A deliberate mismatch and malformed input when relevant.
7. Run at least one individual exercise command and verify that no neighboring
	exercise output appears.
8. Run the exact interpreter-qualified command copied into the exercise's `Run` section, including from a clean terminal context when possible. Confirm that dependency errors such as `ModuleNotFoundError` do not occur.

Do not claim success unless commands were actually run. Report missing prerequisites such as Java, ANTLR, or package installation.

## Conventions

- Use ASCII in source code unless another encoding is required.
- Keep generated parser files out of version control when they can be regenerated.
- Document setup, parser generation, individual runners, root runner, `--answer`, and `--demo-failure`.
- Keep scope limited to the supplied exercises.

## Clarification policy

Ask only when a missing choice changes implementation, such as ANTLR versus a self-contained parser, recursive versus repeated grammar, whether to include a reference answer, or workspace versus user-level scope. Otherwise infer from the grammar and expected outputs, implement, validate, and summarize.
