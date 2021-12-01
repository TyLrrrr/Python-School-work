#!/usr/bin/env python
# coding: utf-8

# In[13]:


i    = 0
j    = 0
Mat  = []
Row  = []
ROWS = 3
COLS = 3

Row = []
for i in range(0, ROWS):
 Row = []
 for j in range(0, COLS):
  # Row.append(0)  # Can be a user input.
    Row.append(input())
 Mat.append(Row)
print(Mat)
print("")


# In[15]:


i    = 0
j    = 0
Mat  = []
Row  = []
ROWS = 6
COLS = 4

Row = []
for i in range(0, ROWS-2):
 Row = []
 for j in range(0, COLS):
  # Row.append(0)  # Can be a user input.
    Row.append(j-3)
 Mat.append(Row)
print(Mat)
print("")


# In[ ]:




