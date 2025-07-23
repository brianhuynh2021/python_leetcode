import unittest
from lc_86_valid_parentheses_1st import valid_parentheses


class TestValidParentheses(unittest.TestCase):
    def test_valid_parentheses(self):
        self.assertEqual(valid_parentheses(""), True)
        self.assertEqual(valid_parentheses("()"), True)
        self.assertEqual(valid_parentheses("(([]))"), True)
        
    def test_invalid_parentheses(self):
        self.assertEqual(valid_parentheses("]"), False)
        self.assertEqual(valid_parentheses("({}"), False)
        self.assertEqual(valid_parentheses("(([))"), False)
        
if __name__=='__main__':
    unittest.main()