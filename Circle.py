from math import pi as p

class Circle:
    def __init__(self, r):

        assert r > 0

        self.r = r

    def perimetr(self):
        return 2 * p * self.r

    def area(self):
        return p * self.r ** 2