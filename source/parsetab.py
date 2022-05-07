
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ATTRIBUTES CHAR CLASS COLON COMMA COMP CTEC CTEF CTEI CTES DIV DO DOT ELSE EQ FLOAT FROM FUNCTION GT GTE ID IF INHERITS INT LB LP LS LT LTE MAIN METHODS MIN MUL NE OR PLUS PROGRAM RB READ RETURN RP RS SEMI THEN UNTIL VARIABLES VOID WHILE WRITEprogram : PROGRAM ID store_program SEMI prog1 prog2 prog3 mainstore_program :prog1 : class\n             | emptyprog2 : vars\n             | emptyprog3 : function\n             | emptyclass : class class\n             | CLASS ID class1 LB class2 class3 RB SEMIclass1 : INHERITS ID\n              | emptyclass2 : attrs\n              | emptyclass3 : mthds\n              | emptyattrs : ATTRIBUTES attrs1attrs1 : lista_ids COLON tipo SEMI attrs2attrs2 : attrs1\n              | emptymthds : METHODS functionvars : VARIABLES attrs1tipo : tipo_param\n            | IDlista_ids : ID list1 list2list1 : LS CTEI RS\n             | LS CTEI COMMA CTEI RS\n             | emptylist2 : COMMA lista_ids\n             | emptymain : MAIN LP RP LB main1 RBmain1 : statement\n             | emptyfunction : function function\n                | tipo_retorno FUNCTION ID store_function LP func1 RP LB func2 main1 RBstore_function :func1 : params\n             | emptyfunc2 : vars\n             | emptytipo_param : INT\n                  | FLOAT\n                  | CHARparams : ID COLON tipo_param par1par1 : COMMA params\n            | emptytipo_retorno : tipo_param\n                    | VOIDstatement : statement statement\n                 | assignment SEMI\n                 | void_call SEMI\n                 | read SEMI\n                 | write SEMI\n                 | if_st\n                 | while_st\n                 | from_st\n                 | return_st SEMIassignment : var EQ expressionvar : ID list1\n           | ID DOT IDvoid_call : ID call1 LP call2 RP\n                 | ID call1 LP RPcall1 : DOT ID\n             | emptycall2 : expression\n             | call2 COMMA call2read : READ LP var read1 RPread1 : COMMA var\n             | emptywrite : WRITE LP write1 RPwrite1 : expression write2\n              | CTES write2write2 : COMMA write1\n              | emptyif_st : IF LP expression RP THEN LB statement RB if1if1 : ELSE LB main1 RB\n           | emptywhile_st : WHILE LP expression RP DO LB main1 RBfrom_st : FROM ID list1 EQ expression UNTIL expression DO LB main1 RBreturn_st : RETURN LP expression RPexpression : exp\n                  | exp OR expexp : k_exp\n           | k_exp AND k_expk_exp : m_exp\n             | m_exp LT m_exp\n             | m_exp GT m_exp\n             | m_exp COMP m_exp\n             | m_exp NE m_exp\n             | m_exp LTE m_exp\n             | m_exp GTE m_expm_exp : term\n             | term PLUS term\n             | term MIN termterm : fact\n            | fact MUL fact\n            | fact DIV factfact : LP expression RP\n            | void_call\n            | var_cte\n            | varvar_cte : CTEI\n               | CTEF\n               | CTECempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,31,98,],[0,-1,-31,]),'ID':([2,9,13,25,29,34,35,47,53,56,65,66,67,68,69,74,80,81,82,90,99,100,101,102,103,104,105,108,110,111,112,113,115,125,131,143,144,145,146,147,148,149,150,151,152,153,154,155,161,163,166,171,174,176,177,178,193,204,205,206,208,211,212,214,216,217,218,221,222,],[3,15,27,-22,40,42,45,27,27,27,85,92,-18,-19,-20,85,-54,-55,-56,114,85,-50,-51,-52,-53,-57,85,132,134,85,85,85,85,85,85,-105,85,85,85,85,85,85,85,85,85,85,85,85,134,196,85,85,92,85,-39,-40,85,85,85,85,85,-105,-78,-75,-77,85,85,-79,-76,]),'SEMI':([3,4,22,23,24,43,44,45,58,71,76,77,78,79,83,85,96,107,109,118,119,120,121,122,123,124,126,127,128,129,130,132,158,164,172,179,180,181,182,183,184,185,186,187,188,189,190,191,192,194,],[-2,5,-41,-42,-43,56,-23,-24,-26,97,100,101,102,103,104,-105,-27,-59,-28,-101,-58,-81,-83,-85,-92,-95,-99,-100,-102,-103,-104,-60,-62,-70,-80,-82,-84,-86,-87,-88,-89,-90,-91,-93,-94,-96,-97,-98,-61,-67,]),'CLASS':([5,7,14,97,],[9,9,9,-10,]),'VARIABLES':([5,6,7,8,14,97,143,],[-105,13,-3,-4,-9,-10,13,]),'VOID':([5,6,7,8,10,11,12,14,17,25,33,56,63,67,68,69,72,97,207,],[-105,-105,-3,-4,21,-5,-6,-9,21,-22,21,-105,21,-18,-19,-20,21,-10,-35,]),'INT':([5,6,7,8,10,11,12,14,17,25,33,35,56,63,67,68,69,72,97,116,207,],[-105,-105,-3,-4,22,-5,-6,-9,22,-22,22,22,-105,22,-18,-19,-20,22,-10,22,-35,]),'FLOAT':([5,6,7,8,10,11,12,14,17,25,33,35,56,63,67,68,69,72,97,116,207,],[-105,-105,-3,-4,23,-5,-6,-9,23,-22,23,23,-105,23,-18,-19,-20,23,-10,23,-35,]),'CHAR':([5,6,7,8,10,11,12,14,17,25,33,35,56,63,67,68,69,72,97,116,207,],[-105,-105,-3,-4,24,-5,-6,-9,24,-22,24,24,-105,24,-18,-19,-20,24,-10,24,-35,]),'MAIN':([5,6,7,8,10,11,12,14,16,17,18,25,33,56,67,68,69,97,207,],[-105,-105,-3,-4,-105,-5,-6,-9,32,-7,-8,-22,-34,-105,-18,-19,-20,-10,-35,]),'INHERITS':([15,],[29,]),'LB':([15,28,30,40,54,117,198,199,213,215,],[-105,39,-12,-11,65,143,204,205,217,218,]),'FUNCTION':([19,20,21,22,23,24,],[34,-47,-48,-41,-42,-43,]),'COMMA':([22,23,24,27,36,38,49,58,85,96,107,109,118,120,121,122,123,124,126,127,128,129,130,132,133,134,136,137,142,157,158,159,179,180,181,182,183,184,185,186,187,188,189,190,191,192,196,203,],[-41,-42,-43,-105,47,-28,59,-26,-105,-27,-59,-28,-101,-81,-83,-85,-92,-95,-99,-100,-102,-103,-104,-60,161,-105,166,166,174,193,-62,-65,-82,-84,-86,-87,-88,-89,-90,-91,-93,-94,-96,-97,-98,-61,-60,193,]),'RP':([22,23,24,38,41,58,66,85,93,94,95,96,107,109,118,120,121,122,123,124,126,127,128,129,130,131,132,133,134,135,136,137,138,139,141,142,156,157,158,159,160,162,165,167,168,173,175,179,180,181,182,183,184,185,186,187,188,189,190,191,192,195,196,197,201,203,],[-41,-42,-43,-28,54,-26,-105,-105,117,-37,-38,-27,-59,-28,-101,-81,-83,-85,-92,-95,-99,-100,-102,-103,-104,158,-60,-105,-105,164,-105,-105,169,170,172,-105,191,192,-62,-65,194,-69,-71,-74,-72,-44,-46,-82,-84,-86,-87,-88,-89,-90,-91,-93,-94,-96,-97,-98,-61,-68,-60,-73,-45,-66,]),'READ':([25,56,65,67,68,69,74,80,81,82,99,100,101,102,103,104,143,176,177,178,204,205,208,211,212,214,216,217,218,221,222,],[-22,-105,86,-18,-19,-20,86,-54,-55,-56,86,-50,-51,-52,-53,-57,-105,86,-39,-40,86,86,86,-105,-78,-75,-77,86,86,-79,-76,]),'WRITE':([25,56,65,67,68,69,74,80,81,82,99,100,101,102,103,104,143,176,177,178,204,205,208,211,212,214,216,217,218,221,222,],[-22,-105,87,-18,-19,-20,87,-54,-55,-56,87,-50,-51,-52,-53,-57,-105,87,-39,-40,87,87,87,-105,-78,-75,-77,87,87,-79,-76,]),'IF':([25,56,65,67,68,69,74,80,81,82,99,100,101,102,103,104,143,176,177,178,204,205,208,211,212,214,216,217,218,221,222,],[-22,-105,88,-18,-19,-20,88,-54,-55,-56,88,-50,-51,-52,-53,-57,-105,88,-39,-40,88,88,88,-105,-78,-75,-77,88,88,-79,-76,]),'WHILE':([25,56,65,67,68,69,74,80,81,82,99,100,101,102,103,104,143,176,177,178,204,205,208,211,212,214,216,217,218,221,222,],[-22,-105,89,-18,-19,-20,89,-54,-55,-56,89,-50,-51,-52,-53,-57,-105,89,-39,-40,89,89,89,-105,-78,-75,-77,89,89,-79,-76,]),'FROM':([25,56,65,67,68,69,74,80,81,82,99,100,101,102,103,104,143,176,177,178,204,205,208,211,212,214,216,217,218,221,222,],[-22,-105,90,-18,-19,-20,90,-54,-55,-56,90,-50,-51,-52,-53,-57,-105,90,-39,-40,90,90,90,-105,-78,-75,-77,90,90,-79,-76,]),'RETURN':([25,56,65,67,68,69,74,80,81,82,99,100,101,102,103,104,143,176,177,178,204,205,208,211,212,214,216,217,218,221,222,],[-22,-105,91,-18,-19,-20,91,-54,-55,-56,91,-50,-51,-52,-53,-57,-105,91,-39,-40,91,91,91,-105,-78,-75,-77,91,91,-79,-76,]),'RB':([25,33,39,50,51,52,56,60,61,62,64,65,67,68,69,72,73,74,75,80,81,82,99,100,101,102,103,104,143,176,177,178,202,205,207,208,209,211,212,214,216,217,218,219,220,221,222,],[-22,-34,-105,-105,-13,-14,-105,71,-15,-16,-17,-105,-18,-19,-20,-21,98,-32,-33,-54,-55,-56,-49,-50,-51,-52,-53,-57,-105,-105,-39,-40,207,-105,-35,211,212,-105,-78,-75,-77,-105,-105,221,222,-79,-76,]),'COLON':([26,27,36,38,46,48,57,58,92,96,],[35,-105,-105,-28,-25,-30,-29,-26,116,-27,]),'LS':([27,85,114,134,],[37,37,37,37,]),'LP':([32,42,55,85,86,87,88,89,91,105,106,109,111,112,113,115,125,131,132,144,145,146,147,148,149,150,151,152,153,154,155,166,171,193,206,],[41,-36,66,-105,110,111,112,113,115,125,131,-64,125,125,125,125,125,125,-63,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,125,]),'CTEI':([37,59,105,111,112,113,115,125,131,144,145,146,147,148,149,150,151,152,153,154,155,166,171,193,206,],[49,70,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,128,]),'EQ':([38,58,84,85,96,107,109,114,132,140,],[-28,-26,105,-105,-27,-59,-28,-105,-60,171,]),'ATTRIBUTES':([39,],[53,]),'METHODS':([39,50,51,52,56,64,67,68,69,],[-105,63,-13,-14,-105,-17,-18,-19,-20,]),'RS':([49,70,],[58,96,]),'MUL':([58,85,96,107,109,118,124,126,127,128,129,130,132,158,191,192,],[-26,-105,-27,-59,-28,-101,154,-99,-100,-102,-103,-104,-60,-62,-98,-61,]),'DIV':([58,85,96,107,109,118,124,126,127,128,129,130,132,158,191,192,],[-26,-105,-27,-59,-28,-101,155,-99,-100,-102,-103,-104,-60,-62,-98,-61,]),'PLUS':([58,85,96,107,109,118,123,124,126,127,128,129,130,132,158,189,190,191,192,],[-26,-105,-27,-59,-28,-101,152,-95,-99,-100,-102,-103,-104,-60,-62,-96,-97,-98,-61,]),'MIN':([58,85,96,107,109,118,123,124,126,127,128,129,130,132,158,189,190,191,192,],[-26,-105,-27,-59,-28,-101,153,-95,-99,-100,-102,-103,-104,-60,-62,-96,-97,-98,-61,]),'LT':([58,85,96,107,109,118,122,123,124,126,127,128,129,130,132,158,187,188,189,190,191,192,],[-26,-105,-27,-59,-28,-101,146,-92,-95,-99,-100,-102,-103,-104,-60,-62,-93,-94,-96,-97,-98,-61,]),'GT':([58,85,96,107,109,118,122,123,124,126,127,128,129,130,132,158,187,188,189,190,191,192,],[-26,-105,-27,-59,-28,-101,147,-92,-95,-99,-100,-102,-103,-104,-60,-62,-93,-94,-96,-97,-98,-61,]),'COMP':([58,85,96,107,109,118,122,123,124,126,127,128,129,130,132,158,187,188,189,190,191,192,],[-26,-105,-27,-59,-28,-101,148,-92,-95,-99,-100,-102,-103,-104,-60,-62,-93,-94,-96,-97,-98,-61,]),'NE':([58,85,96,107,109,118,122,123,124,126,127,128,129,130,132,158,187,188,189,190,191,192,],[-26,-105,-27,-59,-28,-101,149,-92,-95,-99,-100,-102,-103,-104,-60,-62,-93,-94,-96,-97,-98,-61,]),'LTE':([58,85,96,107,109,118,122,123,124,126,127,128,129,130,132,158,187,188,189,190,191,192,],[-26,-105,-27,-59,-28,-101,150,-92,-95,-99,-100,-102,-103,-104,-60,-62,-93,-94,-96,-97,-98,-61,]),'GTE':([58,85,96,107,109,118,122,123,124,126,127,128,129,130,132,158,187,188,189,190,191,192,],[-26,-105,-27,-59,-28,-101,151,-92,-95,-99,-100,-102,-103,-104,-60,-62,-93,-94,-96,-97,-98,-61,]),'AND':([58,85,96,107,109,118,121,122,123,124,126,127,128,129,130,132,158,181,182,183,184,185,186,187,188,189,190,191,192,],[-26,-105,-27,-59,-28,-101,145,-85,-92,-95,-99,-100,-102,-103,-104,-60,-62,-86,-87,-88,-89,-90,-91,-93,-94,-96,-97,-98,-61,]),'OR':([58,85,96,107,109,118,120,121,122,123,124,126,127,128,129,130,132,158,180,181,182,183,184,185,186,187,188,189,190,191,192,],[-26,-105,-27,-59,-28,-101,144,-83,-85,-92,-95,-99,-100,-102,-103,-104,-60,-62,-84,-86,-87,-88,-89,-90,-91,-93,-94,-96,-97,-98,-61,]),'UNTIL':([58,85,96,107,109,118,120,121,122,123,124,126,127,128,129,130,132,158,179,180,181,182,183,184,185,186,187,188,189,190,191,192,200,],[-26,-105,-27,-59,-28,-101,-81,-83,-85,-92,-95,-99,-100,-102,-103,-104,-60,-62,-82,-84,-86,-87,-88,-89,-90,-91,-93,-94,-96,-97,-98,-61,206,]),'DO':([58,85,96,107,109,118,120,121,122,123,124,126,127,128,129,130,132,158,170,179,180,181,182,183,184,185,186,187,188,189,190,191,192,210,],[-26,-105,-27,-59,-28,-101,-81,-83,-85,-92,-95,-99,-100,-102,-103,-104,-60,-62,199,-82,-84,-86,-87,-88,-89,-90,-91,-93,-94,-96,-97,-98,-61,213,]),'DOT':([85,134,],[108,163,]),'CTEF':([105,111,112,113,115,125,131,144,145,146,147,148,149,150,151,152,153,154,155,166,171,193,206,],[129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,129,]),'CTEC':([105,111,112,113,115,125,131,144,145,146,147,148,149,150,151,152,153,154,155,166,171,193,206,],[130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,130,]),'CTES':([111,166,],[137,137,]),'THEN':([169,],[198,]),'ELSE':([211,],[215,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'store_program':([3,],[4,]),'prog1':([5,],[6,]),'class':([5,7,14,],[7,14,14,]),'empty':([5,6,10,15,27,36,39,50,56,65,66,85,114,133,134,136,137,142,143,176,205,211,217,218,],[8,12,18,30,38,48,52,62,69,75,95,109,38,162,38,167,167,175,178,75,75,216,75,75,]),'prog2':([6,],[10,]),'vars':([6,143,],[11,177,]),'prog3':([10,],[16,]),'function':([10,17,33,63,72,],[17,33,33,72,33,]),'tipo_retorno':([10,17,33,63,72,],[19,19,19,19,19,]),'tipo_param':([10,17,33,35,63,72,116,],[20,20,20,44,20,20,142,]),'attrs1':([13,53,56,],[25,64,68,]),'lista_ids':([13,47,53,56,],[26,57,26,26,]),'class1':([15,],[28,]),'main':([16,],[31,]),'list1':([27,85,114,134,],[36,107,140,107,]),'tipo':([35,],[43,]),'list2':([36,],[46,]),'class2':([39,],[50,]),'attrs':([39,],[51,]),'store_function':([42,],[55,]),'class3':([50,],[60,]),'mthds':([50,],[61,]),'attrs2':([56,],[67,]),'main1':([65,176,205,217,218,],[73,202,209,219,220,]),'statement':([65,74,99,176,204,205,208,217,218,],[74,99,99,74,208,74,99,74,74,]),'assignment':([65,74,99,176,204,205,208,217,218,],[76,76,76,76,76,76,76,76,76,]),'void_call':([65,74,99,105,111,112,113,115,125,131,144,145,146,147,148,149,150,151,152,153,154,155,166,171,176,193,204,205,206,208,217,218,],[77,77,77,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,126,77,126,77,77,126,77,77,77,]),'read':([65,74,99,176,204,205,208,217,218,],[78,78,78,78,78,78,78,78,78,]),'write':([65,74,99,176,204,205,208,217,218,],[79,79,79,79,79,79,79,79,79,]),'if_st':([65,74,99,176,204,205,208,217,218,],[80,80,80,80,80,80,80,80,80,]),'while_st':([65,74,99,176,204,205,208,217,218,],[81,81,81,81,81,81,81,81,81,]),'from_st':([65,74,99,176,204,205,208,217,218,],[82,82,82,82,82,82,82,82,82,]),'return_st':([65,74,99,176,204,205,208,217,218,],[83,83,83,83,83,83,83,83,83,]),'var':([65,74,99,105,110,111,112,113,115,125,131,144,145,146,147,148,149,150,151,152,153,154,155,161,166,171,176,193,204,205,206,208,217,218,],[84,84,84,118,133,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,118,195,118,118,84,118,84,84,118,84,84,84,]),'func1':([66,],[93,]),'params':([66,174,],[94,201,]),'call1':([85,],[106,]),'expression':([105,111,112,113,115,125,131,166,171,193,206,],[119,136,138,139,141,156,159,136,200,159,210,]),'exp':([105,111,112,113,115,125,131,144,166,171,193,206,],[120,120,120,120,120,120,120,179,120,120,120,120,]),'k_exp':([105,111,112,113,115,125,131,144,145,166,171,193,206,],[121,121,121,121,121,121,121,121,180,121,121,121,121,]),'m_exp':([105,111,112,113,115,125,131,144,145,146,147,148,149,150,151,166,171,193,206,],[122,122,122,122,122,122,122,122,122,181,182,183,184,185,186,122,122,122,122,]),'term':([105,111,112,113,115,125,131,144,145,146,147,148,149,150,151,152,153,166,171,193,206,],[123,123,123,123,123,123,123,123,123,123,123,123,123,123,123,187,188,123,123,123,123,]),'fact':([105,111,112,113,115,125,131,144,145,146,147,148,149,150,151,152,153,154,155,166,171,193,206,],[124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,124,189,190,124,124,124,124,]),'var_cte':([105,111,112,113,115,125,131,144,145,146,147,148,149,150,151,152,153,154,155,166,171,193,206,],[127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,127,]),'write1':([111,166,],[135,197,]),'call2':([131,193,],[157,203,]),'read1':([133,],[160,]),'write2':([136,137,],[165,168,]),'par1':([142,],[173,]),'func2':([143,],[176,]),'if1':([211,],[214,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID store_program SEMI prog1 prog2 prog3 main','program',8,'p_program','parser.py',10),
  ('store_program -> <empty>','store_program',0,'p_store_program','parser.py',14),
  ('prog1 -> class','prog1',1,'p_prog1','parser.py',18),
  ('prog1 -> empty','prog1',1,'p_prog1','parser.py',19),
  ('prog2 -> vars','prog2',1,'p_prog2','parser.py',23),
  ('prog2 -> empty','prog2',1,'p_prog2','parser.py',24),
  ('prog3 -> function','prog3',1,'p_prog3','parser.py',28),
  ('prog3 -> empty','prog3',1,'p_prog3','parser.py',29),
  ('class -> class class','class',2,'p_class','parser.py',34),
  ('class -> CLASS ID class1 LB class2 class3 RB SEMI','class',8,'p_class','parser.py',35),
  ('class1 -> INHERITS ID','class1',2,'p_class1','parser.py',39),
  ('class1 -> empty','class1',1,'p_class1','parser.py',40),
  ('class2 -> attrs','class2',1,'p_class2','parser.py',44),
  ('class2 -> empty','class2',1,'p_class2','parser.py',45),
  ('class3 -> mthds','class3',1,'p_class3','parser.py',49),
  ('class3 -> empty','class3',1,'p_class3','parser.py',50),
  ('attrs -> ATTRIBUTES attrs1','attrs',2,'p_attrs','parser.py',54),
  ('attrs1 -> lista_ids COLON tipo SEMI attrs2','attrs1',5,'p_attrs1','parser.py',58),
  ('attrs2 -> attrs1','attrs2',1,'p_attrs2','parser.py',62),
  ('attrs2 -> empty','attrs2',1,'p_attrs2','parser.py',63),
  ('mthds -> METHODS function','mthds',2,'p_mthds','parser.py',67),
  ('vars -> VARIABLES attrs1','vars',2,'p_vars','parser.py',72),
  ('tipo -> tipo_param','tipo',1,'p_tipo','parser.py',76),
  ('tipo -> ID','tipo',1,'p_tipo','parser.py',77),
  ('lista_ids -> ID list1 list2','lista_ids',3,'p_lista_ids','parser.py',81),
  ('list1 -> LS CTEI RS','list1',3,'p_list1','parser.py',85),
  ('list1 -> LS CTEI COMMA CTEI RS','list1',5,'p_list1','parser.py',86),
  ('list1 -> empty','list1',1,'p_list1','parser.py',87),
  ('list2 -> COMMA lista_ids','list2',2,'p_list2','parser.py',91),
  ('list2 -> empty','list2',1,'p_list2','parser.py',92),
  ('main -> MAIN LP RP LB main1 RB','main',6,'p_main','parser.py',97),
  ('main1 -> statement','main1',1,'p_main1','parser.py',101),
  ('main1 -> empty','main1',1,'p_main1','parser.py',102),
  ('function -> function function','function',2,'p_function','parser.py',107),
  ('function -> tipo_retorno FUNCTION ID store_function LP func1 RP LB func2 main1 RB','function',11,'p_function','parser.py',108),
  ('store_function -> <empty>','store_function',0,'p_store_function','parser.py',112),
  ('func1 -> params','func1',1,'p_func1','parser.py',118),
  ('func1 -> empty','func1',1,'p_func1','parser.py',119),
  ('func2 -> vars','func2',1,'p_func2','parser.py',123),
  ('func2 -> empty','func2',1,'p_func2','parser.py',124),
  ('tipo_param -> INT','tipo_param',1,'p_tipo_param','parser.py',128),
  ('tipo_param -> FLOAT','tipo_param',1,'p_tipo_param','parser.py',129),
  ('tipo_param -> CHAR','tipo_param',1,'p_tipo_param','parser.py',130),
  ('params -> ID COLON tipo_param par1','params',4,'p_params','parser.py',137),
  ('par1 -> COMMA params','par1',2,'p_par1','parser.py',141),
  ('par1 -> empty','par1',1,'p_par1','parser.py',142),
  ('tipo_retorno -> tipo_param','tipo_retorno',1,'p_tipo_retorno','parser.py',146),
  ('tipo_retorno -> VOID','tipo_retorno',1,'p_tipo_retorno','parser.py',147),
  ('statement -> statement statement','statement',2,'p_statement','parser.py',157),
  ('statement -> assignment SEMI','statement',2,'p_statement','parser.py',158),
  ('statement -> void_call SEMI','statement',2,'p_statement','parser.py',159),
  ('statement -> read SEMI','statement',2,'p_statement','parser.py',160),
  ('statement -> write SEMI','statement',2,'p_statement','parser.py',161),
  ('statement -> if_st','statement',1,'p_statement','parser.py',162),
  ('statement -> while_st','statement',1,'p_statement','parser.py',163),
  ('statement -> from_st','statement',1,'p_statement','parser.py',164),
  ('statement -> return_st SEMI','statement',2,'p_statement','parser.py',165),
  ('assignment -> var EQ expression','assignment',3,'p_assignment','parser.py',170),
  ('var -> ID list1','var',2,'p_var','parser.py',174),
  ('var -> ID DOT ID','var',3,'p_var','parser.py',175),
  ('void_call -> ID call1 LP call2 RP','void_call',5,'p_void_call','parser.py',180),
  ('void_call -> ID call1 LP RP','void_call',4,'p_void_call','parser.py',181),
  ('call1 -> DOT ID','call1',2,'p_call1','parser.py',185),
  ('call1 -> empty','call1',1,'p_call1','parser.py',186),
  ('call2 -> expression','call2',1,'p_call2','parser.py',190),
  ('call2 -> call2 COMMA call2','call2',3,'p_call2','parser.py',191),
  ('read -> READ LP var read1 RP','read',5,'p_read','parser.py',194),
  ('read1 -> COMMA var','read1',2,'p_read1','parser.py',198),
  ('read1 -> empty','read1',1,'p_read1','parser.py',199),
  ('write -> WRITE LP write1 RP','write',4,'p_write','parser.py',204),
  ('write1 -> expression write2','write1',2,'p_write1','parser.py',208),
  ('write1 -> CTES write2','write1',2,'p_write1','parser.py',209),
  ('write2 -> COMMA write1','write2',2,'p_write2','parser.py',213),
  ('write2 -> empty','write2',1,'p_write2','parser.py',214),
  ('if_st -> IF LP expression RP THEN LB statement RB if1','if_st',9,'p_if_st','parser.py',219),
  ('if1 -> ELSE LB main1 RB','if1',4,'p_if1','parser.py',223),
  ('if1 -> empty','if1',1,'p_if1','parser.py',224),
  ('while_st -> WHILE LP expression RP DO LB main1 RB','while_st',8,'p_while_st','parser.py',229),
  ('from_st -> FROM ID list1 EQ expression UNTIL expression DO LB main1 RB','from_st',11,'p_from_st','parser.py',234),
  ('return_st -> RETURN LP expression RP','return_st',4,'p_return_st','parser.py',239),
  ('expression -> exp','expression',1,'p_expression','parser.py',244),
  ('expression -> exp OR exp','expression',3,'p_expression','parser.py',245),
  ('exp -> k_exp','exp',1,'p_exp','parser.py',249),
  ('exp -> k_exp AND k_exp','exp',3,'p_exp','parser.py',250),
  ('k_exp -> m_exp','k_exp',1,'p_k_exp','parser.py',254),
  ('k_exp -> m_exp LT m_exp','k_exp',3,'p_k_exp','parser.py',255),
  ('k_exp -> m_exp GT m_exp','k_exp',3,'p_k_exp','parser.py',256),
  ('k_exp -> m_exp COMP m_exp','k_exp',3,'p_k_exp','parser.py',257),
  ('k_exp -> m_exp NE m_exp','k_exp',3,'p_k_exp','parser.py',258),
  ('k_exp -> m_exp LTE m_exp','k_exp',3,'p_k_exp','parser.py',259),
  ('k_exp -> m_exp GTE m_exp','k_exp',3,'p_k_exp','parser.py',260),
  ('m_exp -> term','m_exp',1,'p_m_exp','parser.py',264),
  ('m_exp -> term PLUS term','m_exp',3,'p_m_exp','parser.py',265),
  ('m_exp -> term MIN term','m_exp',3,'p_m_exp','parser.py',266),
  ('term -> fact','term',1,'p_term','parser.py',270),
  ('term -> fact MUL fact','term',3,'p_term','parser.py',271),
  ('term -> fact DIV fact','term',3,'p_term','parser.py',272),
  ('fact -> LP expression RP','fact',3,'p_fact','parser.py',276),
  ('fact -> void_call','fact',1,'p_fact','parser.py',277),
  ('fact -> var_cte','fact',1,'p_fact','parser.py',278),
  ('fact -> var','fact',1,'p_fact','parser.py',279),
  ('var_cte -> CTEI','var_cte',1,'p_var_cte','parser.py',283),
  ('var_cte -> CTEF','var_cte',1,'p_var_cte','parser.py',284),
  ('var_cte -> CTEC','var_cte',1,'p_var_cte','parser.py',285),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',297),
]
