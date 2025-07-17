import unittest
from Python.lc_67_longest_substring_with_k_distince_characters_2nd import brute_force_longest_substr_with_k


class TestLongSubString(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(brute_force_longest_substr_with_k("eceba", 2), "ece")
        
    def test_repeated_case(self):
        self.assertEqual(brute_force_longest_substr_with_k("aa", 1), "aa")
        
    def test_zero_k(self):
        self.assertEqual(brute_force_longest_substr_with_k("abc", 0), "")
        

if __name__=="__main__":
    unittest.main()