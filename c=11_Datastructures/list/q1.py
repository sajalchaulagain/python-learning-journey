# Print all positive and Negative elements seperately.


# Example fixed list
# numbers = [3, -1, 5, 2, -6, 7, -9, 8]


numbers = list(map(int, input("Enter numbers separated by space : ").split())) #taking input from user. 


#Empty list
pos_list = [] 
neg_list = []


for i in numbers:
    if i >= 0:
        pos_list.append(i)

    else:
        neg_list.append(i)

print(f"positive elements are {pos_list}")
print(f"positive elements are {neg_list}")



""" 
More shorter pythonic version: 
numbers = [3, -1, 5, 2, -6, 7, -9, 8]

pos_list = [i for i in numbers if i >= 0]
Negative_list = [i for i in numbers if i < 0]

print("Positive elements : ", pos_list)
print("Negative elements : ", neg_list)

"""

