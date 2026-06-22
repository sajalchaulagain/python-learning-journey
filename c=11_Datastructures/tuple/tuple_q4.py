# online shopping product catalog

products = (
    ("Laptop", 70000),
    ("Mouse", 1200),
    ("keyboard", 2500), 
    ("headphone", 3500)
)


print("Available products")
print("-----------------------")


for i in products : 

    #tuple unpacking
    name, price = i
    print(f"{name} - Rs.{price}")