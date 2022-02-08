#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
from PIL import Image as im
import matplotlib.pyplot as plt


# In[2]:


img = cv2.imread('img/308a.tif')


# In[3]:


def powerTransform(image, gamma):
    gammaTransform = np.array(255*(image/255) ** gamma, dtype='uint8')
    return gammaTransform


# In[4]:


fig308b = powerTransform(img, .6)
fig308c = powerTransform(img, .4)
fig308d = powerTransform(img, .3)


# In[6]:

plt.figure(figsize=(8, 12))
plt.subplot(221), plt.imshow(img)
plt.subplot(222), plt.imshow(fig308b)
plt.subplot(223), plt.imshow(fig308c)
plt.subplot(224), plt.imshow(fig308d)
plt.show()

