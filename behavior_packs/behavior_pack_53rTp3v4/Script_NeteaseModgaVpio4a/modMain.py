# -*- coding: utf-8 -*-

from common.mod import Mod


@Mod.Binding(name="Script_NeteaseModgaVpio4a", version="0.0.1")
class Script_NeteaseModgaVpio4a(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModgaVpio4aServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModgaVpio4aServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModgaVpio4aClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModgaVpio4aClientDestroy(self):
        pass
