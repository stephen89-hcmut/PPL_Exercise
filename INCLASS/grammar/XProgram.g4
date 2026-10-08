grammar XProgram;

program: vardecl+ EOF;
vardecl: ids COLON typ;
ids: ID (CM ID)*;
typ: INTTYPE | FLOATTYPE;
COLON: ':';
CM: ',';
INTTYPE: 'int';
FLOATTYPE: 'float';
ID: [a-z]+;
WS: [ \t\r\n]+ -> skip;
