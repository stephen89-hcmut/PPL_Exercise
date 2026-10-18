from NAME.common.ast_nodes import Program


class StaticCheck:
    def visitProgram(self, ctx: Program, o: object):
        return None

    def visitVarDecl(self, ctx, o: object):
        return None

    def visitConstDecl(self, ctx, o: object):
        return None

    def visitFuncDecl(self, ctx, o: object):
        return None

    def visitIntType(self, ctx, o: object):
        return None

    def visitFloatType(self, ctx, o: object):
        return None

    def visitIntLit(self, ctx, o: object):
        return None

    def visitId(self, ctx, o: object):
        return None
