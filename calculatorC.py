# implement a calculator class
# multiplication, division, additions, subtractions

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        pass

    def add(self):
        return self.num1+self.num2
        pass

    def subtract(self):
        return self.num2 - self.num1
        pass

    def multiply(self):
        return self.num1*self.num2
        pass

    def divide(self):
        return self.num2/self.num1
        pass

calculation_1 = Calculator(10, 94)
print(calculation_1.add())
print(calculation_1.subtract())
print(calculation_1.multiply())
print(calculation_1.divide())