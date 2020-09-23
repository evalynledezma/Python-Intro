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



