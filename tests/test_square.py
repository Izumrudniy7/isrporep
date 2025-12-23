import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(4)
        self.assertEqual(res, 16)

    def test_area_positive2(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_float(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)

    # Тесты для функции perimeter
    def test_perimeter_positive(self):
        res = perimeter(4)
        self.assertEqual(res, 16)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_float(self):
        res = perimeter(2.5)
        self.assertEqual(res, 10.0)