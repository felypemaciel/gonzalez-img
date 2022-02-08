#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import cv2
import matplotlib.pyplot as plt


# In[3]:


img = cv2.imread('img/342.tif',0)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

img_sobel = abs(sobelx) + abs(sobely)
# In[10]:

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.subplot(122), plt.imshow(img_sobel, cmap='gray')

plt.show()


# In[ ]:




