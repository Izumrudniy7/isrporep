import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_positive(self):
        res = area(5, 3)
        self.assertEqual(res, 15)

    def test_area_float(self):
        res = area(5.5, 2.0)
        self.assertEqual(res, 11.0)

    def test_perimeter_positive(self):
        res = perimeter(5, 3)
        self.assertEqual(res, 16)

    def test_perimeter_square(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_perimeter_float(self):
        res = perimeter(5.5, 2.5)
        self.assertEqual(res, 16.0)

    def test_perimeter_zero(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)