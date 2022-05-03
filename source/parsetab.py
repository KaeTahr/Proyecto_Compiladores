
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ATTRIBUTES CHAR CLASS COLON COMMA COMP CTEC CTEF CTEI CTES DIV DO DOT ELSE EQ FLOAT FROM FUNCTION GT GTE ID IF INHERITS INT LB LP LS LT LTE MAIN METHODS MIN MUL NE OR PLUS PROGRAM RB READ RETURN RP RS SEMI THEN UNTIL VARIABLES VOID WHILE WRITEprogram : PROGRAM ID SEMI prog1 prog2 prog3 mainprog1 : class\n             | emptyprog2 : vars\n             | emptyprog3 : function\n             | emptyclass : class class\n             | CLASS ID class1 LB class2 class3 RB SEMIclass1 : INHERITS ID\n              | emptyclass2 : attrs\n              | emptyclass3 : mthds\n              | emptyattrs : ATTRIBUTES attrs1attrs1 : lista_ids COLON tipo SEMI attrs2attrs2 : attrs1\n              | emptymthds : METHODS functionvars : VARIABLES attrs1tipo : tipo_param\n            | IDlista_ids : ID list1 list2list1 : LS CTEI RS\n             | LS CTEI COMMA CTEI RS\n             | emptylist2 : COMMA lista_ids\n             | emptymain : MAIN LP RP LB main1 RBmain1 : statement\n             | emptyfunction : function function\n                | tipo_retorno FUNCTION ID LP func1 RP LB func2 main1 RBfunc1 : params\n             | emptyfunc2 : vars\n             | emptytipo_param : INT\n                  | FLOAT\n                  | CHARparams : ID COLON tipo_param par1par1 : COMMA params\n            | emptytipo_retorno : tipo_param\n                    | VOIDstatement : statement statement\n                 | assignment SEMI\n                 | void_call SEMI\n                 | read SEMI\n                 | write SEMI\n                 | if_st\n                 | while_st\n                 | from_st\n                 | return_st SEMIassignment : var EQ expressionvar : ID list1\n           | ID DOT IDvoid_call : ID call1 LP func1 RPcall1 : DOT ID\n             | emptyread : READ LP var read1 RPread1 : COMMA var\n             | emptywrite : WRITE LP write1 RPwrite1 : expression write2\n              | CTES write2write2 : COMMA write1\n              | emptyif_st : IF LP expression RP THEN LB statement RB if1if1 : ELSE LB main1 RBwhile_st : WHILE LP expression RP DO LB main1 RBfrom_st : FROM ID list1 EQ expression UNTIL expression DO LB main1 RBreturn_st : RETURN LP expression RPexpression : exp\n                  | exp OR expexp : k_exp\n           | k_exp AND k_expk_exp : m_exp\n             | m_exp LT m_exp\n             | m_exp GT m_exp\n             | m_exp COMP m_exp\n             | m_exp NE m_exp\n             | m_exp LTE m_exp\n             | m_exp GTE m_expm_exp : term\n             | term PLUS term\n             | term MIN termterm : fact\n            | fact MUL fact\n            | fact DIV factfact : LP expression RP\n            | void_call\n            | var_cte\n            | varvar_cte : CTEI\n               | CTEF\n               | CTECempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,30,98,],[0,-1,-30,]),'ID':([2,8,12,24,28,33,34,46,52,54,55,64,69,70,71,76,82,83,84,92,99,100,101,102,103,104,105,108,110,111,112,113,115,117,125,131,143,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,163,165,168,173,199,200,201,202,206,208,210,211,214,215,],[3,14,26,-21,39,41,44,26,26,65,26,87,-17,-18,-19,87,-52,-53,-54,114,87,-48,-49,-50,-51,-55,87,132,134,87,87,87,87,-99,87,65,65,87,-37,-38,87,87,87,87,87,87,87,87,87,87,87,87,134,193,87,87,87,87,87,87,-72,-70,87,87,-73,-71,]),'SEMI':([3,21,22,23,42,43,44,57,73,78,79,80,81,85,87,96,107,109,118,119,120,121,122,123,124,126,127,128,129,130,132,166,174,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,],[4,-39,-40,-41,55,-22,-23,-25,97,100,101,102,103,104,-99,-26,-57,-27,-95,-56,-75,-77,-79,-86,-89,-93,-94,-96,-97,-98,-58,-65,-74,-76,-78,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,-92,-59,-62,]),'CLASS':([4,6,13,97,],[8,8,8,-9,]),'VARIABLES':([4,5,6,7,13,97,117,],[-99,12,-2,-3,-8,-9,12,]),'VOID':([4,5,6,7,9,10,11,13,16,24,32,55,62,69,70,71,74,97,198,],[-99,-99,-2,-3,20,-4,-5,-8,20,-21,20,-99,20,-17,-18,-19,20,-9,-34,]),'INT':([4,5,6,7,9,10,11,13,16,24,32,34,55,62,69,70,71,74,94,97,198,],[-99,-99,-2,-3,21,-4,-5,-8,21,-21,21,21,-99,21,-17,-18,-19,21,21,-9,-34,]),'FLOAT':([4,5,6,7,9,10,11,13,16,24,32,34,55,62,69,70,71,74,94,97,198,],[-99,-99,-2,-3,22,-4,-5,-8,22,-21,22,22,-99,22,-17,-18,-19,22,22,-9,-34,]),'CHAR':([4,5,6,7,9,10,11,13,16,24,32,34,55,62,69,70,71,74,94,97,198,],[-99,-99,-2,-3,23,-4,-5,-8,23,-21,23,23,-99,23,-17,-18,-19,23,23,-9,-34,]),'MAIN':([4,5,6,7,9,10,11,13,15,16,17,24,32,55,69,70,71,97,198,],[-99,-99,-2,-3,-99,-4,-5,-8,31,-6,-7,-21,-33,-99,-17,-18,-19,-9,-34,]),'INHERITS':([14,],[28,]),'LB':([14,27,29,39,53,95,195,196,207,209,],[-99,38,-11,-10,64,117,199,200,210,211,]),'FUNCTION':([18,19,20,21,22,23,],[33,-45,-46,-39,-40,-41,]),'COMMA':([21,22,23,26,35,37,48,57,87,96,107,109,116,118,120,121,122,123,124,126,127,128,129,130,132,133,134,136,137,177,178,179,180,181,182,183,184,185,186,187,188,189,190,193,],[-39,-40,-41,-99,46,-27,58,-25,-99,-26,-57,-27,143,-95,-75,-77,-79,-86,-89,-93,-94,-96,-97,-98,-58,163,-99,168,168,-76,-78,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,-92,-59,-58,]),'RP':([21,22,23,37,40,54,57,66,67,68,87,96,107,109,116,118,120,121,122,123,124,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,142,144,160,161,162,164,167,169,170,175,177,178,179,180,181,182,183,184,185,186,187,188,189,190,192,193,194,],[-39,-40,-41,-27,53,-99,-25,95,-35,-36,-99,-26,-57,-27,-99,-95,-75,-77,-79,-86,-89,-93,-94,-96,-97,-98,-99,-58,-99,-99,166,-99,-99,171,172,174,-42,-44,189,190,191,-64,-66,-69,-67,-43,-76,-78,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,-92,-59,-63,-58,-68,]),'READ':([24,55,64,69,70,71,76,82,83,84,99,100,101,102,103,104,117,145,146,147,199,200,202,206,208,210,211,214,215,],[-21,-99,88,-17,-18,-19,88,-52,-53,-54,88,-48,-49,-50,-51,-55,-99,88,-37,-38,88,88,88,-72,-70,88,88,-73,-71,]),'WRITE':([24,55,64,69,70,71,76,82,83,84,99,100,101,102,103,104,117,145,146,147,199,200,202,206,208,210,211,214,215,],[-21,-99,89,-17,-18,-19,89,-52,-53,-54,89,-48,-49,-50,-51,-55,-99,89,-37,-38,89,89,89,-72,-70,89,89,-73,-71,]),'IF':([24,55,64,69,70,71,76,82,83,84,99,100,101,102,103,104,117,145,146,147,199,200,202,206,208,210,211,214,215,],[-21,-99,90,-17,-18,-19,90,-52,-53,-54,90,-48,-49,-50,-51,-55,-99,90,-37,-38,90,90,90,-72,-70,90,90,-73,-71,]),'WHILE':([24,55,64,69,70,71,76,82,83,84,99,100,101,102,103,104,117,145,146,147,199,200,202,206,208,210,211,214,215,],[-21,-99,91,-17,-18,-19,91,-52,-53,-54,91,-48,-49,-50,-51,-55,-99,91,-37,-38,91,91,91,-72,-70,91,91,-73,-71,]),'FROM':([24,55,64,69,70,71,76,82,83,84,99,100,101,102,103,104,117,145,146,147,199,200,202,206,208,210,211,214,215,],[-21,-99,92,-17,-18,-19,92,-52,-53,-54,92,-48,-49,-50,-51,-55,-99,92,-37,-38,92,92,92,-72,-70,92,92,-73,-71,]),'RETURN':([24,55,64,69,70,71,76,82,83,84,99,100,101,102,103,104,117,145,146,147,199,200,202,206,208,210,211,214,215,],[-21,-99,93,-17,-18,-19,93,-52,-53,-54,93,-48,-49,-50,-51,-55,-99,93,-37,-38,93,93,93,-72,-70,93,93,-73,-71,]),'RB':([24,32,38,49,50,51,55,59,60,61,63,64,69,70,71,74,75,76,77,82,83,84,99,100,101,102,103,104,117,145,146,147,176,198,200,202,203,206,208,210,211,212,213,214,215,],[-21,-33,-99,-99,-12,-13,-99,73,-14,-15,-16,-99,-17,-18,-19,-20,98,-31,-32,-52,-53,-54,-47,-48,-49,-50,-51,-55,-99,-99,-37,-38,198,-34,-99,205,206,-72,-70,-99,-99,214,215,-73,-71,]),'COLON':([25,26,35,37,45,47,56,57,65,96,],[34,-99,-99,-27,-24,-29,-28,-25,94,-26,]),'LS':([26,87,114,134,],[36,36,36,36,]),'LP':([31,41,87,88,89,90,91,93,105,106,109,111,112,113,115,125,132,148,149,150,151,152,153,154,155,156,157,158,159,168,173,201,],[40,54,-99,110,111,112,113,115,125,131,-61,125,125,125,125,125,-60,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,]),'CTEI':([36,58,105,111,112,113,115,125,148,149,150,151,152,153,154,155,156,157,158,159,168,173,201,],[48,72,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,]),'EQ':([37,57,86,87,96,107,109,114,132,140,],[-27,-25,105,-99,-26,-57,-27,-99,-58,173,]),'ATTRIBUTES':([38,],[52,]),'METHODS':([38,49,50,51,55,63,69,70,71,],[-99,62,-12,-13,-99,-16,-17,-18,-19,]),'RS':([48,72,],[57,96,]),'MUL':([57,87,96,107,109,118,124,126,127,128,129,130,132,189,190,],[-25,-99,-26,-57,-27,-95,158,-93,-94,-96,-97,-98,-58,-92,-59,]),'DIV':([57,87,96,107,109,118,124,126,127,128,129,130,132,189,190,],[-25,-99,-26,-57,-27,-95,159,-93,-94,-96,-97,-98,-58,-92,-59,]),'PLUS':([57,87,96,107,109,118,123,124,126,127,128,129,130,132,187,188,189,190,],[-25,-99,-26,-57,-27,-95,156,-89,-93,-94,-96,-97,-98,-58,-90,-91,-92,-59,]),'MIN':([57,87,96,107,109,118,123,124,126,127,128,129,130,132,187,188,189,190,],[-25,-99,-26,-57,-27,-95,157,-89,-93,-94,-96,-97,-98,-58,-90,-91,-92,-59,]),'LT':([57,87,96,107,109,118,122,123,124,126,127,128,129,130,132,185,186,187,188,189,190,],[-25,-99,-26,-57,-27,-95,150,-86,-89,-93,-94,-96,-97,-98,-58,-87,-88,-90,-91,-92,-59,]),'GT':([57,87,96,107,109,118,122,123,124,126,127,128,129,130,132,185,186,187,188,189,190,],[-25,-99,-26,-57,-27,-95,151,-86,-89,-93,-94,-96,-97,-98,-58,-87,-88,-90,-91,-92,-59,]),'COMP':([57,87,96,107,109,118,122,123,124,126,127,128,129,130,132,185,186,187,188,189,190,],[-25,-99,-26,-57,-27,-95,152,-86,-89,-93,-94,-96,-97,-98,-58,-87,-88,-90,-91,-92,-59,]),'NE':([57,87,96,107,109,118,122,123,124,126,127,128,129,130,132,185,186,187,188,189,190,],[-25,-99,-26,-57,-27,-95,153,-86,-89,-93,-94,-96,-97,-98,-58,-87,-88,-90,-91,-92,-59,]),'LTE':([57,87,96,107,109,118,122,123,124,126,127,128,129,130,132,185,186,187,188,189,190,],[-25,-99,-26,-57,-27,-95,154,-86,-89,-93,-94,-96,-97,-98,-58,-87,-88,-90,-91,-92,-59,]),'GTE':([57,87,96,107,109,118,122,123,124,126,127,128,129,130,132,185,186,187,188,189,190,],[-25,-99,-26,-57,-27,-95,155,-86,-89,-93,-94,-96,-97,-98,-58,-87,-88,-90,-91,-92,-59,]),'AND':([57,87,96,107,109,118,121,122,123,124,126,127,128,129,130,132,179,180,181,182,183,184,185,186,187,188,189,190,],[-25,-99,-26,-57,-27,-95,149,-79,-86,-89,-93,-94,-96,-97,-98,-58,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,-92,-59,]),'OR':([57,87,96,107,109,118,120,121,122,123,124,126,127,128,129,130,132,178,179,180,181,182,183,184,185,186,187,188,189,190,],[-25,-99,-26,-57,-27,-95,148,-77,-79,-86,-89,-93,-94,-96,-97,-98,-58,-78,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,-92,-59,]),'UNTIL':([57,87,96,107,109,118,120,121,122,123,124,126,127,128,129,130,132,177,178,179,180,181,182,183,184,185,186,187,188,189,190,197,],[-25,-99,-26,-57,-27,-95,-75,-77,-79,-86,-89,-93,-94,-96,-97,-98,-58,-76,-78,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,-92,-59,201,]),'DO':([57,87,96,107,109,118,120,121,122,123,124,126,127,128,129,130,132,172,177,178,179,180,181,182,183,184,185,186,187,188,189,190,204,],[-25,-99,-26,-57,-27,-95,-75,-77,-79,-86,-89,-93,-94,-96,-97,-98,-58,196,-76,-78,-80,-81,-82,-83,-84,-85,-87,-88,-90,-91,-92,-59,207,]),'DOT':([87,134,],[108,165,]),'CTEF':([105,111,112,113,115,125,148,149,150,151,152,153,154,155,156,157,158,159,168,173,201,],[129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,]),'CTEC':([105,111,112,113,115,125,148,149,150,151,152,153,154,155,156,157,158,159,168,173,201,],[130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,]),'CTES':([111,168,],[137,137,]),'THEN':([171,],[195,]),'ELSE':([205,],[209,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'prog1':([4,],[5,]),'class':([4,6,13,],[6,13,13,]),'empty':([4,5,9,14,26,35,38,49,54,55,64,87,114,116,117,131,133,134,136,137,145,200,210,211,],[7,11,17,29,37,47,51,61,68,71,77,109,37,144,147,68,164,37,169,169,77,77,77,77,]),'prog2':([5,],[9,]),'vars':([5,117,],[10,146,]),'prog3':([9,],[15,]),'function':([9,16,32,62,74,],[16,32,32,74,32,]),'tipo_retorno':([9,16,32,62,74,],[18,18,18,18,18,]),'tipo_param':([9,16,32,34,62,74,94,],[19,19,19,43,19,19,116,]),'attrs1':([12,52,55,],[24,63,70,]),'lista_ids':([12,46,52,55,],[25,56,25,25,]),'class1':([14,],[27,]),'main':([15,],[30,]),'list1':([26,87,114,134,],[35,107,140,107,]),'tipo':([34,],[42,]),'list2':([35,],[45,]),'class2':([38,],[49,]),'attrs':([38,],[50,]),'class3':([49,],[59,]),'mthds':([49,],[60,]),'func1':([54,131,],[66,161,]),'params':([54,131,143,],[67,67,175,]),'attrs2':([55,],[69,]),'main1':([64,145,200,210,211,],[75,176,203,212,213,]),'statement':([64,76,99,145,199,200,202,210,211,],[76,99,99,76,202,76,99,76,76,]),'assignment':([64,76,99,145,199,200,202,210,211,],[78,78,78,78,78,78,78,78,78,]),'void_call':([64,76,99,105,111,112,113,115,125,145,148,149,150,151,152,153,154,155,156,157,158,159,168,173,199,200,201,202,210,211,],[79,79,79,126,126,126,126,126,126,79,126,126,126,126,126,126,126,126,126,126,126,126,126,126,79,79,126,79,79,79,]),'read':([64,76,99,145,199,200,202,210,211,],[80,80,80,80,80,80,80,80,80,]),'write':([64,76,99,145,199,200,202,210,211,],[81,81,81,81,81,81,81,81,81,]),'if_st':([64,76,99,145,199,200,202,210,211,],[82,82,82,82,82,82,82,82,82,]),'while_st':([64,76,99,145,199,200,202,210,211,],[83,83,83,83,83,83,83,83,83,]),'from_st':([64,76,99,145,199,200,202,210,211,],[84,84,84,84,84,84,84,84,84,]),'return_st':([64,76,99,145,199,200,202,210,211,],[85,85,85,85,85,85,85,85,85,]),'var':([64,76,99,105,110,111,112,113,115,125,145,148,149,150,151,152,153,154,155,156,157,158,159,163,168,173,199,200,201,202,210,211,],[86,86,86,118,133,118,118,118,118,118,86,118,118,118,118,118,118,118,118,118,118,118,118,192,118,118,86,86,118,86,86,86,]),'call1':([87,],[106,]),'expression':([105,111,112,113,115,125,168,173,201,],[119,136,138,139,141,160,136,197,204,]),'exp':([105,111,112,113,115,125,148,168,173,201,],[120,120,120,120,120,120,177,120,120,120,]),'k_exp':([105,111,112,113,115,125,148,149,168,173,201,],[121,121,121,121,121,121,121,178,121,121,121,]),'m_exp':([105,111,112,113,115,125,148,149,150,151,152,153,154,155,168,173,201,],[122,122,122,122,122,122,122,122,179,180,181,182,183,184,122,122,122,]),'term':([105,111,112,113,115,125,148,149,150,151,152,153,154,155,156,157,168,173,201,],[123,123,123,123,123,123,123,123,123,123,123,123,123,123,185,186,123,123,123,]),'fact':([105,111,112,113,115,125,148,149,150,151,152,153,154,155,156,157,158,159,168,173,201,],[124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,187,188,124,124,124,]),'var_cte':([105,111,112,113,115,125,148,149,150,151,152,153,154,155,156,157,158,159,168,173,201,],[127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,]),'write1':([111,168,],[135,194,]),'par1':([116,],[142,]),'func2':([117,],[145,]),'read1':([133,],[162,]),'write2':([136,137,],[167,170,]),'if1':([205,],[208,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMI prog1 prog2 prog3 main','program',7,'p_program','parser.py',7),
  ('prog1 -> class','prog1',1,'p_prog1','parser.py',11),
  ('prog1 -> empty','prog1',1,'p_prog1','parser.py',12),
  ('prog2 -> vars','prog2',1,'p_prog2','parser.py',15),
  ('prog2 -> empty','prog2',1,'p_prog2','parser.py',16),
  ('prog3 -> function','prog3',1,'p_prog3','parser.py',19),
  ('prog3 -> empty','prog3',1,'p_prog3','parser.py',20),
  ('class -> class class','class',2,'p_class','parser.py',24),
  ('class -> CLASS ID class1 LB class2 class3 RB SEMI','class',8,'p_class','parser.py',25),
  ('class1 -> INHERITS ID','class1',2,'p_class1','parser.py',28),
  ('class1 -> empty','class1',1,'p_class1','parser.py',29),
  ('class2 -> attrs','class2',1,'p_class2','parser.py',32),
  ('class2 -> empty','class2',1,'p_class2','parser.py',33),
  ('class3 -> mthds','class3',1,'p_class3','parser.py',36),
  ('class3 -> empty','class3',1,'p_class3','parser.py',37),
  ('attrs -> ATTRIBUTES attrs1','attrs',2,'p_attrs','parser.py',40),
  ('attrs1 -> lista_ids COLON tipo SEMI attrs2','attrs1',5,'p_attrs1','parser.py',43),
  ('attrs2 -> attrs1','attrs2',1,'p_attrs2','parser.py',46),
  ('attrs2 -> empty','attrs2',1,'p_attrs2','parser.py',47),
  ('mthds -> METHODS function','mthds',2,'p_mthds','parser.py',50),
  ('vars -> VARIABLES attrs1','vars',2,'p_vars','parser.py',54),
  ('tipo -> tipo_param','tipo',1,'p_tipo','parser.py',57),
  ('tipo -> ID','tipo',1,'p_tipo','parser.py',58),
  ('lista_ids -> ID list1 list2','lista_ids',3,'p_lista_ids','parser.py',61),
  ('list1 -> LS CTEI RS','list1',3,'p_list1','parser.py',64),
  ('list1 -> LS CTEI COMMA CTEI RS','list1',5,'p_list1','parser.py',65),
  ('list1 -> empty','list1',1,'p_list1','parser.py',66),
  ('list2 -> COMMA lista_ids','list2',2,'p_list2','parser.py',69),
  ('list2 -> empty','list2',1,'p_list2','parser.py',70),
  ('main -> MAIN LP RP LB main1 RB','main',6,'p_main','parser.py',74),
  ('main1 -> statement','main1',1,'p_main1','parser.py',77),
  ('main1 -> empty','main1',1,'p_main1','parser.py',78),
  ('function -> function function','function',2,'p_function','parser.py',82),
  ('function -> tipo_retorno FUNCTION ID LP func1 RP LB func2 main1 RB','function',10,'p_function','parser.py',83),
  ('func1 -> params','func1',1,'p_func1','parser.py',86),
  ('func1 -> empty','func1',1,'p_func1','parser.py',87),
  ('func2 -> vars','func2',1,'p_func2','parser.py',90),
  ('func2 -> empty','func2',1,'p_func2','parser.py',91),
  ('tipo_param -> INT','tipo_param',1,'p_tipo_param','parser.py',94),
  ('tipo_param -> FLOAT','tipo_param',1,'p_tipo_param','parser.py',95),
  ('tipo_param -> CHAR','tipo_param',1,'p_tipo_param','parser.py',96),
  ('params -> ID COLON tipo_param par1','params',4,'p_params','parser.py',99),
  ('par1 -> COMMA params','par1',2,'p_par1','parser.py',102),
  ('par1 -> empty','par1',1,'p_par1','parser.py',103),
  ('tipo_retorno -> tipo_param','tipo_retorno',1,'p_tipo_retorno','parser.py',106),
  ('tipo_retorno -> VOID','tipo_retorno',1,'p_tipo_retorno','parser.py',107),
  ('statement -> statement statement','statement',2,'p_statement','parser.py',111),
  ('statement -> assignment SEMI','statement',2,'p_statement','parser.py',112),
  ('statement -> void_call SEMI','statement',2,'p_statement','parser.py',113),
  ('statement -> read SEMI','statement',2,'p_statement','parser.py',114),
  ('statement -> write SEMI','statement',2,'p_statement','parser.py',115),
  ('statement -> if_st','statement',1,'p_statement','parser.py',116),
  ('statement -> while_st','statement',1,'p_statement','parser.py',117),
  ('statement -> from_st','statement',1,'p_statement','parser.py',118),
  ('statement -> return_st SEMI','statement',2,'p_statement','parser.py',119),
  ('assignment -> var EQ expression','assignment',3,'p_assignment','parser.py',123),
  ('var -> ID list1','var',2,'p_var','parser.py',126),
  ('var -> ID DOT ID','var',3,'p_var','parser.py',127),
  ('void_call -> ID call1 LP func1 RP','void_call',5,'p_void_call','parser.py',131),
  ('call1 -> DOT ID','call1',2,'p_call1','parser.py',134),
  ('call1 -> empty','call1',1,'p_call1','parser.py',135),
  ('read -> READ LP var read1 RP','read',5,'p_read','parser.py',139),
  ('read1 -> COMMA var','read1',2,'p_read1','parser.py',142),
  ('read1 -> empty','read1',1,'p_read1','parser.py',143),
  ('write -> WRITE LP write1 RP','write',4,'p_write','parser.py',147),
  ('write1 -> expression write2','write1',2,'p_write1','parser.py',150),
  ('write1 -> CTES write2','write1',2,'p_write1','parser.py',151),
  ('write2 -> COMMA write1','write2',2,'p_write2','parser.py',154),
  ('write2 -> empty','write2',1,'p_write2','parser.py',155),
  ('if_st -> IF LP expression RP THEN LB statement RB if1','if_st',9,'p_if_st','parser.py',159),
  ('if1 -> ELSE LB main1 RB','if1',4,'p_if1','parser.py',162),
  ('while_st -> WHILE LP expression RP DO LB main1 RB','while_st',8,'p_while_st','parser.py',166),
  ('from_st -> FROM ID list1 EQ expression UNTIL expression DO LB main1 RB','from_st',11,'p_from_st','parser.py',170),
  ('return_st -> RETURN LP expression RP','return_st',4,'p_return_st','parser.py',174),
  ('expression -> exp','expression',1,'p_expression','parser.py',178),
  ('expression -> exp OR exp','expression',3,'p_expression','parser.py',179),
  ('exp -> k_exp','exp',1,'p_exp','parser.py',182),
  ('exp -> k_exp AND k_exp','exp',3,'p_exp','parser.py',183),
  ('k_exp -> m_exp','k_exp',1,'p_k_exp','parser.py',186),
  ('k_exp -> m_exp LT m_exp','k_exp',3,'p_k_exp','parser.py',187),
  ('k_exp -> m_exp GT m_exp','k_exp',3,'p_k_exp','parser.py',188),
  ('k_exp -> m_exp COMP m_exp','k_exp',3,'p_k_exp','parser.py',189),
  ('k_exp -> m_exp NE m_exp','k_exp',3,'p_k_exp','parser.py',190),
  ('k_exp -> m_exp LTE m_exp','k_exp',3,'p_k_exp','parser.py',191),
  ('k_exp -> m_exp GTE m_exp','k_exp',3,'p_k_exp','parser.py',192),
  ('m_exp -> term','m_exp',1,'p_m_exp','parser.py',195),
  ('m_exp -> term PLUS term','m_exp',3,'p_m_exp','parser.py',196),
  ('m_exp -> term MIN term','m_exp',3,'p_m_exp','parser.py',197),
  ('term -> fact','term',1,'p_term','parser.py',200),
  ('term -> fact MUL fact','term',3,'p_term','parser.py',201),
  ('term -> fact DIV fact','term',3,'p_term','parser.py',202),
  ('fact -> LP expression RP','fact',3,'p_fact','parser.py',205),
  ('fact -> void_call','fact',1,'p_fact','parser.py',206),
  ('fact -> var_cte','fact',1,'p_fact','parser.py',207),
  ('fact -> var','fact',1,'p_fact','parser.py',208),
  ('var_cte -> CTEI','var_cte',1,'p_var_cte','parser.py',211),
  ('var_cte -> CTEF','var_cte',1,'p_var_cte','parser.py',212),
  ('var_cte -> CTEC','var_cte',1,'p_var_cte','parser.py',213),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',224),
]
