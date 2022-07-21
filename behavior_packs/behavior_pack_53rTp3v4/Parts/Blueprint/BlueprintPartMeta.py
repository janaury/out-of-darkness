# -*- coding: utf-8 -*-

from Meta.TypeMeta import PFloat, PInt, PStr, PBool
from Meta.ClassMetaManager import sunshine_class_meta
from Preset.Model import PartBaseMeta

@sunshine_class_meta
class BlueprintPartMeta(PartBaseMeta):
    CLASS_NAME = 'BlueprintPart'
    PROPERTIES = {'v_isplayer': PBool(sort=10000, group='蓝图零件', text='v_PartVariable_1'), 'v_flog': PFloat(sort=10000, group='蓝图零件', text='v_PartVariable_1')}
