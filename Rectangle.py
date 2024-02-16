class Ractangle:
    def __init__(self, side_a, side_b):

        list_of_sides = [side_a, side_b]

        list_of_sides.sort()

        a, b = list_of_sides

        assert a > 0 and b > 0

        self.a = a
        self.b = b

    def perimetr(self):
        return self.a + self.b

    def area(self):
        return self.a * self.b