class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, number):
        self.result += number
        return self.result

    def reset(self):
        self.result = 0

calc = Calculator()
print(calc.add(5))
print(calc.add(10))
calc.reset()
print(calc.result)
        