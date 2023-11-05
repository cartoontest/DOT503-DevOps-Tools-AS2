import unittest
from application import calculate_rectangle_area

class TestRectangleArea(unittest.TestCase):
    def test_area_positive_values(self):
        self.assertEqual(calculate_rectangle_area(4, 5), 20)

    def test_area_zero_values(self):
        self.assertEqual(calculate_rectangle_area(0, 0), 0)

    def test_area_negative_values(self):
        self.assertEqual(calculate_rectangle_area(-2, -3), 6)

    def test_area_mixed_values(self):
        self.assertEqual(calculate_rectangle_area(3, -4), 12)

    def test_area_float_values(self):
        self.assertEqual(calculate_rectangle_area(3.5, 5.5), 15.75)

if __name__ == "__main__":
    unittest.main()
