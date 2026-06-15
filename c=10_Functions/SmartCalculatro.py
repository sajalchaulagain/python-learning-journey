# Advance Example.

# Smart Calculator

def smart_calculator(operation):
    def calculate(a,b):
        if operation == "+":
            return a+b
        
        elif operation == "-":
            return a-b
        
        elif operation == "*":
            return a*b
        
        elif operation == "/":
            return a/b
        
    return calculate

add = smart_calculator("+")

print(add(10,5))