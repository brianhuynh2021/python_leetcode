import unittest
from lc_87_min_stack_1st import MinStack

class TestMinStack(unittest.TestCase):
    def test_sequence(self):
        s = MinStack()
        s.push(5)
        s.push(2)
        s.push(4)
        s.push(1)
        self.assertEqual(s.getMin(), 1)
        s.pop()
        self.assertEqual(s.getMin(), 2)
        self.assertEqual(s.top(), 4)

if __name__ == "__main__":
    unittest.main()