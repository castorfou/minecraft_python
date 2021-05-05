#!/usr/bin/env python
# coding: utf-8

# In[4]:


pickaxes =14


# In[5]:


pickaxes


# In[6]:


bread=142


# In[7]:


bread


# In[8]:


pickaxes


# In[9]:


iron=30


# In[10]:


cobblestone=25


# In[11]:


pickaxes=12


# In[12]:


cat=5


# In[13]:


cat


# In[39]:


from mcpi.minecraft import Minecraft


# In[40]:


mc=Minecraft.create()


# In[16]:


mc.player.setTilePos(0,0,0)


# In[17]:


mc.setBlock(0,0,1,56)


# In[18]:


i=0
while (i<1000):
    i+=1
    mc.setBlock(0,i,0,56)


# In[19]:


mc.setBlocks(0,0,0,10,10,10,56)


# In[20]:


mc.setBlocks(0,0,0,1000,10000,10,56)


# In[35]:


mc.player.getTilePos()


# In[22]:


mc.player.setTilePos(2110,21,37)


# In[23]:


#1er mur
mc.setBlocks(2110,10,37,2120,20,37,56)
#sol
mc.setBlocks(2110,10,37,2120,10,47,89)
# #2eme mur
mc.setBlocks(2110,10,37,2110,20,47,56)
mc.setBlocks(2120,20,47,2110,10,47,56)
mc.setBlocks(2120,20,47,2120,10,37,56)

mc.setBlocks(2120,20,47,2110,20,37,89)
mc.setBlocks(2115,11,37,2116,13,37,64)


# In[24]:


mc.setBlocks(2110,10,37,2130,30,57,0)


# In[25]:


mc.setBlock(2110,10,37,41)


# In[31]:


def effacer_maison():
    x,y,z =mc.player.getTilePos()
    mc.setBlocks(x-1000,y,z-1000,x+100,y+100,z+100,0)


# In[27]:


def creer_maison(largeur=10,hauteur=10,longueur=10):
    x,y,z =mc.player.getTilePos()

    x=x+2
    z=z+2
    largeur-=1
    hauteur-=1
    longueur-=1

    mc.setBlocks(x,y,z,x+largeur,y+hauteur,z,56)
    mc.setBlocks(x,y,z,x,y+hauteur,z+longueur,56)
    mc.setBlocks(x+largeur,y+hauteur,z+longueur,x+largeur,y,z,56)
    mc.setBlocks(x+largeur,y+hauteur,z+longueur,x,y,z+longueur,56)
    #sol
    mc.setBlocks(x,y,z,x+largeur,y,z+longueur,89)
    #plafond
    mc.setBlocks(x+largeur,y+hauteur,z+longueur,x,y+hauteur,z,89)
    mc.setBlocks(x+5,y+1,z,x+6,y+3,z,0)
    


# In[28]:


effacer_maison()
creer_maison(10,5,5)


# In[32]:


effacer_maison()


# # changing the values of variables
# 
# 

# In[3]:


cats = 5


# In[6]:


cats


# In[7]:



cats=10


# # integers

# In[8]:


name = 'Gabriel'


# In[9]:


name


# In[10]:


type(name)


# In[11]:


nombres= [10,2]


# In[12]:


nombres


# # MISSION #1: TELEPORT THE PLAYER

# In[20]:


from mcpi.minecraft import Minecraft
mc=Minecraft.create()


# In[21]:


x=-128
y=73
z=16


# ![image.png](attachment:image.png)

# In[22]:


mc.player.setTilePos(x,y,z)


# In[4]:


x, y, z


# In[20]:


mc.player.setTilePos(-256,-63,229)


# In[26]:


mc.player.setPos(x,y,z)


# # Mission #2: GO EXACTLY WHERE YOU WANT

# In[25]:


# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Set x,y,and z variables to represent coordinates
x = 10.5
y = 110.0
z = 12.0

# Change the player's position
mc.player.setPos(x,y,z)


# In[26]:


import time


# In[30]:



time.sleep(0.2)
print('je m appelle Eloi')


# In[ ]:




