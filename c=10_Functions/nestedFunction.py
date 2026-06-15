# Nested function: function inside function

def outer():
    def inner():
        print("Inside inner")

    inner()

outer()