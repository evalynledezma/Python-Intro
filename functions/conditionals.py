# conditionals
age  = 101

if age < 25:
  print(f"I'm sorry, you need to be at least 25 years old")
elif age > 100:
  print(f"I'm sorry, {age} is too old to rent a car")

else: 
  print(f"You're good to go, {age} fits in the range to rent a car")


  # challenge
  answer = False

  if 2 < 3:
    answer = True
  
  print(answer)


# practice
  def watermelonParty():

    watermelons = 49

    if watermelons > 50:
      print(True)
    else:
      print(False)

watermelonParty()


# practice
def kid():
  age = 16

  if age == 15:
    print("Can get a permit, but can't get a license")
  elif age > 15:
    print("You could get your license!")
  else: 
    print("Sorry you're too young to drive")
kid()


# ternary operator
role = 'admin'

auth = 'can access' if role == 'admin' else 'cannot access'

print(auth)

# or

if role == 'admin':
  'can access'
else:
  'cannot access'


# practice
# def ageVerification(age):
#   age = 25

#   if age > 25:
#     print('can rent a car')
#   else:
#     print("can't rent a car")
# ageVerification(25)


def ageVerification(age):
  print('can rent a car' if age >= 25 else "can't rent a car")

ageVerification(25)


# # List of comparison operators
# == Equality
# != Inequality
# <> Inequality (deprecated)
# >  Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to

# different syntax for conditionals
# and
# or and
# or 
# and not

# how to build compound conditionals
username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'jonsnow' and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


if username == 'jonsnow' or password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


logged_in = True
standard_user = False

if logged_in and not standard_user:
  print('You can access the admin dashboard')
else:
  print('You can only access the standard dashboard')

# practice
a = 200
b = 33
c = 500
if a == 200 and a > b:
  print('Both conditions are True')

a = 200
b = 33
c = 500
if  a == 200 or a > b:
  print('At least one of the conditions is True')