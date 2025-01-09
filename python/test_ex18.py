from ex10 import Coord, Pixel
import pytest


def test_coord_init():
    c1 = Coord(1, 2)
    assert c1.getxy() == (1, 2)


def test_coord_setxy():
    c1 = Coord(0, 0)
    c1.setxy(-1, -2)
    assert c1.getxy() == (-1, -2)


def test_coord_getset():
    c1 = Coord(4, 7)
    c1.setx(7)
    assert c1.getx() == 7
    c1.sety(4)
    assert c1.gety() == 4


def test_coord_add():
    c1 = Coord(1, 2)
    c2 = Coord(-2, 1)
    assert (c1 + c2).getxy() == (-1, 3)


def test_coord_sub():
    c1 = Coord(5, -2)
    c2 = Coord(1, -1)
    assert (c1 - c2).getxy() == (4, -1)


def test_pixel_init():
    p1 = Pixel(1, 2, 2)
    assert p1.getxy() == (1, 2)
    assert p1.get_color() == 2


def test_pixel_setcolor():
    p1 = Pixel(1, 2, 3)
    p1.set_color(5)
    assert p1.get_color() == 5


def test_pixel_invalidcolor():
    with pytest.raises(ValueError):
        p1 = Pixel(1, 2, 123)


def test_pixel_str():
    p1 = Pixel(1, 2, 3)
    assert str(p1) == "(1, 2), c=3<blue>"


def test_pixel_neg():
    p1 = Pixel(1, 2, 3)
    assert (-p1).get_color() == 4


@pytest.mark.skip("counter test")
def test_should_fail():
    p1 = Pixel(1, 2, 0)
    assert p1.get_color() == 1


@pytest.mark.xfail
def test_hack(monkeypatch):
    def bad_str(self):
        return "ahahah, I broke it!"

    monkeypatch.setattr(Pixel, "__str__", bad_str)
    p1 = Pixel(1, 2, 3)
    assert str(p1) == "(1, 2), c=3<blue>"
