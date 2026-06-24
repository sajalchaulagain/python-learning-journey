# Merge Two Dictionaries into one


# Method 1 

student = {
    "name":"Sajal",
    "age":20
}

college = {
    "College Name": "Texas College of Management & IT",
    "faculty":"Computer Science"
}

merged = {**student, **college}

print(merged)



# Method 2 (using update())

customer = {
    "name":"sajal",
    "email":"chaulagainsajal94@gmail.com"
}

order = {
    "product":"Laptop",
    "price":50000
}

customer.update(order)

print(customer)