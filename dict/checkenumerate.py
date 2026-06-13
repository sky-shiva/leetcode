# A sample dictionary
user_roles = {"Alice": "Admin", "Bob": "Developer", "Charlie": "Tester"}

# Using enumerate on the dictionary
for index, key in enumerate(user_roles):
    print(f"Loop: {index} | Key: {key} | Value: {user_roles[key]}")
