# Generator functions act just like regular functions with just one difference that they use the Python yieldkeyword instead of return .
# A generator function is a function that returns an iterator. 

def test_sequence():
    num = 0
    while num<10:
        yield num
        num += 1
for i in test_sequence():
       print(i, end=",")
    
#Reverse a string
def reverse_str(test_str):
    length = len(test_str)
    for i in range(length - 1, -1, -1):
        yield test_str[i]
for char in reverse_str("Trojan"):
    print(char,end =" ")
    
    
# Decorators are a very powerful and useful tool in Python since it allows programmers to modify/control the behavior of function or class. 
# Decorators are usually called before the definition of a function you want to decorate

def lowercase_decorator(function):
    def wrapper():
        func = function()
        make_lowercase = func.lower()
        return make_lowercase
return wrapper
def split_string(function):
    def wrapper():
        func = function()
        split_string = func.split()
        return split_string
return wrapper
@split_string
@lowercase_decorator
def test_func():
    return 'MOTHER OF DRAGONS'
test_func()
