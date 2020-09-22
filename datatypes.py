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



# nested lists and multipele data types in a list  
users = ['Eva', 'Sam', 'Dan']

ids = [1, 2, 3]

mixed_list = [42, 10.3, 'Altuve', users]
# ^^^ dont do that ^^^

print(mixed_list)

user_list = mixed_list.pop()

print(user_list)
print(mixed_list)

nested_lists = [[123], [234], [345]]


# list query proxesses: len(), negative indexes, and index()
tags = ['python', 'development', 'tutorials', 'code']

number_of_tags =len(tags)
last_item = tags[-1]
index_of_last_item = tags.index(last_item)

print(number_of_tags)
print(last_item)
print(index_of_last_item)


# sort lists in python

tags = ['python', 'development' 'tutorials', 'code']

print(tags)

tags.sort()

print(tags)

# ^^^ alphabetics ^^^

tags.sort(reverse=True)

print(tags)

totals = [234, 5, 63456, 45]
totals.sort(reverse=True)
print(totals)


# using join function to build a URL query string   
# https://www.google.com/search?q=python+development+tutorial

uri = 'https://www.google.com/search?q='
tags = ['python', 'development', 'tutorial']
formatted_tags = '+'.join(tags)
query_uri = f'{uri}{formatted_tags}'

print(query_uri)


# ranges in lists
tags = ['python', 'development', 'tutorials', 'code']

tag_range = tags[2:]
tag_range = tags[0:2]
tag_range = tags[:2]
tag_range = tags[0:-1]

print(tag_range)


