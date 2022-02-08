#!/usr/bin/env python
# coding: utf-8

# In[73]:


import cv2
import numpy as np
import matplotlib.pyplot as plt


# In[66]:


fig305a = cv2.imread('img/305a.tif')


# In[67]:


c = 255 / np.log(1 + np.max(fig305a))
transf_log = c * (np.log(fig305a+1))


# In[68]:


transf_log = np.array(transf_log, dtype = np.uint8)


# In[71]:


plt.subplot(121), plt.imshow(fig305a)
plt.subplot(122), plt.imshow(transf_log)
plt.show()

