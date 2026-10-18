from NAME.common.ast_nodes import Program, RedeclaredDeclaration


class StaticCheck:
    def visitProgram(self, ctx: Program, o: object = None):
        names = []
        for declaration in ctx.decl:
            declaration.accept(self, names)
        return names

    def visitVarDecl(self, ctx, o):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        o.append(ctx.name)
        return o

    def visitConstDecl(self, ctx, o):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        o.append(ctx.name)
        return o

    def visitIntType(self, ctx, o):
        return o

    def visitFloatType(self, ctx, o):
        return o

    def visitIntLit(self, ctx, o):
        return o
