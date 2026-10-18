from NAME.common.ast_nodes import Program, RedeclaredConstant, RedeclaredVariable


class StaticCheck:
    def visitProgram(self, ctx: Program, o: object = None):
        names = []
        for declaration in ctx.decl:
            declaration.accept(self, names)

    def visitVarDecl(self, ctx, o):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        o.append(ctx.name)
        return o

    def visitConstDecl(self, ctx, o):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        o.append(ctx.name)
        return o

    def visitIntType(self, ctx, o):
        return o

    def visitFloatType(self, ctx, o):
        return o

    def visitIntLit(self, ctx, o):
        return o
