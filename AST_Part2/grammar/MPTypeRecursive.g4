grammar MPTypeRecursive;

program: mptype EOF;
mptype: primtype | arraytype;
arraytype: primtype dimens;
primtype: INTTYPE | FLOATTYPE;
dimens: dimen+;
dimen: '[' num '..' num ']';
num: '-'? INTLIT;

INTLIT: [0-9]+;
INTTYPE: 'integer';
FLOATTYPE: 'real';
WS: [ \t\r\n]+ -> skip;
