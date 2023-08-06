import math


class Triangle:
    def __init__(self, cat1, cat2):
        self.cat1 = cat1
        self.cat2 = cat2

    def calculate_hypotenuse(self):
        return math.sqrt(self.cat1**2 + self.cat2**2)


side1 = int(input())
side2 = int(input())

h = Triangle(side1, side2)
print(h.calculate_hypotenuse())
