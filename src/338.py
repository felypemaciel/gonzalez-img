#!/usr/bin/env python
# coding: utf-8

# In[237]:


import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[210]:


img = cv2.imread('img/338.tif', 0)


# In[212]:


cinza = np.zeros([img.shape[0], img.shape[1]])


# In[214]:


for i in range(img.shape[0]-1):
    for j in range(img.shape[1]-1):
        cinza[i][j] = int(img[i][j-1]) + int(img[i-1][j]) + int(img[i+1][j]) + int(img[i][j+1]) - 4*int(img[i][j])


# In[215]:


b338 = np.zeros([img.shape[0],img.shape[1]])


# In[216]:


b338 = img - cinza


# In[219]:


super8 = np.zeros([img.shape[0],img.shape[1]])


# In[253]:


for i in range(img.shape[0]-1):
    for j in range(img.shape[1]-1):
        super8[i][j] = int(img[i-1][j-1]) + int(img[i][j-1]) + int(img[i+1][j-1]) + int(img[i-1][j]) + int(img[i+1][j]) + int(img[i-1][j+1]) + int(img[i][j+1]) + int(img[i+1][j+1]) - 8*int(img[i][j])


# In[255]:


super8 = super8 - np.min(super8)


# In[256]:


super8 = 255*(super8/np.max(super8))


# In[258]:


agucadab = np.zeros([img.shape[0],img.shape[1]])


# In[259]:


agucadab = img - super8
agucadab = agucadab - np.min(agucadab)
agucadab = 255*(agucadab/np.max(agucadab))

# In[262]:


fig, axs = plt.subplots(1,3)
fig.set_size_inches(12,4)

plt.subplot(131), plt.imshow(img,cmap='gray')
plt.subplot(132), plt.imshow(b338,cmap='gray')
plt.subplot(133), plt.imshow(agucadab,cmap='gray')

plt.show()



