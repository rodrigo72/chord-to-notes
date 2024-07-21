
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD AUG COMMA DIM ELEVEN FIVE FOUR HALF_DIM7 LPAREN MAJ MIN NINE NOTE OMIT PITCH RPAREN SEVEN SIX SIX_NINE SLASH SUS THIRTEEN THREE TWOAll : NOTE Pitch Quality Elements InversionPitch : PITCH\n              |\n    Quality : MIN\n                | AUG\n                | DIM\n                | HALF_DIM7\n                |\n    Elements : Elements Element\n                 |\n    Element : SUS SusAux\n                 | ADD AddAux\n                 | OMIT OmitAux\n                 | LPAREN SetElems RPAREN\n                 | SIX_NINE\n                 | MAJ MajorType\n    Element : NumberElement : PitchNumberMajorType : SEVEN\n                  | NINE\n                  | ELEVEN\n                  | THIRTEEN\n    PitchNumber : PITCH NumberNumber : TWO\n               | THREE\n               | FOUR\n               | FIVE\n               | SIX\n               | SEVEN\n               | NINE\n               | ELEVEN\n               | THIRTEEN\n    SusAux : PITCH SusNumber\n               | SusNumber\n    SusNumber : TWO\n                  | FOUR\n    AddAux : TWO\n               | FOUR\n               | SIX\n               | NINE\n               | ELEVEN\n               | THIRTEEN\n    OmitAux : THREE\n                | FIVE\n    SetElems : SetElems COMMA SetElem\n                 | SetElem\n    SetElem : PITCH Number\n                | Number\n                | OMIT OmitAux\n    Inversion : SLASH NOTE\n                  | SLASH NOTE PITCH\n                  |\n    '
    
