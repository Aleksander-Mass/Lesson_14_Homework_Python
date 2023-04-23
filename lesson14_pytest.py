import pytest
from lesson14 import Rectangle


def test_area():
    r = Rectangle(5, 6)
    assert r.get_area() == 5 * 6


def test_perimeter():
    r = Rectangle(5, 6)
    assert r.get_long() == 2 * (5 + 6)


if __name__ == '__main__':
    pytest.main(['-v'])