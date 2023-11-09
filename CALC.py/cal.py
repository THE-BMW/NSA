import math

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, number):
        self.result += number
        return self.result

    def subtract(self, number):
        self.result -= number
        return self.result

    def multiply(self, number):
        self.result *= number
        return self.result

    def divide(self, number):
        if number == 0:
            raise ValueError("Division by zero is not allowed.")
        self.result /= number
        return self.result

    def root(self, degree):
        if degree == 0:
            raise ValueError("Root degree of 0 is not allowed.")
        self.result = self.result ** (1 / degree)
        return self.result

    def clear(self):
        self.result = 0
        return self.result


calculator = Calculator()

while True:
    operation = input("Choose operation (add, subtract, multiply, divide, root, clear): ")
    number = 0

    if operation in ['add', 'subtract', 'multiply', 'divide', 'root']:
        number = float(input("Enter a number: "))

    if operation == 'add':
        print(calculator.add(number))
    elif operation == 'subtract':
        print(calculator.subtract(number))
    elif operation == 'multiply':
        print(calculator.multiply(number))
    elif operation == 'divide':
        print(calculator.divide(number))
    elif operation == 'root':
        print(calculator.root(number))
    elif operation == 'clear':
        print(calculator.clear())
    else:
        print("Unknown operation. Please choose a valid operation.")