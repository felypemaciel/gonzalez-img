#!/usr/bin/env python
# coding: utf-8

# In[53]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image


# In[50]:


img1 = cv2.imread('img/340.tif')
img = cv2.imread('img/340.tif',0)


# In[88]:


borrada = cv2.GaussianBlur(img, (5,5), 3)


# In[89]:


mascara = np.zeros([img.shape[0], img.shape[1]])
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        mascara[i][j] = int(img[i][j]) - int(borrada[i][j])


# In[92]:


img2 = np.zeros([img.shape[0], img.shape[1]])
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img2[i][j] = int(img[i][j]) + int(mascara[i][j])


# In[12]:


img2 = img + mascara


# In[93]:


highboost = np.zeros([img.shape[0], img.shape[1]])
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        highboost[i][j] = int(img[i][j]) + 4.5*int(mascara[i][j])


# In[14]:


highboost = img + 4.5*mascara


# In[95]:


fig, axs = plt.subplots(5,1)
fig.set_size_inches(5,10)

plt.subplot(511), plt.imshow(img, cmap='gray')
plt.subplot(512), plt.imshow(borrada, cmap='gray')
plt.subplot(513), plt.imshow(mascara, cmap='gray')
plt.subplot(514), plt.imshow(img2, cmap='gray')
plt.subplot(515), plt.imshow(highboost, cmap='gray')

plt.show()


# In[ ]:




