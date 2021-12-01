#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Selecting a Entree
Order = []
Entrees = ["Chicken", "Burger", "Wings", "Wrap"]
print(Entrees)
while True:
        entree = input("Enter the entree ")
        if entree.lower() == "chicken": 
            print(entree.capitalize() + " selected")
            Order.append(entree.capitalize())
            break
        elif entree.lower() == "burger":
            print(entree.capitalize() + " selected")
            Order.append(entree.capitalize())
            break
        elif entree.lower() == "wings":
            print(entree.capitalize() + " selected ")
            Order.append(entree.capitalize())
            break
        elif entree.lower() == "wrap":
            print(entree.capitalize() + " selected")
            Order.append(entree.capitalize())
            break
        else:
            print ("Input invalid")

#Selecting a Side
Sides = ["soup", "Fries", "Salad"]
print(Sides)
while True:
        side = input("Enter the side ")
        if side.lower() == "soup":
            print(side.capitalize() + " selected")
            Order.append(side.capitalize())
            break
        elif side.lower() == "fries":
            print(side.capitalize() + " selected")
            Order.append(side.capitalize())
            break
        elif side.lower() == "salad":
            print(side.capitalize() + " selected")
            Order.append(side.capitalize())
            break
        else:
            print ("Input invalid")


#Selecting a Drink
Drinks = ["Coffee", "Water", "Coke"]
print(Drinks)
while True:
        drink = input("Enter the drink ")
        if drink.lower() == "coffee":
            print(drink.capitalize() + " selected")
            Order.append(drink.capitalize())
            break
        elif drink.lower() == "coke":
            print(drink.capitalize() + " selected")
            Order.append(drink.capitalize())
            break
        elif drink.lower() == "water":
            print(drink.capitalize() + " selceted")
            Order.append(drink.capitalize())
            break
        else:
            print("input invalid")
#print(Order) testing if the list works
print(Order[0] + ", " + Order[1] + ", and " + Order[2] + " selected")


# In[ ]:




