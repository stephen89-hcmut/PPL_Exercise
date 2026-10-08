grammar XIdsRecursive;

start: ids EOF;
ids: ID CM ids | ID;
CM: ',';
ID: [a-z]+;
WS: [ \t\r\n]+ -> skip;
