def setNewPet():
  name, view, old, owner = input("Imy pitomca: "), input("Vid pitomsa: "), int(input("Vozrast: ")), input("Vladelec: ")
  while old <= 0:
    print("Vozrast ne moshet byt menshe 1 goda!")
    old = int(input("Vozrast: "))
  pets[name] = {
    "Vid pitomca": view,
    "Vozrast pitomca": old,
    "Imy vladelca": owner
  }
  return name

def getPet(name):
  if name in pets:
    str = ""
    for key, value in pets[name].items():
      nstr = f'{key}: {value}. '
      if key == 'Vid pitomsa':
        nstr = f'Это {value} po klichke "{name}". '
      elif key == 'Vozrast pitomca':
        post = 'let'
        if value <= 4 or value >= 21:
          i = value % 10
          if i == 1: post = 'god'
          elif i < 5: post = 'goda'
        nstr = f'{key}: {value} {post}. '
      str += nstr
    print(str)
  return False

getPet(setNewPet())