
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BEGIN BREAK ELSE END FLT FOR FUNCTION ID IF INT LET LOOP OR PRINT READ WHILE abrellave abreparentesis asignacion cierrallave cierraparentesis coma comillasdobles diferenteque dividir igualque mayor mayorigual menor menorigual multiplicacion num puntoycoma resta suma\n    Programa : V F Main\n    \n    V : LET aux asignacion K puntoycoma V\n    V : LET aux asignacion abreparentesis  A cierraparentesis puntoycoma V\n      |\n    \n    aux : type ID\n    \n    type : INT\n    type : FLT\n    \n    A : num\n    A : A coma num\n    \n    Main : BEGIN puntoycoma  Z END puntoycoma\n      |\n    \n    Z : S puntoycoma\n    Z : Z S puntoycoma\n    \n    K : ID\n    K : num\n    \n    F : F FUNCTION ID abrellave S cierrallave\n      |\n    \n    S : ID abreparentesis cierraparentesis\n    S : IF EL abrellave Z cierrallave ELSE abrellave Z cierrallave\n    S : READ abreparentesis ID abreparentesis A cierraparentesis cierraparentesis\n    S : PRINT abreparentesis M cierraparentesis\n    S : LET ID asignacion IF abreparentesis EL cierraparentesis abrellave Z cierrallave ELSE abrellave Z cierrallave\n    S : WHILE EL abrellave Z cierrallave\n    S : LOOP abrellave Z abreparentesis EL cierraparentesis B cierrallave \n    S : FOR abreparentesis LET type ID asignacion K  puntoycoma EL puntoycoma ID suma num cierraparentesis abrellave Z cierrallave\n    S : ID D asignacion E\n    S : BREAK\n      |\n    \n    B : abrellave BREAK cierrallave\n      |\n    \n    M : comillasdobles K comillasdobles\n    M : A\n    \n    D : abreparentesis A cierraparentesis\n      |\n    \n    E : expSuma\n    E : expResta\n    E : T\n    \n    expSuma : E suma T\n    \n    expResta : E resta T\n    \n    T : expMult\n    T : expDiv\n    T : X\n    \n    expMult : T multiplicacion X\n    \n    expDiv : T dividir X\n    \n    X : IDaux\n    X : ID abreparentesis A cierraparentesis\n    X : num\n    X : abreparentesis E cierraparentesis\n    \n    IDaux : ID\n    \n    EL : AL\n    EL : orAux\n    \n    AL : TL\n    AL : andAux\n    \n    orAux : EL OR AL\n    \n    andAux : AL AND TL\n    \n    TL : abreparentesis EL cierraparentesis\n    TL : Comp\n    \n    Comp : J W J\n    \n    J : ID abreparentesis A cierraparentesis\n    J : IDoux\n    J : num\n    \n    IDoux : ID\n    \n    W : mayorigual\n    W : menorigual\n    W : menor\n    W : mayor\n    W : igualque\n    W : diferenteque\n    '
    
