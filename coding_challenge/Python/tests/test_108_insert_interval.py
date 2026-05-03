import unittest

from coding_challenge.Python.lc_108_insert_interval import insert_interval


class TestInsertInterval(unittest.TestCase):
    def test_insert_an_interval(self):
        intervals = [[1, 3], [6, 9]]
        new_interval = [2, 5]
        result = insert_interval(intervals, new_interval)
        self.assertEqual(result, [[1, 5], [6, 9]])