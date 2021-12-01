#!/usr/bin/env python
# coding: utf-8

# In[53]:


import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')
zline = np.linspace(1, 15, 1000)
xline = np.sin(zline)
yline = np.cos(zline)
ax.plot3D(xline, yline, zline, 'red')

# Data for three-dimensional scattered points
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Blues');
plt.show()


x = [1,2,3,4,5]
y = [2,4,6,8,10]
z = [3,6,9,12,15]

plt.plot(x,y, label = "y = 2x")
plt.legend()
plt.plot(x,z, label = "y = 3x")
plt.legend()
plt.show()
x = np.arange(1, 6, 1)
y = x ** 2

plt.plot(x[0:3], y[0:3], "o--r", label= "y = x^2")
plt.plot(x[2:], y[2:], "o--b", label= "y = x^2")
plt.legend()
plt.show()


# In[ ]:




