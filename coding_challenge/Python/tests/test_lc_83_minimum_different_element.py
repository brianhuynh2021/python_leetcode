import unittest

from lc_83_minimum_difference_element_2nd import optimized_find_min_diff_element


class TestMinDiffElement(unittest.TestCase):
    def test_exactly_match(self):
        self.assertEqual(optimized_find_min_diff_element([1, 2, 3], 2), 2)

    def test_closest_right(self):
        self.assertEqual(optimized_find_min_diff_element([1, 3, 8, 10], 9), 8)

    def test_closest_left(self):
        self.assertEqual(optimized_find_min_diff_element([5, 10, 15], 12), 10)


if __name__ == "__main__":
    unittest.main()
