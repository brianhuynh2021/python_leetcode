from lc_02_target_sum import check_target_sum_optimized, check_target_sum_brute_force
import unittest
from typing import Optional, List

class TestCheckTargetSum(unittest.TestCase):
    def test_exist_check_sum(self):
        a = [1, 3, 5, 7, 14]
        k = 8
        result = check_target_sum_brute_force(a, k)
        self.assertEqual(result, True, 'Happy case')
        
    def test_not_exist_check_sum(self):
        a = [1, 3, 5, 7, 14, 25]
        k = 13
        result = check_target_sum_optimized(a, k)
        self.assertEqual(result, False, 'Not exist check sum')
        
        
if __name__=='__main__':
    unittest.main(verbosity=2)