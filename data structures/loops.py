# loops for lists, tuples, and dictionaries
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']
players = ('Altuve', 'Bregman', 'Correa', 'Gattis')

for player in players:
  print(player)

players = {
  '2b': 'Altuve',
  '3b': 'Bregman',
  'ss': 'Correa',
  'dh': 'Gattis'
}

for position, player in players.items():
  print('Position', position)
  print('Player', player)


# challenge
user = {
  'username': 'evazema',
  'email': 'eva@ledezma.org',
  'phone': '801-123-4567'
}

for key, value in user.items():
  print('Key => '+ key)
  print("Value => " + value)

for key in user.keys():
  print('Key => ' + key)

for value in user.values():
  print('Value => ' + value)


# loop through characters of a string
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for letter in alphabet:
  print(letter)


# looping over ranges
for num in range(6,16):
  print(num)

for num in range(10,31,2):
  print(num)


# continur and break in loops
usernames = [
  'jon',
  'tyrion',
  'theon',
  'cersei',
  'sansa',
]

for username in usernames:
  if username == 'cersei':
    print(f'Sorry, {username}, you are not allowed')
    continue
  else:
    print(f'{username} is allowed')

for username in usernames:
  if username == 'cersei':
    print(f'{username} was found at index {usernames.index(username)}')
    break
  print(username)


  # challenge
  cereals = [
  'frosted flakes',
  'shredded wheat',
  'coco pebbles',
]
for cereal in cereals:
  if cereal == 'shredded wheat':
    print(f'shredded wheat is gross!')
    continue
  print(f'{cereal} is allowed')


# while Loop  
nums = list(range(1, 100))

while len(nums) > 0:
  print(nums.pop())

def guessing_game():
  while True:
    print('What is your guess?')
    guess = input()

    if guess == '42':
      print('You correctly guessed it!')
      return False
    else:
      print(f"No, {guess} isn't the answer, please try again\n")

guessing_game()


# challenge
dog = ('tom', 'sam', 'bella', 'thanos')

data = 0
while data < len(dog):
  print(dog[data])
  data = data + 1


# combine and flatten lists with for/ in loop
legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

raw_db = [legacy_customers, new_customers]

print(raw_db)

for legacy_customer in legacy_customers:
  new_customers.append(legacy_customer)

print(new_customers)


# challenge
numbers = [1,2,3,4,5,6]
results = []

for number in numbers:
  results.append(number + 1) 

print(results) 


# using list comprehension
num_list = range(1, 11)
cubed_nums = []

for num in num_list:
  cubed_nums.append(num ** 3)

cubed_nums = [num ** 3 for num in num_list]

print(cubed_nums)

even_numbers = []

for num in num_list:
  if num % 2 == 0:
    even_numbers.append(num)

even_numbers = [num for num in num_list if num % 2 == 0]

print(even_numbers)