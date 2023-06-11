number = int(input("number: "))

def getStatus(numb):
  str = '';
  if numb == 0: return 'Nulevoe chislo'
  if numb % 2 == 0:
    if numb < 0: str = 'Otrisatelnoe chetnoe chislo'
    else: str = 'Poloschitelnoe chetnoe chislo'
  else:
    if numb < 0: str = 'Otrisatelnoe chetnoe chislo'
    else: str = 'Poloschitelnoe chetnoe chislo'
  return str

print("Result:", getStatus(number))