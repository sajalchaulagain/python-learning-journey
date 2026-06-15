# Higher order function : function that accept other functions. 

def shout(text):
    return text.upper()

def greet(func):
    print(func("hello"))

greet(shout)