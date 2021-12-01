#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy

def main(): #the main function created the 2 matrix's and call all other functions
    i    = 0
    j    = 0
    Mat1  = []
    Mat2 = []
    ROWS = 5 # Set to 5 after testing
    COLS = 5 # Set to 5 after testing

    print("Enter floats for Matrix 1")
    print("-------------------------")
    # Setting up the first matrix
    Row = []
    for i in range(0, ROWS):
        Row = []
        for j in range(0, COLS):
            while True:    #this will make sure a number is being entered or continue to ask for input, turns ints into floats
                num = input("Please enter a float: ") #initial input by user to be tested
                try:
                    val = float(num) #tests to see if a float turns ints to floats
                    break;
                except ValueError: #if not a float it will not break the loop and ask again for an input
                    print("Not a float, please enter a float!")
            Row.append(val)
        Mat1.append(Row) 

    print("Matrix 1: " + str(Mat1))
    print("")
    print("Enter floats for Matrix 2")
    print("-------------------------")
    # Setting up the second matrix, view the first to see what everything is doing
    Row = []
    for i in range(0, ROWS):
        Row = []
        for j in range(0, COLS):
            while True:
                num = input("Please enter a float: ")
                try:
                    val = float(num)
                    break;
                except ValueError:
                    print("Not a float, please enter a float!")
            Row.append(val)
        Mat2.append(Row)
    print("Matrix 2: " + str(Mat2))
    print("")
    print("Adding 2 lists with a function")
    print("------------------------------")

    def addList(a,b): #creating a function that will take in 2 arguments
        Mat3 = [] #setting up an empty list for the new matrix
        Mat3 = numpy.add(a,b) # will add the 2 arguments which will be matrixes
        print("Matrix 3: " +str(Mat3))

    addList(Mat1, Mat2) # calls the previous function with the 2 matrixes as arguments

    print("")
    print("Multiplying 2 lists with a function")
    print("-----------------------------------")

    def multList(a,b): #creating a function that will take in 2 arguments
        Mat4 = [] #setting up an empty list for the new matrix
        Mat4 = numpy.multiply(a,b) # will multiply the 2 arguments which will be the matrixes
        print("Matrix 4: " + str(Mat4))

    multList(Mat1, Mat2) # calls the previous function with the 2 matrixes as arguments

    print("")
    print("Multiply matrix by an integer")
    print("-----------------------------")

    def intMultList(a): # Creating a funtion that will take 1 arguement
        Mat5 = [] #setting up an empty list that will just be full of the user int to mult previous matrix
        Mat6 = [] #Setting up an empty list that will containt the multipled matrix, could of used the previous one but ohwell.
        ROWS = 5
        COLS = 5

        while True:
            num = input("Please enter a int: ") #initial input by user to be tested
            try:
                val = int(num) #test for int, will break loop if it is
                break;
            except ValueError: #if not a int it will not break the loop and ask again for an input
                print("Not an int, please enter a int!")

        for i in range(0, ROWS): # this sets up the matrix with only the user input int as every index.
            Row = []
            for j in range(0, COLS):        
                Row.append(val)
            Mat5.append(Row)
        Mat6 = numpy.multiply(a,Mat5)  #multiplies the argument matrix and a the int matrix  
        print("Matrix 5: " + str(Mat6))

    intMultList(Mat1) #calls the function with list as an argument. 


    print("")
    print("Divide matrix by an integer")
    print("-----------------------------")
    #This is the one I had trouple with and where I came up with the idea to make a matrix with the user input int and every index
    #I had tried quite a few things to divide but kept getting a typematcherror or something like that
    #so I decided to brute force it in my own way which was taking the user input putting it in a matrix
    #of the same size and using the divide function of numpy and it worked, so heck yeah. 
    def intDivList(a):
        Mat7 = [] #setting up an empty list that will just be full of the user int to mult previous matrix
        Mat8 = [] #Setting up an empty list that will containt the multipled matrix
        ROWS = 5
        COLS = 5

        while True:
            num = input("Please enter a int: ") #initial input by user to be tested
            try:
                val = int(num) #test for int, will break loop if it is
                break;
            except ValueError: #if not a int it will not break the loop and ask again for an input
                print("Not an int, please enter a int!")

        for i in range(0, ROWS):
            Row = []
            for j in range(0, COLS):        
                Row.append(val)
            Mat7.append(Row)
        Mat8 = numpy.divide(a,Mat7) #divides the arguement matrix and the int matrix 
        print("Matrix 6: " + str(Mat8))

    intDivList(Mat1) #calls the function with matrix as an argument. 

main()


# In[ ]:




