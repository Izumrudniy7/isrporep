import unittest
from circle import area, perimeter
import math

class CircleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(3)
        expected = math.pi * 9
        self.assertAlmostEqual(res, expected)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        res = area(2.5)
        expected = math.pi * 6.25
        self.assertAlmostEqual(res, expected)

    def test_perimeter_positive(self):
        res = perimeter(3)
        expected = 2 * math.pi * 3
        self.assertAlmostEqual(res, expected)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_float(self):
        res = perimeter(2.5)
        expected = 2 * math.pi * 2.5
        self.assertAlmostEqual(res, expected)