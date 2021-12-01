#!/usr/bin/env python
# coding: utf-8

# In[10]:


import matplotlib.pyplot as plt
import pandas as pd

DataFilePath = "C:\\Users\\sathe\\Desktop\\Data2.csv"
Population   = pd.read_csv(DataFilePath)

#print(Population)

List1 = list(Population["Year"])
List2 = list(Population["United States"])
List3 = list(Population["Canada"])
List4 = list(Population["Mexico"])

plt.plot(List1, List2, "o-r", label = "United States")
plt.plot(List1, List3, "o-g", label = "Canada")
plt.plot(List1, List4, "o-b", label = "Mexico")
plt.title("Population per year", fontdict = {"fontname" : "Times New Roman", "fontsize" : 20, "color" : "red"})
plt.xlabel("Year", fontdict = {"fontname" : "Times New Roman", "fontsize" : 20, "color" : "b"})
plt.ylabel("Population", fontdict = {"fontname" : "Times New Roman", "fontsize" : 20, "color" : "#0000FF"})
plt.xticks(List1)
#plt.xticks(List1[::2])
plt.xticks(List1[::3] + [2013])
plt.legend()
plt.show()


# In[ ]:




