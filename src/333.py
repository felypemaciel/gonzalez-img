#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


img = cv2.imread('img/333.tif')


# In[6]:


blur3 = cv2.blur(img,(3,3))
blur5 = cv2.blur(img,(5,5))
blur9 = cv2.blur(img,(9,9))
blur15 = cv2.blur(img,(15,15))
blur35 = cv2.blur(img,(35,35))


# In[10]:


fig, axs = plt.subplots(3,2)
fig.set_size_inches(8,12)

plt.subplot(321), plt.imshow(img)
plt.subplot(322), plt.imshow(blur3)
plt.subplot(323), plt.imshow(blur5)
plt.subplot(324), plt.imshow(blur9)
plt.subplot(325), plt.imshow(blur15)
plt.subplot(326), plt.imshow(blur35)

plt.show()


# In[ ]:




