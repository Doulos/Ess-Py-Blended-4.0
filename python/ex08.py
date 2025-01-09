class Coord:
    """Implement a coord object (x,y)

    Note that we use the convention _x,_y for the x,y instance variable
    to convey that these attributes are like "protected attribute":
    - OK to use directly within own/derived class
    - use the get/set interfaces elsewhere

    The Pixel class will directly access the self._x, self._y. This
    will simplify the writing of the class, but we must ensure to not
    break thing inherited from Coord.
    """

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


p = Pixel(1, 2, 3)
p.print()  # should see: (1, 2), c=3<blue>
assert p.get_color() == 3
p.set_color(2)
assert p.get_color() == 2
assert p.complement().get_color() == 5
p.setxy(3, 4)
p.complement().print()  # Should see: (3,4), c=5<purple>
