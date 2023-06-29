import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length(self):
        return 2 * math.pi * self.radius

    def square(self):
        return math.pi * self.radius ** 2


circ = Circle(5)
print(circ.square(), circ.length())
