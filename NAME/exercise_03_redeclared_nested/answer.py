from NAME.common.ast_nodes import (
    Program, RedeclaredConstant, RedeclaredFunction, RedeclaredVariable,
)


class StaticCheck:
    def visitProgram(self, ctx: Program, o: object = None):
        scope = []
        for declaration in ctx.decl:
            declaration.accept(self, [scope])

    def visitVarDecl(self, ctx, o):
        if ctx.name in o[0]:
            raise RedeclaredVariable(ctx.name)
        o[0].append(ctx.name)
        return o

    def visitConstDecl(self, ctx, o):
        if ctx.name in o[0]:
            raise RedeclaredConstant(ctx.name)
        o[0].append(ctx.name)
        return o

    def visitFuncDecl(self, ctx, o):
        if ctx.name in o[0]:
            raise RedeclaredFunction(ctx.name)
        o[0].append(ctx.name)
        function_scope = [[]] + o
        for parameter in ctx.param:
            parameter.accept(self, function_scope)
        for declaration in ctx.body:
            declaration.accept(self, function_scope)
        return o

    def visitIntType(self, ctx, o):
        return o

    def visitFloatType(self, ctx, o):
        return o

    def visitIntLit(self, ctx, o):
        return o
