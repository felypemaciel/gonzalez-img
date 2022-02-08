#!/usr/bin/env python
# coding: utf-8

# In[127]:


import numpy as np
import cv2
from PIL import Image as im
import matplotlib.pyplot as plt


# In[128]:


img = cv2.imread('img/312a.tif')


# In[135]:


slicingb = np.where(img >= 148, 255, 50)


# In[130]:


slicingc = np.where(np.logical_and(img >= 70, img <= 150 ), 0, img )


# In[131]:


fig, axs = plt.subplots(1, 3)
fig.set_size_inches(12, 4)

plt.subplot(131), plt.imshow(img)
plt.subplot(132), plt.imshow(slicingb)
plt.subplot(133), plt.imshow(slicingc)
plt.show()

