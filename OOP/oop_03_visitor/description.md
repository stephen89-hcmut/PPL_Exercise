# OOP 3 - Visitor pattern

As in the previous question, when a task is added into expression classes, new methods are added into these classes. Please change the way these classes are implemented in such a way that these classes do not change their contents when new tasks are added into these classes:

- Define class Eval to calculate the value of an expression
- Define class PrintPrefix to return the string corresponding to the expression in prefix format
- Define class PrintPostfix to return the string corresponding to the expression in postfix format

Let x be an object expressing an expression, x.accept(Eval()) will return the value of the expression x, x.accept(PrintPrefix()) will return the expression in prefix format and x.accept(PrintPostfix()) will return the expression in postfix format.

Be careful that you are not allowed to use type(), isinstance() when implementing this exercise

Tip: Use Visitor pattern.
