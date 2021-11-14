#!/usr/bin/env python
# coding: utf-8

# # chap 1

# ## chap 1.1

# In[2]:


"w" + "o" * 5


# In[3]:


print(2+2)


# In[4]:


print(2*2)
print("W" + "o" * 5)
print("PYTHON")
print("<3s")
print("Minecraft")


# In[8]:


from mcpi.minecraft import Minecraft
mc = Minecraft.create()


# In[9]:


mc.player.setTilePos(0, 120, 0)


# # chap2

# ### chap2.1

# f1=barre inventaire
# f3=position etc

# In[10]:


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x=10
y=110
z=12


# In[11]:


mc.player.setTilePos(x, y, z)


# Pour se teleporter
# definir x, y et z
# entrer mc.player.setTilePos(x, y, z)

# In[14]:


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x=20
y=56
z=63


# In[15]:


mc.player.setTilePos(x, y, z)


# ### chap2.2

# In[16]:


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x=56
y=96
z=135


# In[17]:


mc.player.setPos(x, y, z)


# difference avec 2.1= ici, on se teleporte au dessus du bloc  (en gros, on ne tombe pas)

# ### chap 2.3

# In[18]:


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x=1
y=5
z=32

mc.player.setTilePos(x, y, z)

time.sleep(10)

x=5
y=22
z=11

mc.player.setTilePos(x, y, z)


# time.sleep() --> attendre pour une donnée de temps avant de faire action suivante

# ### chap2.4

# In[19]:


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x=10
y=11
z=12
mc.player.setTilePos(x, y, z)


# In[20]:


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x=10
y=110
z=-12
mc.player.setTilePos(x, y, z)

