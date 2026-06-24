# Sum all values in a dictionary

marks = {
    "Math":86,
    "Science":85,
    "English":81,
    "Computer":90
}

total_marks = sum(marks.values())

print("Total Marks: ", total_marks)


# Alternative (using loop)

sales ={
    "Laptop":5,
    "Mouse": 12,
    "Keyboard":6,
    "Monitor":3
}


total = 0

for value in sales.values():
    total += value


print(total)