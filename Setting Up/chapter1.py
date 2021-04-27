# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft

#mc = Minecraft.create(port=25565)
mc = Minecraft.create()

mc.player.setTilePos(0,120,0)

curPos = mc.player.getTilePos()

print(curPos)

mc.postToChat('hello')