# Exercise 4 - ASTGeneration voi grammar lap

## De bai

Given the grammar of MP as follows:

```text
program: vardecl+ EOF;
vardecl: mptype ids ';' ;
mptype: INTTYPE | FLOATTYPE;
ids: ID (',' ID)*;
INTTYPE: 'int';
FLOATTYPE: 'float';
ID: [a-z]+;
```

And AST classes:

```python
class Program:  # decl: list[VarDecl]
class Type(ABC): pass
class IntType(Type): pass
class FloatType(Type): pass
class VarDecl:  # variable: Id; varType: Type
class Id:  # name: str
```

Hãy hoàn thiện class `ASTGeneration` để sinh AST từ input MP. Trong project này,
`MPRepeatedVisitor` là tên visitor được ANTLR generate tương ứng với `MPVisitor`
trong đề Moodle.

```python
class ASTGeneration(MPRepeatedVisitor):
	def visitProgram(self, ctx):
		return None

	def visitVardecl(self, ctx):
		return None

	def visitMptype(self, ctx):
		return None

	def visitIds(self, ctx):
		return None
```

Sinh viên tự implement các method trên để tất cả test case PASS.

## Expected output

Ví dụ input `int a;float b;` cần tạo:

```text
Program([VarDecl(Id(a),IntType), VarDecl(Id(b),FloatType)])
```

Diem can chu y la ANTLR tra ve danh sach context cho `ctx.vardecl()` va danh sach terminal cho `ctx.ID()`. Visitor can lap qua cac danh sach nay de tao AST phang.

## Chay

```bash
.venv/bin/python AST_Part1/exercise_04_ast_generation_repeated/main.py
```

Runner mac dinh dung `solution.py` de sinh vien lam bai. De kiem tra expected
bang dap an tham khao:

```bash
.venv/bin/python AST_Part1/exercise_04_ast_generation_repeated/main.py --answer
```
