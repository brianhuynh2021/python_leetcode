import unittest

from lc_98_merge_k_sorted_list import (
    linked_to_list,
    list_to_linked,
    merge_k_lists_bruteforce,
)


class TesMergeSortedLists(unittest.TestCase):
    def test_empty_input(self):
        self.assertIsNone(merge_k_lists_bruteforce([]))

    def test_example_case(self):
        lists = [
            list_to_linked([1, 4, 5]),
            list_to_linked([1, 3, 4]),
            list_to_linked([2, 6]),
        ]
        result = merge_k_lists_bruteforce(lists)
        self.assertEqual(linked_to_list(result), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_single_list(self):
        lists = [list_to_linked([1, 2, 3])]
        result = merge_k_lists_bruteforce(lists)
        self.assertEqual(linked_to_list(result), [1, 2, 3])
