# find the second gratest largest elements

# Example with fixed list
# a = [3, 4, 8, 2, 5, 9, 7]

#user define list
a = list(map(int, input("Enter the numbers list seperated by space : ").split()))

largest = a[0]
sec_largest = a[0]


for i in a:
    if i > largest:
        sec_largest = largest
        largest = i

    elif i > sec_largest:
        sec_largest = i

print(f"Second largest is {sec_largest}")


"""
Python has a shortcut using sorting:

sec_largest = sorted(set(a))[-2]
print(f"Second largest is {sec_largest}")

---> Here, set(a) removes duplicates, sorted() arranges them, 
and [-2] picks the second last (second largest).

"""


