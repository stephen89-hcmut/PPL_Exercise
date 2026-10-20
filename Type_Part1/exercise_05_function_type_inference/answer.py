from Type_Part1.common.type2_nodes import (
    CallStmt, FuncDecl, TypeCannotBeInferred, TypeMismatchInStatement,
    UndeclaredIdentifier, Redeclared,
)

UNKNOWN = object()


def find(name, env):
    for scope in env:
        if name in scope:
            return scope[name]
    raise UndeclaredIdentifier(name)


class StaticCheck:
    def visit(self, node, o=None):
        return node.accept(self, o)

    def visitProgram(self, ctx, o=None):
        scope = {}
        self._declare(ctx.decl, scope)
        env = [scope]
        for declaration in ctx.decl:
            if isinstance(declaration, FuncDecl):
                self._check_function(declaration, env)
        for stmt in ctx.stmts:
            self.visit(stmt, env)

    def _declare(self, declarations, scope):
        for declaration in declarations:
            if declaration.name in scope:
                raise Redeclared(declaration)
            if isinstance(declaration, FuncDecl):
                scope[declaration.name] = declaration
            else:
                scope[declaration.name] = UNKNOWN

    def visitVarDecl(self, ctx, o):
        return UNKNOWN

    def visitFuncDecl(self, ctx, o):
        self._check_function(ctx, o)

    def _check_function(self, ctx, outer):
        scope = {}
        self._declare(ctx.param, scope)
        self._declare(ctx.local, scope)
        env = [scope] + outer
        for stmt in ctx.stmts:
            self.visit(stmt, env)
        ctx._param_types = [scope[parameter.name] for parameter in ctx.param]

    def visitCallStmt(self, ctx, o):
        function = find(ctx.name, o)
        if not isinstance(function, FuncDecl):
            raise UndeclaredIdentifier(ctx.name)
        if len(ctx.args) != len(function.param):
            raise TypeMismatchInStatement(ctx)
        for argument, parameter in zip(ctx.args, function.param):
            arg_type = self.visit(argument, o)
            if arg_type is UNKNOWN:
                raise TypeCannotBeInferred(ctx)
            old = getattr(function, "_param_types", [UNKNOWN] * len(function.param))[
                function.param.index(parameter)
            ]
            if old is not UNKNOWN and old is not arg_type:
                raise TypeMismatchInStatement(ctx)
        for parameter_type in getattr(function, "_param_types", []):
            if parameter_type is UNKNOWN:
                raise TypeCannotBeInferred(ctx)

    def visitAssign(self, ctx, o):
        rhs = self.visit(ctx.rhs, o)
        lhs = find(ctx.lhs.name, o)
        if lhs is UNKNOWN and rhs is UNKNOWN:
            raise TypeCannotBeInferred(ctx)
        if lhs is UNKNOWN:
            self._set(ctx.lhs.name, rhs, o)
        elif rhs is UNKNOWN:
            self._set(ctx.rhs.name, lhs, o)
        elif lhs is not rhs:
            raise TypeMismatchInStatement(ctx)

    def _set(self, name, value, env):
        for scope in env:
            if name in scope:
                scope[name] = value
                return

    def visitIntLit(self, ctx, o):
        return int

    def visitFloatLit(self, ctx, o):
        return float

    def visitBoolLit(self, ctx, o):
        return bool

    def visitId(self, ctx, o):
        value = find(ctx.name, o)
        if isinstance(value, FuncDecl):
            raise UndeclaredIdentifier(ctx.name)
        return value
