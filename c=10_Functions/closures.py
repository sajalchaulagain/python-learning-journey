# closures

def multiplier(x):
    def multiply(y):
        return x*y
    
    return multiply

double = multiplier(2)

print(double(10))