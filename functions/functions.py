# heading generator function
def heading_generator(title, heading_type):
  return (f'<h{heading_type}>{title}</h{heading_type>}')

print(heading_generator('Greeting', '1'))

print(heading_generator('Hi there', '3'))


# basic syntax for functions 
def full_name(first, last):
  print(f'{first} {last}')


full_name('Kristine', 'Hudgens')

def auth(email, password):
  if email == 'kristine@hudgens.com' and password == 'secret':
    print('Authorized')
  else:
    print('Not Authorized')


full_name()


def hundred():
  for num in range(1, 101):
    print(num)

hundred()


def counter(max_value):
  for num in range(1, max_value):
    print(num)

counter(1000)


# practice
def greeting():
  print('hello')

greeting()


def greeting(greeting_phrase, name):
  print(greeting_phrase, name)

greeting('hello', 'eva')


def sum_two_numbers(num_one, num_two, num_three):
  print(num_one + num_two - num_three)

sum_two_numbers(4, 4, 1)


# return value from a function
def full_name(first, last):
  print(f'{first} {last}')


full_name('Kristine', 'Hudgens')

# practice
def sum_two_numbers(num_one, num_two):
  return num_one + num_two


result = sum_two_numbers(1,2)
print(result)


# nest functions in parent functions
def greeting(first, last):
  def full_name():
    return f'{first} {last}'

  print(f'Hi {full_name()}!')


greeting('Kristine', 'Hudgens')


# guide to default arguments
def greeting(name = 'Guest'):
  print(f'Hi {name}!')

greeting()
greeting('Kristine')

# Nope
def some_function(collection = []):
  collection.append(1)
  print(id(collection))
  return collection


print(some_function())
print(some_function())


# utilize named function arguments
def full_name(first, last):
  print(f'{first} {last}')


full_name('Kristine', 'Hudgens')
full_name(first = 'Kristine', last = 'Hudgens')
full_name(last = 'Hudgens', first = 'Kristine')


# function arguments unpacking
def greeting(*args):
  print('Hi ' + ' '.join(args))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting(*names):
  print('Hi ' + ' '.join(names))


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting(time_of_day, *args):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting('Morning', 'Tiffany', 'Hudgens')


# keyword arguments
def greeting(**kwargs):
  print(kwargs)


greeting()
greeting(first = 'Kristine', last = 'Hudgens')

def greeting(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest!')


greeting()
greeting(first = 'Kristine', last = 'Hudgens')


# combine all arguments
def greeting(time_of_day, *args, **kwargs):
  print(f"Hi {' '.join(args)}, I hope that you are having a great {time_of_day}")

  if kwargs:
    print('Your tasks for the day are:')
    for key, val in kwargs.items():
      print(f"{key} => {val}")


greeting('Morning',
          'Kristine',
          first = 'Empty dishwasher',
          second = 'Take pupper outside',
          third = 'Math homework')


