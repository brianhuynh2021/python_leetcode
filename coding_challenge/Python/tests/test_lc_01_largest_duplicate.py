import unittest
from unittest.mock import Mock, patch
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from lc_01_largest_duplicate_finder_02 import find_largest_duplicate_optimized

class TestLargestNumber(unittest.TestCase):
    
    def test_with_duplicate(self):
        test_cases = [
            # [input, expected_output]
            [[1, 3, 5, 7, 7, 9, 6, 8, 8, 8, 7], 8],  # Example case
            [[5, 5, 3, 1], 5],  # Duplicate at beginning
            [[1, 2, 3, 4, 5, 5], 5],  # Duplicate at end
            [[10, 1, 10, 2], 10],  # Largest number is duplicate
            [[5, 1, 3, 5, 7, 9], 5],  # Only one duplicate
            [[5, 5, 5, 5], 5],  # All elements are the same
            [[10, 5, 9, 10, 12], 10],  # Largest duplicate is not the largest number
            [[-1, -1, -2, -3], -1],  # Negative numbers
            [[0, 0, 1], 0],  # Zero as duplicate
        ]
        
        for nums, expected in test_cases:
            with self.subTest(nums=nums, expected=expected):
                result = find_largest_duplicate_optimized(nums)
                self.assertEqual(result, expected)
                
    @patch('lc_01_largest_duplicate_finder_02.find_largest_duplicate_optimized')
    def test_mock_data(self, mock_function):
        mock_function.return_value = 8
        
        # Test
        from lc_01_largest_duplicate_finder_02 import process_data_with_message
        result = process_data_with_message([1, 5, 5, 3])
        # Verify
        self.assertEqual(result, "Largest duplicate is 8")
        mock_function.assert_called_once_with([1, 5, 5, 3])
        
if __name__=='__main__':
    unittest.main(verbosity=2)
