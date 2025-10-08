import unittest

from lc_91_next_greater_element_1st import next_greater_element_brute


class TestGreaterElement(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(next_greater_element_brute([2, 1, 2, 4, 3]), [4, 2, 4, -1, -1])

    def test_strictly_decreasing(self):
        self.assertEqual(
            next_greater_element_brute([5, 4, 3, 2, 1]), [-1, -1, -1, -1, -1]
        )

    def test_strictly_increasing(self):
        self.assertEqual(next_greater_element_brute([1, 2, 3, 4]), [2, 3, 4, -1])

    def test_single_element(self):
        self.assertEqual(next_greater_element_brute([42]), [-1])

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            next_greater_element_brute([])


def test_strictly_increasing():
    assert next_greater_element_brute([1, 2, 3, 4]) == [2, 3, 4, -1]


def test_strictly_decreasing():
    assert next_greater_element_brute([5, 4, 3, 2, 1]) == [-1, -1, -1, -1, -1]


def test_single_element():
    assert next_greater_element_brute([99]) == [-1]
