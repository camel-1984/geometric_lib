import unittest
import math
from circle import area, perimeter


class TestCircle(unittest.TestCase):

    def test_area_positive_radius(self):
        radius = 5
        expected_area = math.pi * radius * radius
        result = area(radius)
        self.assertAlmostEqual(result, expected_area)

    def test_perimeter_positive_radius(self):
        radius = 5
        expected_perimeter = 2 * math.pi * radius
        result = perimeter(radius)
        self.assertAlmostEqual(result, expected_perimeter)

    def test_area_negative_radius(self):
        radius = -5
        with self.assertRaises(ValueError):
            area(radius)

    def test_perimeter_negative_radius(self):
        radius = -5
        with self.assertRaises(ValueError):
            perimeter(radius)
