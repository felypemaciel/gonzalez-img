#!/usr/bin/env python
# coding: utf-8

# In[49]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image as im


# In[19]:


img = cv2.imread('img/310b.tif')


# In[35]:


rmax = np.max(img)
rmin = np.min(img)


# In[36]:


m = 255/(rmax - rmin)


# In[39]:


stretching = np.array(m*img + 255 - m*rmax, dtype='uint8')


# In[144]:


ret,str2 = cv2.threshold(img,np.mean(img),255,cv2.THRESH_BINARY)


# In[145]:


fig, axs = plt.subplots(1, 3)
fig.set_size_inches(12, 4)

plt.subplot(131), plt.imshow(img)
plt.subplot(132), plt.imshow(stretching)
plt.subplot(133), plt.imshow(str2)
plt.show()

