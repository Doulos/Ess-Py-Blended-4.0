class Coord:
    def __init__(self, x, y):
        self.setxy(x, y)

    def setxy(self, x, y):
        self.setx(x)
        self.sety(y)

    def getxy(self):
        return (self.getx(), self.gety())

    def setx(self, x):
        self._x = x

    def sety(self, y):
        self._y = y

    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def __add__(self, other):
        return Coord(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        return Coord(self._x - other._x, self._y - other._y)


class Pixel(Coord):
    _name = [
        "black",
        "red",
        "yellow",
        "blue",
        "orange",
        "purple",
        "green",
        "white",
    ]

    def __init__(self, x, y, c):
        super().__init__(x, y)
        self.set_color(c)

    def set_color(self, c):
        if 0 <= c <= 7:
            self._c = c
        else:
            raise ValueError

    def get_color(self):
        return self._c

    def __str__(self):
        return f"{(self._x, self._y)}, c={self._c}<{Pixel._name[self._c]}>"

    def __repr__(self):
        return f"Pixel({self._x},{self._y},{self._c})"

    def __neg__(self):
        return Pixel(self._x, self._y, 7 - self._c)

    def __add__(self, other):
        r = super().__add__(other)
        return Pixel(r._x, r._y, self._c | other._c)

    def __sub__(self, other):
        r = super().__sub__(other)
        return Pixel(r._x, r._y, self._c & other._c)


p = Pixel(1, 2, 3)
print(p)
print(repr(p))

assert p.get_color() == 3
p.set_color(2)
assert p.get_color() == 2
assert (-p).get_color() == 5
p.setxy(3, 4)
print(-p)

print("\nTest Pixel addition/substraction:")
p1 = Pixel(1, 2, 3)
p2 = Pixel(3, 4, 1)
print(f"{p1 = }")
print(f"{p2 = }")
r1 = p1 + p2
r2 = p1 - p2
print("r1=", r1)
print("r2=", r2)
