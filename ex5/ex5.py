day1_users = ["alice", "bob", "charlie", "david", "alice", "eva"]
day2_users = ["bob", "frank", "eva", "george", "charlie", "charlie"]

set_days1 = set(day1_users | day2_users)
print(set_days1)