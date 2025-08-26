import unittest
from lc_48_group_anagrams_2nd import group_anagrams_brute


class TestGroupAnagrams(unittest.TestCase):
    def test_basic_case(self):
        data = ["eat", "tea", "tan", "ate", "nat", "bat"]
        output = group_anagrams_brute(data)
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertEqual(
            set(frozenset(g) for g in output),
            set(frozenset(g) for g in expected)
        )

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            group_anagrams_brute([])

    def test_one_word(self):
        self.assertEqual(group_anagrams_brute(["abc"]), [["abc"]])

    def test_duplicates(self):
        data = ["abc", "bca", "abc"]
        output = group_anagrams_brute(data)
        expected = [["abc", "bca", "abc"]]
        self.assertEqual(
            set(frozenset(g) for g in output),
            set(frozenset(g) for g in expected)
        )