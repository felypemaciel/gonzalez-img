#!/usr/bin/env python
# coding: utf-8

# In[54]:


import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image as im


# In[46]:


dollar = cv2.imread('img/314.tif',0)
dollararray = np.asarray(dollar)


# In[47]:


binarydollar = []
for i in range(dollar.shape[0]):
    for j in range(dollar.shape[1]):
        binarydollar.append(np.binary_repr(dollar[i][j], width=8))


# In[56]:


bit8 = (np.array([int(i[0]) for i in binarydollar], dtype=np.uint8)*128).reshape(dollar.shape[0], dollar.shape[1])
bit7 = (np.array([int(i[1]) for i in binarydollar], dtype=np.uint8)*64).reshape(dollar.shape[0], dollar.shape[1])
bit6 = (np.array([int(i[2]) for i in binarydollar], dtype=np.uint8)*32).reshape(dollar.shape[0], dollar.shape[1])
bit5 = (np.array([int(i[3]) for i in binarydollar], dtype=np.uint8)*16).reshape(dollar.shape[0], dollar.shape[1])
bit4 = (np.array([int(i[4]) for i in binarydollar], dtype=np.uint8)*8).reshape(dollar.shape[0], dollar.shape[1])
bit3 = (np.array([int(i[5]) for i in binarydollar], dtype=np.uint8)*4).reshape(dollar.shape[0], dollar.shape[1])
bit2 = (np.array([int(i[6]) for i in binarydollar], dtype=np.uint8)*2).reshape(dollar.shape[0], dollar.shape[1])
bit1 = (np.array([int(i[7]) for i in binarydollar], dtype=np.uint8)*1).reshape(dollar.shape[0], dollar.shape[1])


# In[51]:


fig, axs = plt.subplots(3, 3)
fig.set_size_inches(14, 6)

plt.subplot(331), plt.imshow(dollar, cmap='gray')
plt.subplot(332), plt.imshow(cv2.normalize(bit1, np.zeros(dollar.shape), 0, 255, cv2.NORM_MINMAX), cmap='gray')
plt.subplot(333), plt.imshow(cv2.normalize(bit2, np.zeros(dollar.shape), 0, 255, cv2.NORM_MINMAX), cmap='gray')
plt.subplot(334), plt.imshow(cv2.normalize(bit3, np.zeros(dollar.shape), 0, 255, cv2.NORM_MINMAX), cmap='gray')
plt.subplot(335), plt.imshow(cv2.normalize(bit4, np.zeros(dollar.shape), 0, 255, cv2.NORM_MINMAX), cmap='gray')
plt.subplot(336), plt.imshow(cv2.normalize(bit5, np.zeros(dollar.shape), 0, 255, cv2.NORM_MINMAX), cmap='gray')
plt.subplot(337), plt.imshow(cv2.normalize(bit6, np.zeros(dollar.shape), 0, 255, cv2.NORM_MINMAX), cmap='gray')
plt.subplot(338), plt.imshow(cv2.normalize(bit7, np.zeros(dollar.shape), 0, 255, cv2.NORM_MINMAX), cmap='gray')
plt.subplot(339), plt.imshow(cv2.normalize(bit8, np.zeros(dollar.shape), 0, 255, cv2.NORM_MINMAX), cmap='gray')

plt.show()

