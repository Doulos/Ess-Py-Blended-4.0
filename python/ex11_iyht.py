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


class BunchOfPixels:
    def __init__(self, bunch):
        assert isinstance(bunch, list)
        for c in bunch:
            assert isinstance(c, Pixel)
        self._bunch = bunch

    def gen(self):
        for c in self._bunch:
            yield c

    __iter__ = gen


pixels = [Pixel(n, n, c) for n, c in zip(range(7), [0, 1, 5, 2, 1, 4, 7])]
bunch = BunchOfPixels(pixels)

for p in bunch:
    print(p)

print("\nCreate list with complementary Pixel")
invert = [-p for p in bunch]
for p in invert:
    print(p)

print("\nFilter green color (6)")
s = filter(lambda c: c.get_color() != 6, invert)
for p in s:
    print(p)