_lr_action_items = {'NOTE':([0,13,],[2,32,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,58,59,60,61,],[0,-3,-8,-2,-10,-4,-5,-6,-7,-52,-1,-9,-15,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-50,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,-16,-19,-20,-21,-22,-51,-33,-14,]),'PITCH':([2,3,4,5,6,7,8,9,10,12,15,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,58,60,61,62,],[4,-8,-2,-10,-4,-5,-6,-7,14,-9,35,51,-15,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,59,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,-16,-19,-20,-21,-22,-33,-14,51,]),'MIN':([2,3,4,],[-3,6,-2,]),'AUG':([2,3,4,],[-3,7,-2,]),'DIM':([2,3,4,],[-3,8,-2,]),'HALF_DIM7':([2,3,4,],[-3,9,-2,]),'SLASH':([2,3,4,5,6,7,8,9,10,12,19,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,58,60,61,],[-3,-8,-2,-10,-4,-5,-6,-7,13,-9,-15,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,-16,-19,-20,-21,-22,-33,-14,]),'SUS':([2,3,4,5,6,7,8,9,10,12,19,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,58,60,61,],[-3,-8,-2,-10,-4,-5,-6,-7,15,-9,-15,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,-16,-19,-20,-21,-22,-33,-14,]),'ADD':([2,3,4,5,6,7,8,9,10,12,19,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,58,60,61,],[-3,-8,-2,-10,-4,-5,-6,-7,16,-9,-15,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,-16,-19,-20,-21,-22,-33,-14,]),'OMIT':([2,3,4,5,6,7,8,9,10,12,18,19,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,58,60,61,62,],[-3,-8,-2,-10,-4,-5,-6,-7,17,-9,53,-15,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,-16,-19,-20,-21,-22,-33,-14,53,]),'LPAREN':([2,3,4,5,6,7,8,9,10,12,19,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,58,60,61,],[-3,-8,-2,-10,-4,-5,-6,-7,18,-9,-15,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,-16,-19,-20,-21,-22,-33,-14,]),'SIX_NINE':([2,3,4,5,6,7,8,9,10,12,19,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,58,60,61,],[-3,-8,-2,-10,-4,-5,-6,-7,19,-9,-15,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,-16,-19,-20,-21,-22,-33,-14,]),'MAJ':([2,3,4,5,6,7,8,9,10,12,19,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,54,55,56,57,58,60,61,],[-3,-8,-2,-10,-4,-5,-6,-7,20,-9,-15,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,-16,-19,-20,-21,-22,-33,-14,]),'TWO':([2,3,4,5,6,7,8,9,10,12,14,15,16,18,19,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,54,55,56,57,58,60,61,62,],[-3,-8,-2,-10,-4,-5,-6,-7,23,-9,23,37,40,23,-15,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,37,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,23,-16,-19,-20,-21,-22,-33,-14,23,]),'THREE':([2,3,4,5,6,7,8,9,10,12,14,17,18,19,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,53,54,55,56,57,58,60,61,62,],[-3,-8,-2,-10,-4,-5,-6,-7,24,-9,24,47,24,-15,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,24,47,-16,-19,-20,-21,-22,-33,-14,24,]),'FOUR':([2,3,4,5,6,7,8,9,10,12,14,15,16,18,19,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,51,54,55,56,57,58,60,61,62,],[-3,-8,-2,-10,-4,-5,-6,-7,25,-9,25,38,41,25,-15,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,38,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,25,-16,-19,-20,-21,-22,-33,-14,25,]),'FIVE':([2,3,4,5,6,7,8,9,10,12,14,17,18,19,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,53,54,55,56,57,58,60,61,62,],[-3,-8,-2,-10,-4,-5,-6,-7,26,-9,26,48,26,-15,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,26,48,-16,-19,-20,-21,-22,-33,-14,26,]),'SIX':([2,3,4,5,6,7,8,9,10,12,14,16,18,19,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,54,55,56,57,58,60,61,62,],[-3,-8,-2,-10,-4,-5,-6,-7,27,-9,27,42,27,-15,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,27,-16,-19,-20,-21,-22,-33,-14,27,]),'SEVEN':([2,3,4,5,6,7,8,9,10,12,14,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,54,55,56,57,58,60,61,62,],[-3,-8,-2,-10,-4,-5,-6,-7,28,-9,28,28,-15,55,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,28,-16,-19,-20,-21,-22,-33,-14,28,]),'NINE':([2,3,4,5,6,7,8,9,10,12,14,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,54,55,56,57,58,60,61,62,],[-3,-8,-2,-10,-4,-5,-6,-7,29,-9,29,43,29,-15,56,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,29,-16,-19,-20,-21,-22,-33,-14,29,]),'ELEVEN':([2,3,4,5,6,7,8,9,10,12,14,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,54,55,56,57,58,60,61,62,],[-3,-8,-2,-10,-4,-5,-6,-7,30,-9,30,44,30,-15,57,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,30,-16,-19,-20,-21,-22,-33,-14,30,]),'THIRTEEN':([2,3,4,5,6,7,8,9,10,12,14,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,51,54,55,56,57,58,60,61,62,],[-3,-8,-2,-10,-4,-5,-6,-7,31,-9,31,45,31,-15,58,-17,-18,-24,-25,-26,-27,-28,-29,-30,-31,-32,-23,-11,-34,-35,-36,-12,-37,-38,-39,-40,-41,-42,-13,-43,-44,31,-16,-19,-20,-21,-22,-33,-14,31,]),'RPAREN':([23,24,25,26,27,28,29,30,31,47,48,49,50,52,63,64,65,],[-24,-25,-26,-27,-28,-29,-30,-31,-32,-43,-44,61,-46,-48,-47,-49,-45,]),'COMMA':([23,24,25,26,27,28,29,30,31,47,48,49,50,52,63,64,65,],[-24,-25,-26,-27,-28,-29,-30,-31,-32,-43,-44,62,-46,-48,-47,-49,-45,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'All':([0,],[1,]),'Pitch':([2,],[3,]),'Quality':([3,],[5,]),'Elements':([5,],[10,]),'Inversion':([10,],[11,]),'Element':([10,],[12,]),'Number':([10,14,18,51,62,],[21,33,52,63,52,]),'PitchNumber':([10,],[22,]),'SusAux':([15,],[34,]),'SusNumber':([15,35,],[36,60,]),'AddAux':([16,],[39,]),'OmitAux':([17,53,],[46,64,]),'SetElems':([18,],[49,]),'SetElem':([18,62,],[50,65,]),'MajorType':([20,],[54,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> All","S'",1,None,None,None),
  ('All -> NOTE Pitch Quality Elements Inversion','All',5,'p_All','chord_yacc.py',6),
  ('Pitch -> PITCH','Pitch',1,'p_Pitch','chord_yacc.py',12),
  ('Pitch -> <empty>','Pitch',0,'p_Pitch','chord_yacc.py',13),
  ('Quality -> MIN','Quality',1,'p_Quality','chord_yacc.py',23),
  ('Quality -> AUG','Quality',1,'p_Quality','chord_yacc.py',24),
  ('Quality -> DIM','Quality',1,'p_Quality','chord_yacc.py',25),
  ('Quality -> HALF_DIM7','Quality',1,'p_Quality','chord_yacc.py',26),
  ('Quality -> <empty>','Quality',0,'p_Quality','chord_yacc.py',27),
  ('Elements -> Elements Element','Elements',2,'p_Elements','chord_yacc.py',37),
  ('Elements -> <empty>','Elements',0,'p_Elements','chord_yacc.py',38),
  ('Element -> SUS SusAux','Element',2,'p_Element','chord_yacc.py',50),
  ('Element -> ADD AddAux','Element',2,'p_Element','chord_yacc.py',51),
  ('Element -> OMIT OmitAux','Element',2,'p_Element','chord_yacc.py',52),
  ('Element -> LPAREN SetElems RPAREN','Element',3,'p_Element','chord_yacc.py',53),
  ('Element -> SIX_NINE','Element',1,'p_Element','chord_yacc.py',54),
  ('Element -> MAJ MajorType','Element',2,'p_Element','chord_yacc.py',55),
  ('Element -> Number','Element',1,'p_Element2','chord_yacc.py',67),
  ('Element -> PitchNumber','Element',1,'p_Element3','chord_yacc.py',73),
  ('MajorType -> SEVEN','MajorType',1,'p_MajorType','chord_yacc.py',78),
  ('MajorType -> NINE','MajorType',1,'p_MajorType','chord_yacc.py',79),
  ('MajorType -> ELEVEN','MajorType',1,'p_MajorType','chord_yacc.py',80),
  ('MajorType -> THIRTEEN','MajorType',1,'p_MajorType','chord_yacc.py',81),
  ('PitchNumber -> PITCH Number','PitchNumber',2,'p_PitchNumber','chord_yacc.py',88),
  ('Number -> TWO','Number',1,'p_Number','chord_yacc.py',94),
  ('Number -> THREE','Number',1,'p_Number','chord_yacc.py',95),
  ('Number -> FOUR','Number',1,'p_Number','chord_yacc.py',96),
  ('Number -> FIVE','Number',1,'p_Number','chord_yacc.py',97),
  ('Number -> SIX','Number',1,'p_Number','chord_yacc.py',98),
  ('Number -> SEVEN','Number',1,'p_Number','chord_yacc.py',99),
  ('Number -> NINE','Number',1,'p_Number','chord_yacc.py',100),
  ('Number -> ELEVEN','Number',1,'p_Number','chord_yacc.py',101),
  ('Number -> THIRTEEN','Number',1,'p_Number','chord_yacc.py',102),
  ('SusAux -> PITCH SusNumber','SusAux',2,'p_SusAux','chord_yacc.py',109),
  ('SusAux -> SusNumber','SusAux',1,'p_SusAux','chord_yacc.py',110),
  ('SusNumber -> TWO','SusNumber',1,'p_SusNumber','chord_yacc.py',120),
  ('SusNumber -> FOUR','SusNumber',1,'p_SusNumber','chord_yacc.py',121),
  ('AddAux -> TWO','AddAux',1,'p_AddAux','chord_yacc.py',128),
  ('AddAux -> FOUR','AddAux',1,'p_AddAux','chord_yacc.py',129),
  ('AddAux -> SIX','AddAux',1,'p_AddAux','chord_yacc.py',130),
  ('AddAux -> NINE','AddAux',1,'p_AddAux','chord_yacc.py',131),
  ('AddAux -> ELEVEN','AddAux',1,'p_AddAux','chord_yacc.py',132),
  ('AddAux -> THIRTEEN','AddAux',1,'p_AddAux','chord_yacc.py',133),
  ('OmitAux -> THREE','OmitAux',1,'p_OmitAux','chord_yacc.py',140),
  ('OmitAux -> FIVE','OmitAux',1,'p_OmitAux','chord_yacc.py',141),
  ('SetElems -> SetElems COMMA SetElem','SetElems',3,'p_SetElems','chord_yacc.py',148),
  ('SetElems -> SetElem','SetElems',1,'p_SetElems','chord_yacc.py',149),
  ('SetElem -> PITCH Number','SetElem',2,'p_SetElem','chord_yacc.py',158),
  ('SetElem -> Number','SetElem',1,'p_SetElem','chord_yacc.py',159),
  ('SetElem -> OMIT OmitAux','SetElem',2,'p_SetElem','chord_yacc.py',160),
  ('Inversion -> SLASH NOTE','Inversion',2,'p_Inversion','chord_yacc.py',170),
  ('Inversion -> SLASH NOTE PITCH','Inversion',3,'p_Inversion','chord_yacc.py',171),
  ('Inversion -> <empty>','Inversion',0,'p_Inversion','chord_yacc.py',172),
]