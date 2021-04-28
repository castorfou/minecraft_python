#!/usr/bin/env python
# coding: utf-8

# # pour se connecter à minecraft
# ![image.png](attachment:image.png)

# In[54]:


from mcpi.minecraft import Minecraft
mc=Minecraft.create()


# # pour se teleporter sur la carte à la position 0,0,0

# In[23]:


mc.player.setTilePos(0,0,0)


# ## pour connaitre sa position

# In[5]:


mc.player.getTilePos()


# # pour créer une maison

# In[6]:


def creer_maison(largeur=10,hauteur=10,longueur=10):
    x,y,z =mc.player.getTilePos()
    print(x,y,z)

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
    mc.setBlocks(x+largeur,y+hauteur,z+
                 longueur,x,y+hauteur,z,89)
    mc.setBlocks(x+5,y+1,z,x+6,y+3,z,0)
    


# # pour effacer une maison à x, y, z

# In[41]:


def effacer_maison(x,y,z):
#     x,y,z =mc.player.getTilePos()
    mc.setBlocks(x-100,y,z-100,x+100,y+100,z+100,0)


# In[43]:


effacer_maison(19,0,-12)


# In[10]:


creer_maison()


# # on va chercher la taille du monde

# In[21]:


mc.player.setTilePos(10000000000,200,0)


# # on va eraser le monde (1000 de côté)

# In[56]:


def effacer_monde(taille=100):
    x,y,z =mc.player.getTilePos()
    mc.setBlocks(x-taille,y+150,z-taille,x+taille,y+200,z+taille,0)


# In[53]:


effacer_monde(200)


# In[55]:


mc.player.setTilePos(200,200,200)


# In[ ]:




