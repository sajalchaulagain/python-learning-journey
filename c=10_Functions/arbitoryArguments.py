# Arbitory  Arguments (*args) --> what if we don't know how many inputs will come?

def total(*numbers):
    print(sum(numbers))

total(1,4,5,3)
total(34,456,5)


# Tricks : *args means bring everyone inside the bus.