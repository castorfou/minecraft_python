#!/usr/bin/env python
# coding: utf-8

# # MISSION #1: TELEPORT the PLAYER
# 

# In[52]:


from mcpi.minecraft import Minecraft
mc = Minecraft.create()


# In[2]:


mc


# In[46]:


x = 4
y = 63
z = -92

x,y,z

mc.player.setTilePos(x,y,z)


# In[22]:


print(f'truc de ouf d\'eloi', x1,y1,z1)


# In[ ]:


import time

for i in range(10):

    poof = mc.player.getPos()

    x1,y1,z1=poof
    x1=x1-10
    time.sleep(0.5)
    mc.player.setTilePos(x1,y1,z1)
    # x1, poof


# In[49]:


mc.player.getPos()


# In[51]:


#truc de ouf de eloi = 
mc.player.setTilePos(26,40,55)


# # mission #2 : Go exactly where you want

# In[62]:


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
#Set x, y, z variablesto represent coordinate

x = 10.56
y = 110.0
z = 12.0

# Changethe player`s position

mc.player.setPos(x,y,z)


# In[63]:


mc.player.setPos(x,y,z)


# In[64]:


mc.player.setTilePos(x,y,z)


# In[65]:


import time

time.sleep(5)
print("Gabriel est le roi du python")


# # mission #3 : Teleportation Tour

# In[ ]:




