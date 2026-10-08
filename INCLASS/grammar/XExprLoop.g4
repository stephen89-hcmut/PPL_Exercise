grammar XExprLoop;

exp: term ((ADDOP | SUBOP) term)*;
term: (factor (MULOP | DIVOP))* factor;
factor: ID | INTLIT | '(' exp ')';
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
ID: [a-z]+;
INTLIT: [0-9]+;
WS: [ \t\r\n]+ -> skip;
