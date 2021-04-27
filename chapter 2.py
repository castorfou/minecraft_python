#!/usr/bin/env python
# coding: utf-8

# In[1]:


pickaxes =14


# In[2]:


pickaxes


# In[3]:


bread=142


# In[4]:


bread


# In[5]:


pickaxes


# In[6]:


iron=30


# In[7]:


cobblestone=25


# In[8]:


pickaxes=12


# In[9]:


cat=5


# In[10]:


cat


# In[123]:


from mcpi.minecraft import Minecraft


# In[124]:


mc=Minecraft.create()


# In[110]:


mc.player.setTilePos(0,0,0)


# In[112]:


mc.setBlock(0,0,1,56)


# In[113]:


i=0
while (i<1000):
    i+=1
    mc.setBlock(0,i,0,56)


# In[114]:


mc.setBlocks(0,0,0,10,10,10,56)


# In[116]:


mc.setBlocks(0,0,0,1000,10000,10,56)


# In[65]:


mc.player.getTilePos()


# In[132]:


mc.player.setTilePos(2110,21,37)


# In[145]:


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


# In[137]:


mc.setBlocks(2110,10,37,2130,30,57,0)


# In[149]:


mc.setBlock(2110,10,37,41)


# In[209]:


def effacer_maison():
    x,y,z =mc.player.getTilePos()
    mc.setBlocks(x-100,y,z-100,x+100,y+100,z+100,0)


# In[221]:


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
    


# In[222]:


effacer_maison()
creer_maison(10,5,5)


# In[219]:


effacer_maison()


# In[ ]:




