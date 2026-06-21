# check if the list is already sorted


# example fixed list
# num_list = [1, 4, 6, 3 , 23,4]

# user defined list
num_list = list(map(int, input("Enter the numbers seperated by space : ").split()))

list = sorted(num_list)

if num_list == list:
    print(f"list is sorted")

else:
    print(f"list is not sorted")