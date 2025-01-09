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

    def add(self, other):
        return Coord(self._x + other._x, self._y + other._y)

    def sub(self, other):
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

    def print(self):
        print(f"{(self._x, self._y)}, c={self._c}<{Pixel._name[self._c]}>")

    def complement(self):
        return Pixel(self._x, self._y, 7 - self._c)

    def add(self, other):
        r = super().add(other)
        return Pixel(r._x, r._y, self._c | other._c)

    def sub(self, other):
        r = super().sub(other)
        return Pixel(r._x, r._y, self._c & other._c)


class PixelPair:
    def __init__(self, a, b):
        if not isinstance(a, Pixel) or not isinstance(b, Pixel):
            raise TypeError
        self.a = a
        self.b = b

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def print(self):
        print("a: ", end="")
        self.a.print()
        print("b: ", end="")
        self.b.print()


a = Pixel(0, 1, 1)
b = Pixel(4, 8, 2)
p = PixelPair(a, b)
p.print()

# Reference assignement
print("\nTest: cp = p")
cp = p
print(f"{cp is p = }")
print(f"{cp.get_a() is p.get_a() = }")
print(f"{cp.get_b() is p.get_b() = }")
cp.print()
print("Set a color to 4")
a.set_color(4)
cp.print()

# shallow copy
print("\nTest: cp = copy.copy(p)")
import copy

cp = copy.copy(p)
print(f"{cp is p = }")
print(f"{cp.get_a() is p.get_a() = }")
print(f"{cp.get_b() is p.get_b() = }")
cp.print()
print("Set a color to 5")
a.set_color(5)
cp.print()

# deep copy
print("\nTest: cp = copy.deepcopy(p)")
cp = copy.deepcopy(p)
print(f"{cp is p = }")
print(f"{cp.get_a() is p.get_a() = }")
print(f"{cp.get_b() is p.get_b() = }")
cp.print()
print("Set a color to 6")
a.set_color(6)
cp.print()
