import unittest
from lc_102_insert_into_a_BST import Solution, TreeNode, inorder_traversal


class TestInsertIntoBST(unittest.TestCase):

    def setUp(self):
        """Build a test tree before each test."""
        self.solution = Solution()
        self.root = TreeNode(4)
        self.root.left = TreeNode(2, TreeNode(1), TreeNode(3))
        self.root.right = TreeNode(7)

    def test_insert_value_right(self):
        """Insert a value into the right subtree."""
        result = self.solution.insert_into_BST(self.root, 5)
        self.assertEqual(inorder_traversal(result), [1, 2, 3, 4, 5, 7])

    def test_insert_value_left(self):
        """Insert a value into the left subtree."""
        result = self.solution.insert_into_BST(self.root, 0)
        self.assertEqual(inorder_traversal(result), [0, 1, 2, 3, 4, 7])

    def test_insert_empty_tree(self):
        """Insert into an empty tree."""
        result = self.solution.insert_into_BST(None, 10)
        self.assertEqual(result.val, 10)

    def test_insert_iterative(self):
        """Test iterative insert method."""
        result = self.solution.insert_into_BST_iterative(self.root, 6)
        self.assertEqual(inorder_traversal(result), [1, 2, 3, 4, 6, 7])


if __name__ == '__main__':
    unittest.main(verbosity=2)