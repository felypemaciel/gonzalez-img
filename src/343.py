#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# In[2]:


img = cv2.imread('img/343.tif',0)


# In[3]:


def laplaciano(img):
    cinza = np.zeros([img.shape[0],img.shape[1]])
    for i in range(img.shape[0]-1):
        for j in range(img.shape[1]-1):
            cinza[i][j] = int(img[i][j-1]) + int(img[i-1][j]) + int(img[i+1][j]) + int(img[i][j+1]) - 4*int(img[i][j])
    return cinza


# In[108]:


# DEPRECATED
#def sobel(img):
#    M = np.zeros([img.shape[0], img.shape[1]])
#    for i in range (img.shape[0]-1):
#        for j in range(img.shape[1]-1):
#            x = abs((img[i-1][j+1] + 2*img[i][j+1] + img[i+1][j+1]) - (img[i-1][j-1] + 2*img[i][j-1] + img[i+1][j-1]))
#            y = abs((img[i+1][j-1] + 2*img[i+1][j] + img[i+1][j+1]) - (img[i-1][j-1] + 2*img[i-1][j] + img[i-1][j+1]))
#            M[i][j] = x + y
#    return M


# In[10]:


def sobel(img):
    sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
    img_sobel = abs(sobelx) + abs(sobely)
    return img_sobel


# In[5]:


cinza = laplaciano(img)


# In[6]:


agucada = img - cinza


# In[11]:


img_sobel = sobel(img)


# In[12]:


sobel_blur = cv2.blur(img_sobel, (5,5))


# In[13]:


produto = agucada*sobel_blur


# In[14]:


produto_u8 = img.astype(np.uint8)


# In[15]:


realcada = cv2.add( img , produto_u8)


# In[16]:


potencia = realcada**0.6


# In[17]:


fig, axs = plt.subplots(2,4)
fig.set_size_inches(20, 16)

plt.subplot(241), plt.imshow(img, cmap='gray')
plt.subplot(242), plt.imshow(cinza, cmap='gray')
plt.subplot(243), plt.imshow(sobel_blur, cmap='gray')
plt.subplot(244), plt.imshow(produto, cmap='gray')
plt.subplot(245), plt.imshow(agucada, cmap='gray')
plt.subplot(246), plt.imshow(img_sobel, cmap='gray')
plt.subplot(247), plt.imshow(realcada, cmap='gray')
plt.subplot(248), plt.imshow(potencia, cmap='gray')

plt.show()


# In[ ]:




