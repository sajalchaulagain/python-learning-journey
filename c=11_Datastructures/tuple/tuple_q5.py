# Cricket scoreboard Example

#batsman information

players = (
    ("Rohit Sharma", 106),
    ("Virat Kohli", 70),
    ("KL Rahul", 45),
    ("Hardik Pandya", 23)
)

print("Cricket scoreboard")
print("--------------------")


total_runs = 0

for i in players :

    # unpack tuple

    name, runs = i

    print(f"{name} : {runs}")


    # Add runs to total
    total_runs += runs


print("----------------------------")
print("Total Runs: ", total_runs)