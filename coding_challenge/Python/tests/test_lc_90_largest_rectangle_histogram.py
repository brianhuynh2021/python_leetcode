import unittest
from lc_90_largest_rectangle_in_histogram import Solution


class TestLargestRectangleBruteForce(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        self.assertEqual(self.sol.largest_rectangle_area([2,1,5,6,2,3]), 10)

    def test_case2(self):
        self.assertEqual(self.sol.largest_rectangle_area([2,4]), 4)

    def test_case3(self):
        self.assertEqual(self.sol.largest_rectangle_area([1,1,1,1]), 4)

    def test_single_bar(self):
        self.assertEqual(self.sol.largest_rectangle_area([4]), 4)

    def test_decreasing(self):
        self.assertEqual(self.sol.largest_rectangle_area([5,4,3,2,1]), 9)

if __name__ == '__main__':
    unittest.main()