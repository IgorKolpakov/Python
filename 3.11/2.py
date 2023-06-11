import collections

pets = {}

def get_pet(ID):
  return pets[ID] if ID in pets.keys() else False

def get_suffix(value):
  post = 'let'
  if value <= 4 or value >= 21:
    i = value % 10
    if i == 1: post = 'god'
    elif i < 5: post = 'goda'
  return f'{value} {post}'

def create():
  try:
    last = collections.deque(pets, maxlen=1)[0]
  except:
    last = 0
  
  pets[last + 1] = update()
  print(f'{last + 1} zapis sozdana!')

def read(name, obj):
  str = ""

  for key, value in obj.items():
    nstr = f'{key}: {value}. '
    if key == 'Vid pitomca':
      nstr = f'Eto {value} po klichke "{name}". '
    elif key == 'Vozrast pitomca':
      nstr = f'{key}: {get_suffix(value)}. '
    str += nstr
  print(str)

def update():
  name, view, old, owner = input("Imy pitomca: "), input("Vid pitomca: "), int(input("Vozrast: ")), input("Vladelec: ")
  while old <= 0:
    print("Vozrast ne moshet byt menshe 1 goda!")
    old = int(input("Vozrast: "))

  obj = {}
  obj[name] = {
    "Vid pitomca": view,
    "Vozrast pitomca": old,
    "Imy vladelca": owner
  }
  return obj

def delete(ID):
  pet = get_pet(ID)
  if pet:
    del pets[ID]
    print('zapic udalena!')
  else: print('Pitomca s takim ID ne suchestvuet!')

def pets_list():
  print('spisok vseh pitomcev:')

  for key in pets:
    pet = get_pet(key)
    print(f'[ID: {key}]: ', end='')
    if pet:
      name = list(pet.keys())[0]
      read(name, pet[name])

command = ''
while command != 'stop':
  command = input('> ')
  if command == 'create':
    create()
  elif command == 'list':
    pets_list()
  elif command == 'get':
    pet = get_pet(int(input('ID: ')))
    if pet:
      name = list(pet.keys())[0]
      read(name, pet[name])
    else: print('Pitomca s takim ID ne suchestvuet!')
  elif command == 'update':
    id = int(input('ID: '))
    pet = get_pet(id)
    if pet:
      name = list(pet.keys())[0]
      pets[id] = update()
    else: print('Pitomca s takim ID ne suchestvuet!')
  elif command == 'delete':
    id = int(input('ID: '))
    delete(id)