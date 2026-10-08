grammar XExprRecursive;

exp: exp ADDOP term | exp SUBOP term | term;
term: factor MULOP term | factor DIVOP term | factor;
factor: ID | INTLIT | '(' exp ')';
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
ID: [a-z]+;
INTLIT: [0-9]+;
WS: [ \t\r\n]+ -> skip;
