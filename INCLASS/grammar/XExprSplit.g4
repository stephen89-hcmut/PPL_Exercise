grammar XExprSplit;

exp: term (addop term)*;
addop: ADDOP | SUBOP;
term: (factor mulop)* factor;
mulop: MULOP | DIVOP;
factor: ID | INTLIT | '(' exp ')';
ADDOP: '+';
SUBOP: '-';
MULOP: '*';
DIVOP: '/';
ID: [a-z]+;
INTLIT: [0-9]+;
WS: [ \t\r\n]+ -> skip;
