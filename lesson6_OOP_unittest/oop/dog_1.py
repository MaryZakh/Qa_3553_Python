class Dog:
    species = "Canis familiaris"

    def __init__(self,name):
        self.name = name

dog1 = Dog("Bobby")
dog2 = Dog("Ocean")

print(dog1.species,dog1.name)
print(dog2.species,dog2.name)

Dog.species = "Wolf"

print(dog1.species,dog1.name)
print(dog2.species,dog2.name)
