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
 