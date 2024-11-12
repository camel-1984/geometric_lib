import unittest
import math
from calculate import calc


class TestCalculate(unittest.TestCase):

    def test_calc_correct_arguments(self):
        self.assertAlmostEqual(calc("circle", "area", [5]), math.pi * 5 * 5)
        self.assertAlmostEqual(calc("square", "area", [4]), 4 * 4)
        self.assertAlmostEqual(
            calc("triangle", "area", [3, 4, 5]), 6.0
        )

        self.assertAlmostEqual(
            calc("circle", "perimeter", [5]), 2 * math.pi * 5
        )
        self.assertAlmostEqual(calc("square", "perimeter", [4]), 4 * 4)
        self.assertAlmostEqual(calc("triangle", "perimeter", [3, 4, 5]), 3 + 4 + 5)

    def test_calc_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calc("line", "area", [5])

    def test_calc_invalid_function(self):
        with self.assertRaises(AssertionError):
            calc("circle", "speed", [5])

    def test_calc_incorrect_number_of_arguments(self):
        with self.assertRaises(TypeError):
            calc("circle", "area", [5, 52])

        with self.assertRaises(TypeError):
            calc("square", "perimeter", [])

        with self.assertRaises(TypeError):
            calc("triangle", "area", [5, 52])

    def test_calc_invalid_argument_types(self):
        with self.assertRaises(TypeError):
            calc("circle", "area", ["one"])

        with self.assertRaises(TypeError):
            calc("square", "area", ["4"])

        with self.assertRaises(TypeError):
            calc("triangle", "perimeter", [3, "four", 5])
