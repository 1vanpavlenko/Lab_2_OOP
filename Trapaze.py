class Trapezoid:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimetr(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        return 0.25*(self.b + self.a)/(self.b - self.a)((((-self.a + self.b + self.c + self.d)*(self.a - self.b + self.c - self.d)*(self.a - self.b - self.c + self.d))**0.5))