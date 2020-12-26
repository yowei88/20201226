def bp(x,y,z,b):
    h=(b//2)+1
    for i in range(h):
        x1=x+i
        y1=y+i
        z1=z+i
        x2=x+b-i
        z2=z+b-i
        mc.setBlocks(x1,y1,z1,x2,y,z2,46)
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
b=int(input("Base:"))
bp(x+1,y,z,b)
