import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(6, 4)
        self.assertEqual(res, 12.0)

    def test_area_positive2(self):
        res = area(6, 3)
        self.assertEqual(res, 18.0)
        
    def test_area_zero_height(self):
        res = area(6, 0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        res = area(5.5, 3.0)
        self.assertEqual(res, 8.25)

    def test_perimeter_positive(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_zero_side(self):
        res = perimeter(3, 0, 5)
        self.assertEqual(res, 8)

    def test_perimeter_float(self):
        res = perimeter(2.5, 3.5, 4.5)
        self.assertEqual(res, 10.5)