sentence = 'The quick brown fox jumped over the lazy dog'

sentence_two = 'That is my dog\'s bowl'

sentence_three = "That is my dog's bowl"

sentence_four = "Tiffany said, \"That is my dog's bowl\""


# sentence = 'The quick brown fox jumped'
# sentence -> variable
# 'The quick brown fox jumped' -> string
# = -> assignment

sentence = 'The quick brown fox jumped'
sentence_two = sentence.upper()

print(sentence)
print(sentence_two)

sentence = 'the quick brown fox jumped'.capitalize()
print(sentence)

sentence = 'the quick brown fox jumped'.title()
print(sentence)

sentence = 'the Quick Brown fox jumped'
print(sentence.lower()) 


# [start:stop:step]
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1 
#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6  (slice position)
#    0   1   2   3   4   5    (index position)
# The quick brown fox jumped
# T => 0
# h => 1
# e => 2
# '' => 3


starter_sentence = 'The quick brown fox jumped'

new_sentence = 'The' + starter_sentence[3:]
#assumes blank after colin goes to end
print(new_sentence)


# Heredoc

#must use different syntax than regular quotes because of empty line
content = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
""".strip()
# strip takes out any newline characters
print(content)


import operator
from functools import reduce

"""
dynamic_reducer([1, 2, 3], '+')
dynamic_reducer([1, 2, 3], '-')
dynamic_reducer([1, 2, 3], '*')
dynamic_reducer([1, 2, 3], '/')
"""

def dynamic_reducer(collection, op):

  operators = {
      "+": operator.add,
      "-": operator.sub,
      "*": operator.mul,
      "/": operator.truediv
  }

  return reduce((lambda total, element: operators[op](total, element)) ,collection)



print(dynamic_reducer([1, 2, 3,] '+'))
print(dynamic_reducer([1, 2, 3,] '-'))
print(dynamic_reducer([1, 2, 3,] '*'))
print(dynamic_reducer([1, 2, 3,] '/'))


# # Heredoc

# content = """
# Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

# Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

# Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
# """
# print(repr(content))

long_string = '\nNullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.\n\nVestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.\n\nInteger posuere erat a ante venenatis dapibus posuere velit aliquet.\n'

print(long_string)


name = 'Kristine'
product = 'Python elearning course'

email_content = f"""
Hi {name}

Thank you for purchasing {product}
Regards,

Sales Team
"""

print (email_content)


# python's string interpolation
name = 'Kristine'
age = 12
product = 'Python eLearning course'

greeting = "Product Purchase: {2} - Hi {0},  you are listed as {1}  years old - {3}...".format(name, age, product, 'Jordan')

print(greeting)

sentence = 'The quick brown fox jumped over the lazy dog.'



# Find, Index, and In

sentence = 'The quick brown fox jumped over the lazy dog.'

query = sentence.find('oops')
query_two = sentence.index('oops')

print(query)
print(query_two)

query = 'oops' in sentence

print(query)


sentence = 'The quick brown fox jumped over the lazy dog'

sentence = 'New Value'

print(sentence)


# netagive index values

sentence = 'The quick brown fox jumped over the lazy dog.'

print(sentence[-1])


# strip lstrip rstrip
url = 'https://google.com'

# print(url.strip('https://'))

url = url.lstrip('https://')
url = url.rstrip('.com/')
url = url.strip()

print(url)


# partition function
heading = "Python: An Introduction"

header, _, subheader = heading.partition(': ')

print(header)
print(subheader)


# split function
tags = 'python,coding,programming,development'

list_of_tags = tags.split(',')
list_of_tags = tags.split()

print(list_of_tags)

heading = "Python: An Introduction"

heading, subheading = heading.split(': ')

print(heading)
print(subheading)


# strings numbers or alphanumeric characters
api_data ='5'
greeting = 'Hi there'

# print(api_data.isalpha())
# print(greeting.isalpha())

print(api_data.isnumeric())
print(greeting.isalpha())