_lr_action_items = {'LET':([0,15,20,21,32,38,56,57,63,67,84,85,87,101,111,141,147,148,153,160,162,166,167,],[3,27,27,27,3,-12,27,86,-13,27,27,27,3,27,27,27,27,27,27,27,27,27,27,]),'FUNCTION':([0,2,4,32,58,61,87,114,],[-4,-17,10,-4,-2,-16,-4,-3,]),'BEGIN':([0,2,4,32,58,61,87,114,],[-4,-17,11,-4,-2,-16,-4,-3,]),'$end':([0,1,2,4,9,32,58,61,62,87,114,],[-4,0,-17,-11,-1,-4,-2,-16,-10,-4,-3,]),'INT':([3,86,],[7,7,]),'FLT':([3,86,],[8,8,]),'asignacion':([5,13,23,40,54,89,128,],[12,-5,-34,66,83,-33,139,]),'ID':([6,7,8,10,12,15,20,21,24,27,28,38,46,52,56,63,66,67,68,69,71,72,73,74,75,76,77,81,84,85,99,101,111,112,113,116,117,118,119,125,139,141,147,148,151,153,157,160,162,166,167,],[13,-6,-7,14,18,23,23,23,49,54,49,-12,49,79,23,-13,90,23,49,49,49,-63,-64,-65,-66,-67,-68,18,23,23,90,23,23,49,128,90,90,90,90,49,18,23,23,23,49,23,159,23,23,23,23,]),'puntoycoma':([11,15,16,18,19,21,22,31,36,37,38,42,43,44,45,47,49,50,51,56,59,63,64,67,84,85,90,91,92,93,94,95,96,97,98,100,101,102,103,104,105,108,111,122,126,130,131,132,133,134,140,141,142,146,147,148,150,152,153,155,160,162,164,166,167,168,],[15,-28,32,-14,-15,-28,38,-27,62,63,-12,-50,-51,-52,-53,-57,-62,-60,-61,-28,87,-13,-18,-28,-28,-28,-49,-26,-35,-36,-37,-40,-41,-42,-45,-47,-28,-54,-55,-56,-58,-21,-28,-59,-23,-38,-39,-43,-44,-48,-46,-28,-20,151,-28,-28,-24,-19,-28,157,-28,-28,-22,-28,-28,-25,]),'abreparentesis':([12,23,24,25,26,28,30,38,46,49,63,66,68,69,79,85,90,99,110,112,116,117,118,119,125,151,],[17,39,46,52,53,46,57,-12,46,78,-13,99,46,46,107,112,115,99,125,46,99,99,99,99,46,46,]),'num':([12,17,24,28,39,46,53,60,66,68,69,71,72,73,74,75,76,77,78,81,99,107,112,115,116,117,118,119,125,139,151,161,],[19,34,51,51,34,51,34,88,100,51,51,51,-63,-64,-65,-66,-67,-68,34,19,100,34,51,34,100,100,100,100,51,19,51,163,]),'abrellave':([14,29,41,42,43,44,45,47,49,50,51,55,102,103,104,105,122,135,138,143,158,165,],[20,56,67,-50,-51,-52,-53,-57,-62,-60,-61,84,-54,-55,-56,-58,-59,141,144,148,160,166,]),'IF':([15,20,21,38,56,63,67,83,84,85,101,111,141,147,148,153,160,162,166,167,],[24,24,24,-12,24,-13,24,110,24,24,24,24,24,24,24,24,24,24,24,24,]),'READ':([15,20,21,38,56,63,67,84,85,101,111,141,147,148,153,160,162,166,167,],[25,25,25,-12,25,-13,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'PRINT':([15,20,21,38,56,63,67,84,85,101,111,141,147,148,153,160,162,166,167,],[26,26,26,-12,26,-13,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'WHILE':([15,20,21,38,56,63,67,84,85,101,111,141,147,148,153,160,162,166,167,],[28,28,28,-12,28,-13,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'LOOP':([15,20,21,38,56,63,67,84,85,101,111,141,147,148,153,160,162,166,167,],[29,29,29,-12,29,-13,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'FOR':([15,20,21,38,56,63,67,84,85,101,111,141,147,148,153,160,162,166,167,],[30,30,30,-12,30,-13,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'BREAK':([15,20,21,38,56,63,67,84,85,101,111,141,144,147,148,153,160,162,166,167,],[31,31,31,-12,31,-13,31,31,31,31,31,31,149,31,31,31,31,31,31,31,]),'comillasdobles':([18,19,53,109,],[-14,-15,81,124,]),'cierrallave':([20,31,35,38,63,64,90,91,92,93,94,95,96,97,98,100,101,108,111,126,130,131,132,133,134,138,140,142,145,147,149,150,152,153,154,162,164,167,168,],[-28,-27,61,-12,-13,-18,-49,-26,-35,-36,-37,-40,-41,-42,-45,-47,121,-21,126,-23,-38,-39,-43,-44,-48,-30,-46,-20,150,152,154,-24,-19,156,-29,164,-22,168,-25,]),'END':([21,38,63,],[36,-12,-13,]),'cierraparentesis':([33,34,39,42,43,44,45,47,49,50,51,65,70,80,82,88,90,92,93,94,95,96,97,98,100,102,103,104,105,106,120,122,123,124,127,129,130,131,132,133,134,136,137,140,163,],[59,-8,64,-50,-51,-52,-53,-57,-62,-60,-61,89,104,108,-32,-9,-49,-35,-36,-37,-40,-41,-42,-45,-47,-54,-55,-56,-58,122,134,-59,136,-31,138,140,-38,-39,-43,-44,-48,142,143,-46,165,]),'coma':([33,34,65,82,88,106,123,129,],[60,-8,60,60,-9,60,60,60,]),'OR':([41,42,43,44,45,47,49,50,51,55,70,102,103,104,105,122,127,137,155,],[68,-50,-51,-52,-53,-57,-62,-60,-61,68,68,-54,-55,-56,-58,-59,68,68,68,]),'AND':([42,44,45,47,49,50,51,102,103,104,105,122,],[69,-52,-53,-57,-62,-60,-61,69,-55,-56,-58,-59,]),'mayorigual':([48,49,50,51,122,],[72,-62,-60,-61,-59,]),'menorigual':([48,49,50,51,122,],[73,-62,-60,-61,-59,]),'menor':([48,49,50,51,122,],[74,-62,-60,-61,-59,]),'mayor':([48,49,50,51,122,],[75,-62,-60,-61,-59,]),'igualque':([48,49,50,51,122,],[76,-62,-60,-61,-59,]),'diferenteque':([48,49,50,51,122,],[77,-62,-60,-61,-59,]),'multiplicacion':([90,94,95,96,97,98,100,130,131,132,133,134,140,],[-49,118,-40,-41,-42,-45,-47,118,118,-43,-44,-48,-46,]),'dividir':([90,94,95,96,97,98,100,130,131,132,133,134,140,],[-49,119,-40,-41,-42,-45,-47,119,119,-43,-44,-48,-46,]),'suma':([90,91,92,93,94,95,96,97,98,100,120,130,131,132,133,134,140,159,],[-49,116,-35,-36,-37,-40,-41,-42,-45,-47,116,-38,-39,-43,-44,-48,-46,161,]),'resta':([90,91,92,93,94,95,96,97,98,100,120,130,131,132,133,134,140,],[-49,117,-35,-36,-37,-40,-41,-42,-45,-47,117,-38,-39,-43,-44,-48,-46,]),'ELSE':([121,156,],[135,158,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Programa':([0,],[1,]),'V':([0,32,87,],[2,58,114,]),'F':([2,],[4,]),'aux':([3,],[5,]),'type':([3,86,],[6,113,]),'Main':([4,],[9,]),'K':([12,81,139,],[16,109,146,]),'Z':([15,56,67,84,141,148,160,166,],[21,85,101,111,147,153,162,167,]),'S':([15,20,21,56,67,84,85,101,111,141,147,148,153,160,162,166,167,],[22,35,37,22,22,22,37,37,37,22,37,22,37,22,37,22,37,]),'A':([17,39,53,78,107,115,],[33,65,82,106,123,129,]),'D':([23,],[40,]),'EL':([24,28,46,112,125,151,],[41,55,70,127,137,155,]),'AL':([24,28,46,68,112,125,151,],[42,42,42,102,42,42,42,]),'orAux':([24,28,46,112,125,151,],[43,43,43,43,43,43,]),'TL':([24,28,46,68,69,112,125,151,],[44,44,44,44,103,44,44,44,]),'andAux':([24,28,46,68,112,125,151,],[45,45,45,45,45,45,45,]),'Comp':([24,28,46,68,69,112,125,151,],[47,47,47,47,47,47,47,47,]),'J':([24,28,46,68,69,71,112,125,151,],[48,48,48,48,48,105,48,48,48,]),'IDoux':([24,28,46,68,69,71,112,125,151,],[50,50,50,50,50,50,50,50,50,]),'W':([48,],[71,]),'M':([53,],[80,]),'E':([66,99,],[91,120,]),'expSuma':([66,99,],[92,92,]),'expResta':([66,99,],[93,93,]),'T':([66,99,116,117,],[94,94,130,131,]),'expMult':([66,99,116,117,],[95,95,95,95,]),'expDiv':([66,99,116,117,],[96,96,96,96,]),'X':([66,99,116,117,118,119,],[97,97,97,97,132,133,]),'IDaux':([66,99,116,117,118,119,],[98,98,98,98,98,98,]),'B':([138,],[145,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Programa","S'",1,None,None,None),
  ('Programa -> V F Main','Programa',3,'p_Programa','anLexSin.py',191),
  ('V -> LET aux asignacion K puntoycoma V','V',6,'p_V','anLexSin.py',199),
  ('V -> LET aux asignacion abreparentesis A cierraparentesis puntoycoma V','V',8,'p_V','anLexSin.py',200),
  ('V -> <empty>','V',0,'p_V','anLexSin.py',201),
  ('aux -> type ID','aux',2,'p_aux','anLexSin.py',205),
  ('type -> INT','type',1,'p_type','anLexSin.py',214),
  ('type -> FLT','type',1,'p_type','anLexSin.py',215),
  ('A -> num','A',1,'p_A','anLexSin.py',224),
  ('A -> A coma num','A',3,'p_A','anLexSin.py',225),
  ('Main -> BEGIN puntoycoma Z END puntoycoma','Main',5,'p_Main','anLexSin.py',231),
  ('Main -> <empty>','Main',0,'p_Main','anLexSin.py',232),
  ('Z -> S puntoycoma','Z',2,'p_Z','anLexSin.py',238),
  ('Z -> Z S puntoycoma','Z',3,'p_Z','anLexSin.py',239),
  ('K -> ID','K',1,'p_K','anLexSin.py',245),
  ('K -> num','K',1,'p_K','anLexSin.py',246),
  ('F -> F FUNCTION ID abrellave S cierrallave','F',6,'p_F','anLexSin.py',253),
  ('F -> <empty>','F',0,'p_F','anLexSin.py',254),
  ('S -> ID abreparentesis cierraparentesis','S',3,'p_S','anLexSin.py',259),
  ('S -> IF EL abrellave Z cierrallave ELSE abrellave Z cierrallave','S',9,'p_S','anLexSin.py',260),
  ('S -> READ abreparentesis ID abreparentesis A cierraparentesis cierraparentesis','S',7,'p_S','anLexSin.py',261),
  ('S -> PRINT abreparentesis M cierraparentesis','S',4,'p_S','anLexSin.py',262),
  ('S -> LET ID asignacion IF abreparentesis EL cierraparentesis abrellave Z cierrallave ELSE abrellave Z cierrallave','S',14,'p_S','anLexSin.py',263),
  ('S -> WHILE EL abrellave Z cierrallave','S',5,'p_S','anLexSin.py',264),
  ('S -> LOOP abrellave Z abreparentesis EL cierraparentesis B cierrallave','S',8,'p_S','anLexSin.py',265),
  ('S -> FOR abreparentesis LET type ID asignacion K puntoycoma EL puntoycoma ID suma num cierraparentesis abrellave Z cierrallave','S',17,'p_S','anLexSin.py',266),
  ('S -> ID D asignacion E','S',4,'p_S','anLexSin.py',267),
  ('S -> BREAK','S',1,'p_S','anLexSin.py',268),
  ('S -> <empty>','S',0,'p_S','anLexSin.py',269),
  ('B -> abrellave BREAK cierrallave','B',3,'p_B','anLexSin.py',275),
  ('B -> <empty>','B',0,'p_B','anLexSin.py',276),
  ('M -> comillasdobles K comillasdobles','M',3,'p_M','anLexSin.py',283),
  ('M -> A','M',1,'p_M','anLexSin.py',284),
  ('D -> abreparentesis A cierraparentesis','D',3,'p_D','anLexSin.py',291),
  ('D -> <empty>','D',0,'p_D','anLexSin.py',292),
  ('E -> expSuma','E',1,'p_E','anLexSin.py',299),
  ('E -> expResta','E',1,'p_E','anLexSin.py',300),
  ('E -> T','E',1,'p_E','anLexSin.py',301),
  ('expSuma -> E suma T','expSuma',3,'p_expSuma','anLexSin.py',306),
  ('expResta -> E resta T','expResta',3,'p_expResta','anLexSin.py',312),
  ('T -> expMult','T',1,'p_T','anLexSin.py',322),
  ('T -> expDiv','T',1,'p_T','anLexSin.py',323),
  ('T -> X','T',1,'p_T','anLexSin.py',324),
  ('expMult -> T multiplicacion X','expMult',3,'p_expMult','anLexSin.py',329),
  ('expDiv -> T dividir X','expDiv',3,'p_expDiv','anLexSin.py',335),
  ('X -> IDaux','X',1,'p_X','anLexSin.py',346),
  ('X -> ID abreparentesis A cierraparentesis','X',4,'p_X','anLexSin.py',347),
  ('X -> num','X',1,'p_X','anLexSin.py',348),
  ('X -> abreparentesis E cierraparentesis','X',3,'p_X','anLexSin.py',349),
  ('IDaux -> ID','IDaux',1,'p_IDaux','anLexSin.py',353),
  ('EL -> AL','EL',1,'p_EL','anLexSin.py',365),
  ('EL -> orAux','EL',1,'p_EL','anLexSin.py',366),
  ('AL -> TL','AL',1,'p_AL','anLexSin.py',370),
  ('AL -> andAux','AL',1,'p_AL','anLexSin.py',371),
  ('orAux -> EL OR AL','orAux',3,'p_orAux','anLexSin.py',377),
  ('andAux -> AL AND TL','andAux',3,'p_andAux','anLexSin.py',383),
  ('TL -> abreparentesis EL cierraparentesis','TL',3,'p_TL','anLexSin.py',391),
  ('TL -> Comp','TL',1,'p_TL','anLexSin.py',392),
  ('Comp -> J W J','Comp',3,'p_Comp','anLexSin.py',397),
  ('J -> ID abreparentesis A cierraparentesis','J',4,'p_J','anLexSin.py',407),
  ('J -> IDoux','J',1,'p_J','anLexSin.py',408),
  ('J -> num','J',1,'p_J','anLexSin.py',409),
  ('IDoux -> ID','IDoux',1,'p_IDoux','anLexSin.py',413),
  ('W -> mayorigual','W',1,'p_W','anLexSin.py',422),
  ('W -> menorigual','W',1,'p_W','anLexSin.py',423),
  ('W -> menor','W',1,'p_W','anLexSin.py',424),
  ('W -> mayor','W',1,'p_W','anLexSin.py',425),
  ('W -> igualque','W',1,'p_W','anLexSin.py',426),
  ('W -> diferenteque','W',1,'p_W','anLexSin.py',427),
]
