# An instance method is a function that belong to an object.

class Pokemon():
    def __init__(self,name,specialty,health = 100):
        self.name = name
        self.specialty = specialty
        self.health = health

    def roar(self):
        print("Raaaarr")

    def describe(self):
        print(f"I am {self.name}. I am a {self.specialty} pokemon!")

    def take_damage(self,amount):
        self.health -= amount



squirtle = Pokemon("Squirtle","Water")
charmander = Pokemon("Charmander","Fire",110)

squirtle.roar()
charmander.roar()

print()

squirtle.describe()
charmander.describe()

print()

squirtle.take_damage(40)
print(squirtle.health)