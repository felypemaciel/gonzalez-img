#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt

# In[18]:


from skimage import data
from skimage.util.dtype import dtype_range
from skimage.util import img_as_ubyte
from skimage import exposure
from skimage.morphology import rectangle
from skimage.filters import rank


# In[7]:


img = cv2.imread('img/326.tif')


# In[14]:


img0 = cv2.imread('img/326.tif', 0)


# In[4]:


imgeq = cv2.equalizeHist(img0)


# In[19]:


footprint = rectangle(3,3)
imglocaleq = rank.equalize(img0, footprint)


# In[24]:


fig, axs = plt.subplots(13)
fig.set_size_inches(12,3)

plt.subplot(131), plt.imshow(img)
plt.subplot(132), plt.imshow(imgeq, cmap='gray')
plt.subplot(133), plt.imshow(imglocaleq, cmap='gray')

plt.show()


# In[ ]:




