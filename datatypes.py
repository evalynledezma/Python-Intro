# making lists
"""
User Database Query
Kristine
Tiffany
Jordan
"""

users = ['Kristine', 'Tiffany', 'Jordan']

print(users)

users.insert(1, 'Anthony')

print(users)

users.append('Ian')

print(users)

print([users[2]])

users[4] = 'Brayden'

print(users)


# remove elements from a list
users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan')

print(users)

popped_user = users.pop()

print(popped_user)
print(users)

del users[0]

print(users)
