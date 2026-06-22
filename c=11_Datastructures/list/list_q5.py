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



"""
Another Methode as well..

a = [10, 20, 30, 40, 60, 50]

for i in range(len(a)-1):
    if a[i] > a[i+1]:
        print("your list is not sorted")
        break
        
    else:
        print("your list is sorted")
"""