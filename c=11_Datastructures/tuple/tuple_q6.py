# Instagram followers Ranking

users = (
    ("Sajal", 89),
    ("Rohit", 150),
    ("Virat", 300),
    ("Hardik", 80)
)

highest_user = ""
hightest_followers = 0

for i in users:

    username, followers = i

    if followers > hightest_followers:
        hightest_followers = followers
        hightest_user = username

print("Most Popular User")
print("----------------------------")
print(highest_user)
print(hightest_followers)