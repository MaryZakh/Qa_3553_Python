class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says:Woof!"

    def sleep(self):
        return f"{self.name} is sleeping"

dog1 = Dog("Rex")
dog2 = Dog("Max")

print(dog1.bark())
print(dog2.sleep())