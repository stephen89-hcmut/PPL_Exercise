# OOP 1 - Arithmetic expression eval

To express an arithmetic expression, there are 5 following classes:

Exp: general arithmetic expression

BinExp(left,op,right): an arithmetic expression that contains one binary operators (+,-,\*,/) and two operands

UnExp(op,operand): an arithmetic expression that contains one unary operator (+,-) and one operand

IntLit(val): an arithmetic expression that contains one integer number

FloatLit(val): an arithmetic expression that contains one floating point number

Define these classes in Python (their parents, attributes, methods) such that their objects can response to eval() message by returning the value of the expression. For example, let object x express the arithmetic expression 3 + 4 \* 2.0, x.eval() must return 11.0
