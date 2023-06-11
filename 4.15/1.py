class Transport:
   def __init__(self, name, max_speed, mileage):
      self.name = name
      self.max_speed = max_speed
      self.mileage = mileage

   def getInfo(self):
      print(f'Nazvanie avto {self.name} Skorost: {self.max_speed} Probeg: {self.mileage}')

Autobus = Transport('Renaul Logan', 180, 12)
Autobus.getInfo()