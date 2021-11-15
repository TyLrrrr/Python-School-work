#!/usr/bin/env python
# coding: utf-8

# In[5]:


def multiply(*args):
    result = 1
    for i in args:
        result *= i
    print(result)
multiply(2,3)
multiply(3,4,6,7)
multiply(2.4,2.7,5.6)

#using *args to take multiple parameters


# In[18]:


from multipledispatch import dispatch
import math

class shape:
    def __init__(self):
        pass
    
    #@dispatch(int)
    #def area(self,side):
    #    return side*side
    
    @dispatch(int, int)
    def area(self, height, width):
        return width* height
    
    @dispatch(float, str)
    def area(self, param, shapeType):
        if shapeType == "circle":
            return math.pi * param * param
        if shapeType == "square":
            return  param * param
    
x = shape()
print(x.area(5,5))
print(x.area(8,9))
print(x.area(10.0, "square"))
print(x.area(10.0, "circle"))
        
#function overloading: static binding at compile time, 
#the ability of the function to behave in different ways depend on the number of parameters passed to it


# In[ ]:




