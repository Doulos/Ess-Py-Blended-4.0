class Coord:
    def __init__(self, x, y):
        self.setxy(x, y)

    def setxy(self, x, y):
        self.setx(x)
        self.sety(y)

    def getxy(self):
        return (self.getx(), self.gety())

    def setx(self, x):
        self.x = x

    def sety(self, y):
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def add(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def sub(self, other):
        return Coord(self.x - other.x, self.y - other.y)


c1 = Coord(1, 1)
c2 = Coord(4, 8)
c1.setxy(2, 2)
print("c1.getxy() =", c1.getxy())
c1.setx(4)
c1.sety(5)
print("c1.getxy() =", c1.getxy())
print("c2.getxy() =", c2.getxy())
print("c1.getx() =", c1.getx())
print("c1.gety() =", c1.gety())
print("c1.add(c2) =", c1.add(c2).getxy())
print("c1.sub(c2) =", c1.sub(c2).getxy())
