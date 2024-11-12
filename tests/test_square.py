import unittest
from square import area, perimeter


class TestSquare(unittest.TestCase):

    def test_area_positive_side(self):
        side = 5
        expected_area = side * side
        result = area(side)
        self.assertAlmostEqual(result, expected_area)

    def test_perimeter_positive_side(self):
        side = 5
        expected_perimeter = 4 * side
        result = perimeter(side)
        self.assertAlmostEqual(result, expected_perimeter)

    def test_area_negative_side(self):
        side = -5
        with self.assertRaises(ValueError):
            area(side)

    def test_perimeter_negative_side(self):
        side = -5
        with self.assertRaises(ValueError):
            perimeter(side)
