#!/usr/bin/env python
# coding: utf-8

# In[13]:


from datetime import datetime
tupday = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
lday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = lday[datetime.today().weekday()]

if day in tupday:
    print(day + " is in tuple")
else:
    print("what")


# In[ ]:




