import math

class Calculator:
    result = 0

    def __init__(self):
        self.result = 0
        pass

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

    def multiply(self, a, b):
        self.result = a * b
        return self.result

    def divide(self, a, b):
        self.result = a / b
        return self.result

    def square(self, a):
        self.result = a * a
        return self.result

    def square_root(self, a):
        self.result = math.sqrt(a)
        return self.result
