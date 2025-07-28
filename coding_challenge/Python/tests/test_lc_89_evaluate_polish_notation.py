import unittest
from lc_89_evalue_reverse_polish_notation_1st import evaluate_reverse_polish_notation

class TestReversePolisNotation(unittest.TestCase):
    def test_single_operand(self):
        self.assertEqual(evaluate_reverse_polish_notation(["42"]), 42)
        self.assertEqual(evaluate_reverse_polish_notation(["-7"]), -7)
    
    def test_simple_operations(self):
        self.assertEqual(evaluate_reverse_polish_notation(["2", "3", "+"]), 5)
        self.assertEqual(evaluate_reverse_polish_notation(["5", "3", "-"]), 2)
        self.assertEqual(evaluate_reverse_polish_notation(["4", "2", "*"]), 8)
        self.assertEqual(evaluate_reverse_polish_notation(["8", "2", "/"]), 4)
        
    def test_complex_expression(self):
        tokens = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
        self.assertEqual(evaluate_reverse_polish_notation(tokens), 14)
        
    def test_division_truncate_toward_zero(self):
        self.assertEqual(evaluate_reverse_polish_notation(["13", "5", "/"]), 2)
        self.assertEqual(evaluate_reverse_polish_notation(["-13", "5", "/"]), -2)
        
    def test_invalid_empty_token(self):
        with self.assertRaises(ValueError):
            evaluate_reverse_polish_notation([])