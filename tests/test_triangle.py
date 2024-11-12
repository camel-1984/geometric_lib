import unittest
import math
from triangle import area, perimeter

class TestTriangle(unittest.TestCase):

    def test_area_valid_triangle(self):
        a, b, c = 3, 4, 5
        p = (a + b + c) / 2
        expected_area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        result = area(a, b, c)
        self.assertAlmostEqual(result, expected_area)

    def test_perimeter_valid_triangle(self):
        a, b, c = 3, 4, 5
        expected_perimeter = a + b + c
        result = perimeter(a, b, c)
        self.assertAlmostEqual(result, expected_perimeter)

    def test_area_invalid_triangle(self):
        a, b, c = 1, 2, 10  
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_perimeter_invalid_triangle(self):
        a, b, c = 1, 2, 10  
        with self.assertRaises(ValueError):
            perimeter(a, b, c)

    def test_area_negative_side(self):
        a, b, c = -3, 4, 5
        with self.assertRaises(ValueError):
            area(a, b, c)

    def test_perimeter_negative_side(self):
        a, b, c = -3, 4, 5
        with self.assertRaises(ValueError):
            perimeter(a, b, c)
