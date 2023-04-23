import unittest
from lesson14 import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.r = Rectangle(5, 6)

    def test_area(self):
        self.assertEqual(self.r.get_area(), 5 * 6)

    def test_long(self):
        self.assertEqual(self.r.get_long(), 2 * (5 + 6))


if __name__ == '__main__':
    unittest.main()