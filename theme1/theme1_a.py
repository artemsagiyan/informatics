import math


class Triangle:
    def __init__(self, cat1, cat2):
        self.cat1 = cat1
        self.cat2 = cat2

    def calculate_hypotenuse(self):
        return math.sqrt(self.cat1**2 + self.cat2**2)
