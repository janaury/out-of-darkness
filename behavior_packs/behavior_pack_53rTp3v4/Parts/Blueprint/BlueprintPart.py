# -*- coding: utf-8 -*-

from Preset.Model.PartBase import PartBase
from Preset.Model.GameObject import registerGenericClass

@registerGenericClass('BlueprintPart')
class BlueprintPart(PartBase):

    def __init__(self):
        super(BlueprintPart, self).__init__()
        self.name = '蓝图零件'
        self.description = '蓝图零件'
        self.bpFiles = ['BlueprintPart.bp']
        self.replicated = []
        self.v_isplayer = False
        self.v_flog = 0.0

    def TickClient(self):
        return PartBase.TickClient(self)

    def DestroyServer(self):
        return PartBase.DestroyServer(self)

    def InitClient(self):
        return PartBase.InitClient(self)

    def DestroyClient(self):
        return PartBase.DestroyClient(self)

    def TickServer(self):
        return PartBase.TickServer(self)

    def InitServer(self):
        return PartBase.InitServer(self)
