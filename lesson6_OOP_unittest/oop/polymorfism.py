class Cat:
    def make_sound(self):
        return "Meow"

class Dog:
    def make_sound(self):
        return "Woof"

animals = [Cat(),Dog()]
for animal in animals:
    print(animal.make_sound())