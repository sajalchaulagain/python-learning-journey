# Recursive Function --> function calling itself

def countdown(n):
    if n == 0:
        print("Boom")
        return
    
    print(n)
    countdown(n-1)

countdown(5)