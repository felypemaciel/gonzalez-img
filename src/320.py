#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image as im


# In[38]:


imga = cv2.imread('img/3201.tif')
imga0 = cv2.imread('img/3201.tif',0)
imgb = cv2.imread('img/3202.tif')
imgb0 = cv2.imread('img/3202.tif',0)
imgc = cv2.imread('img/3203.tif')
imgc0 = cv2.imread('img/3203.tif',0)
imgd = cv2.imread('img/3204.tif')
imgd0 = cv2.imread('img/3204.tif',0)


# In[40]:


eqa = cv2.equalizeHist(imga0)
eqb = cv2.equalizeHist(imgb0)
eqc = cv2.equalizeHist(imgc0)
eqd = cv2.equalizeHist(imgd0)


# In[50]:


fig, axs = plt.subplots(4, 3)
fig.set_size_inches(12, 16)

plt.subplot(431), plt.imshow(imgd, cmap='gray')
plt.subplot(432), plt.imshow(eqd, cmap='gray')
plt.subplot(433), plt.hist(eqd.flatten(), 255, [0, 255])
plt.subplot(434), plt.imshow(imga, cmap='gray')
plt.subplot(435), plt.imshow(eqa, cmap='gray')
plt.subplot(436), plt.hist(eqa.flatten(), 255, [0, 255])
plt.subplot(437), plt.imshow(imgb, cmap='gray')
plt.subplot(438), plt.imshow(eqb, cmap='gray')
plt.subplot(439), plt.hist(eqb.flatten(), 255, [0, 255])
plt.subplot(4,3,10), plt.imshow(imgc, cmap='gray')
plt.subplot(4,3,11), plt.imshow(eqc, cmap='gray')
plt.subplot(4,3,12), plt.hist(eqc.flatten(), 255, [0, 255])

plt.show()

