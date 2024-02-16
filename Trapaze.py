class Trapezoid:
    def __init__(self, side_a, side_b, side_c, side_d):

        list_of_sides = [side_a, side_b, side_c, side_d]

        list_of_sides.sort()

        a, b, c, d = list_of_sides 

        assert a > 0 and b > 0 and c > 0 and d > 0

        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimetr(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        return 0.25*(self.b + self.a)/(self.b - self.a)((((-self.a + self.b + self.c + self.d)*(self.a - self.b + self.c - self.d)*(self.a - self.b - self.c + self.d))**0.5))