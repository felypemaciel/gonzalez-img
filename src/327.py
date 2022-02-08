#!/usr/bin/env python
# coding: utf-8

# In[58]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[74]:


img = cv2.imread('img/327.tif')
img0 = cv2.imread('img/327.tif', 0)


# In[75]:


imgglobaleq = cv2.equalizeHist(img0)


# In[76]:


g = np.zeros([img.shape[0], img.shape[1]])
mediaglobal = img0.mean()
dpglobal = img0.std()


# In[62]:


g.shape


# In[30]:


def mediadp(vizinhos):
    media = np.mean(vizinhos)
    std = np.std(vizinhos)
    return [media, std]


# In[77]:


for i in range (1, img0.shape[0]-1):
    for j in range (1, img0.shape[1]-1):
        vizinhos = []
        for m in range (i-1, i+2):
            for n in range (j-1, j+2):
                vizinhos.append(img0[m][n])
        media, std = mediadp(vizinhos)
        if ((media <= 0.4*mediaglobal) and (0.02*dpglobal <= std <= 0.4*dpglobal)):
            g[i][j] = 4*img0[i][j]
        else:
            g[i][j] = img0[i][j]


# In[78]:


fig, axs = plt.subplots(13)
fig.set_size_inches(12,4)

plt.subplot(131), plt.imshow(img0, cmap='gray')
plt.subplot(132), plt.imshow(imgglobaleq, cmap='gray')
plt.subplot(133), plt.imshow(g, cmap='gray')

plt.show()

