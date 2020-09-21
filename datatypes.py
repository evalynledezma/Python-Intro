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


# Advanced Techniques for Implementing Ranges and Slices
tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

tag_range = tags[1:-1:2]
tag_range = tags[::-1]

print(tag_range)

tags.sort(reverse=True)

print(tags)


# sorted Function
sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices, reverse=True)

print(sorted_list)


# median in a python list with odd number of numbers
import math

"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sorted_list = sorted(sale_prices)
num_of_sales = len(sorted_list)
half_slice = math.floor(num_of_sales/2)
first_sales_items = sorted_list[:half_slice]
last_sales_items = sorted_list[-(half_slice):]
median = sorted_list[half_slice:(half_slice + 1)]

print(sorted_list)
print(num_of_sales)
print(first_sales_items)
print(last_sales_items)
print(median)


# slice class to store slices
tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
]

print(tags[1:4:2])

slice_obj = slice(1, 4, 2)

print(slice_obj.start)
print(slice_obj.stop)
print(slice_obj.step)

print(tags[slice_obj])


# adding to lists with in place and copy
tags = ['python', 'development', 'tutorials', 'code']

# Nope
tags[-1] = 'Programming'

# In Place
tags.extend('Programming')
tags.extend(['Programming'])

# New List
new_tags = tags + ['Programming']

print(new_tags)

print(tags)


# dictionaries
players = {
  "ss": "Correa",
  "2b": "Altuve",
  "3b": "Bregman",
  "DH": "Gattis",
  "OF": "Springer",
}

second_base = players['2b']
designated_hitter = players['DH']

print(designated_hitter)


# nested collections
teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

astros = teams['astros']
print(astros)
print(teams['angels'])
print(teams['yankees'])


# add new key value pairs
teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
}

teams['red sox'] = ['Price', 'Betts']

print(teams)


# get function
teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
}

featured_team = teams.get('yankees', 'No featured team')

print(featured_team)