# The problem with method overloading in Python is that we may overload the methods
# but can only use the latest defined method. 

******************************************************************************
def product(a, b):
    p = a * b
    print(p)
 
# Second product method
# Takes three argument and print their
# product
 
 
def product(a, b, c):
    p = a * b*c
    print(p)
 
# Uncommenting the below line shows an error
# product(4, 5)
 
 
# This line will call the second product method
product(4, 5, 5)
******************************************************************************

# Function to take multiple arguments
def add(datatype, *args):
 
    # if datatype is int
    # initialize answer as 0
    if datatype == 'int':
        answer = 0
 
    # if datatype is str
    # initialize answer as ''
    if datatype == 'str':
        answer = ''
 
    # Traverse through the arguments
    for x in args:
 
        # This will do addition if the
        # arguments are int. Or concatenation
        # if the arguments are str
        answer = answer + x
 
    print(answer)
 
 
# Integer
add('int', 5, 6)
 
# String
add('str', 'Hi ', 'Geeks')

******************************************************************************
def add(a=None, b=None):
    # Checks if both parameters are available
    # if statement will be executed if only one parameter is available
    if a != None and b == None:
        print(a)
    # else will be executed if both are available and returns addition of two
    else:
        print(a+b)
 
 
# two arguments are passed, returns addition of two
add(2, 3)
# only one argument is passed, returns a
add(2)
******************************************************************************
### By Using Multiple Dispatch Decorator 
from multipledispatch import dispatch
 
# passing one parameter
 
 
@dispatch(int, int)
def product(first, second):
    result = first*second
    print(result)
 
# passing two parameters
 
 
@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)
 
# you can also pass data type of any value as per requirement
 
 
@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)
 
 
# calling product method with 2 arguments
product(2, 3)  # this will give output of 6
 
# calling product method with 3 arguments but all int
product(2, 3, 2)  # this will give output of 12
 
# calling product method with 3 arguments but all float
product(2.2, 3.4, 2.3)  # this will give output of 17.985999999999997
******************************************************************************

In Backend, Dispatcher creates an object which stores different implementation and on runtime, 
it selects the appropriate method as the type and number of parameters passed
