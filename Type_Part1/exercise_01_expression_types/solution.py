from Type_Part1.common.ast_nodes import BoolLit, FloatLit, IntLit


class StaticCheck:
    def visitBinOp(self, ctx, o):
        return None

    def visitUnOp(self, ctx, o):
        return None

    def visitIntLit(self, ctx: IntLit, o):
        return None

    def visitFloatLit(self, ctx: FloatLit, o):
        return None

    def visitBoolLit(self, ctx: BoolLit, o):
        return None
