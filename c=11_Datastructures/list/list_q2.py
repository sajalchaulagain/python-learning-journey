# find the mean (average) of all list elements.

# Example fixed list
# num_list = [10, 20, 30, 22]


num_list = list(map(int, input("Enter the number seperate by space : ").split()))   #--> for taking user input


average = sum(num_list) / len(num_list)

print(f"The average of {num_list} is {average}")


"""

Another method: 

num_list = [10, 20, 30, 22]
sum = 0

for i in num_list:
    sum = sum + i

avg = sum / len(l)

print(f"average is {avg}")

"""