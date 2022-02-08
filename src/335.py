#!/usr/bin/env python
# coding: utf-8

# # imagem 3.35

# In[1]:


import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[2]:


img = cv2.imread('img/335.tif')


# In[5]:


blur3 = cv2.blur(img, (3,3))


# In[8]:


medianblur3 = cv2.medianBlur(img, 3)


# In[9]:


fig, axs = plt.subplots(13)
fig.set_size_inches(12,4)

plt.subplot(131), plt.imshow(img)
plt.subplot(132), plt.imshow(blur3)
plt.subplot(133), plt.imshow(medianblur3)

plt.show()


# In[ ]:




