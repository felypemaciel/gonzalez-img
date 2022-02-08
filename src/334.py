#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[2]:


img = cv2.imread('img/334.tif',0)


# In[3]:


blur15 = cv2.blur(img, (15,15))


# In[4]:


ret, imglim = cv2.threshold(blur15, 65, 255, cv2.THRESH_BINARY)


# In[5]:


fig, axs = plt.subplots(13)
fig.set_size_inches(12,4)

plt.subplot(131), plt.imshow(img, cmap='gray')
plt.subplot(132), plt.imshow(blur15, cmap='gray')
plt.subplot(133), plt.imshow(imglim, cmap='gray')

plt.show()

