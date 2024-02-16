class Triangle:

    def __init__(self, side_a, side_b, side_c):
        list_of_sides = [side_a, side_b, side_c]

        list_of_sides.sort()

        a, b, c = list_of_sides

        assert a > 0 and b > 0 and c > 0
        assert c < a + b

        self.a = side_a
        self.b = side_b
        self.c = side_c

    def perimeter(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimeter() / 2

        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
