from lc_95_connect_ropes_to_minize_cost_2nd import min_cost_bruteforce_loops_trace
import unittest


class TestConnectRopes(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(min_cost_bruteforce_loops_trace([]), 0)
        
    def test_single(self):
        self.assertEqual(min_cost_bruteforce_loops_trace([1]), 0)
        
    def test_two(self):
        self.assertEqual(min_cost_bruteforce_loops_trace([1, 2]), 3)