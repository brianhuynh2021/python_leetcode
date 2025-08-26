import unittest
from lc_68_fruits_into_basket_2nd import fruit_into_baskets_brute, fruit_into_baskets_optimize


class TestFruitIntoBasket(unittest.TestCase):
    def test_all_same_fruit(self):
        self.assertEqual(fruit_into_baskets_brute([1, 1, 1, 1]), 4)

    def test_exactly_two_types(self):
        self.assertEqual(fruit_into_baskets_brute([1, 2, 1, 2, 1]), 5)

    def test_more_than_two_types(self):
        self.assertEqual(fruit_into_baskets_brute([1, 2, 3, 2, 2]), 4)

    def test_single_element(self):
        self.assertEqual(fruit_into_baskets_brute([1]), 1)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            fruit_into_baskets_brute([])

    def test_switching_fruits(self):
        self.assertEqual(fruit_into_baskets_brute([1, 2, 3, 1, 2, 3, 1]), 2)