# Count the frequncy of each element in a list using a dictionary

likes = [
    "Sajal",
    "Ram",
    "Sajal",
    "Hari",
    "Sajal",
    "Ram",
    "Sajal",
]

frequency = {}

for user in likes:
    frequency[user] = frequency.get(user, 0) + 1

print(frequency)