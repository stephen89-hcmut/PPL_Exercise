grammar XIdsLoop;

ids: ID (CM ID)*;
CM: ',';
ID: [a-z]+;
WS: [ \t\r\n]+ -> skip;
