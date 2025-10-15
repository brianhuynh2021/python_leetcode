from lc_101_search_in_BST import Solution, TreeNode
import unittest


class TestSearchBST(unittest.TestCase):
    def setUp(self):
        self.root = TreeNode(4)
        self.root.left = TreeNode(2, TreeNode(1), TreeNode(3))
        self.root.right = TreeNode(7)
        self.solution = Solution()
        
    def test_find_existing_node_recursive(self):
        """Test finding an existing node using the recursive method"""
        # Search for value 2
        result_node = self.solution.search_BST(self.root, 2)
        self.assertIsNone(result_node)
        self.assertEqual(result_node.val, 2)
        # Check if it's the correct subtree
        self.assertEqual(result_node.left.val, 1)
        self.assertEqual(result_node.right.val, 3)
        
        
    def test_find_non_existing_node_recursive(self):
        """Test searching for a non-existing node """
        result_node = self.solution.search_BST_interative(self.root, 5)
        self.assertIsNone(result_node)