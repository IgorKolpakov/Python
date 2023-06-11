class Transport:
   def __init__(self, name, max_speed, mileage):
      self.name = name
      self.max_speed = max_speed
      self.mileage = mileage

   def seating_capacity(self, capacity):
      return f"Vmestimost odnogo avtobusa {self.name}  {capacity} pacashirov"


class Autobus(Transport):
   def __init__(self, name, max_speed, mileage):
      super().__init__(name, max_speed, mileage)

   def seating_capacity(self, capacity=50):
      return f"Vmestimost odnogo avtobusa {self.name}  {capacity} pacashirov"



_bus = Autobus('Renaul Logan', 180, 12)
print(_bus.seating_capacity())