# find the greatest element and print its index.


# Example of fixed list.
# a = [1, 2, 4, 5, 3, 8, 9, 7, 6, 0]

# user input value
a = list(map(int, input("Enter the number seperated by space : ").split()))

largest = a[0]
index = 0

for i in range(len(a)):
    if a[i] > largest:
        largest = a[i]
        index = i

print(f"largest value is {largest} at index {index}")


"""

Another method: 
largest = max(a)
index = a.index(largest)
print(f"largest value is {largest} at index {index})


"""
