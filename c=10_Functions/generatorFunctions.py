# Generator functions

# Normal function : return
# Generator: yield

def numbers():
    yield 1
    yield 2
    yield 3

for n in numbers():
    print(n)




"""
Why use it?
--> Normal function : gives entire pizza
--> generator: gives slice by slice

--> It basically saves memory.

"""