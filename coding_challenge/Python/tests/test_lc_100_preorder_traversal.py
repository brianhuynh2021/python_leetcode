import sys
from io import StringIO
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
from lc_100_tree_binary_tree_fundamentals_02 import (
    preorder_traversal,
    TreeNode,
    build_tree
)
import unittest

class TestPreorderTraversal(unittest.TestCase):
    """Test cases for preorder traversal"""
    
    def test_preorder_simple_tree(self):
        """Test preorder with simple tree: 1-2-3"""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        root = build_tree([1, 2, 3])
        preorder_traversal(root)
        
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue().strip(), "1 2 3")
    
    
    def test_preorder_with_children(self):
        """Test preorder with tree: 1,2,3,4,5,None,6"""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        root = build_tree([1, 2, 3, 4, 5, None, 6])
        preorder_traversal(root)
        
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue().strip(), "1 2 4 5 3 6")
    
    
    def test_preorder_single_node(self):
        """Test preorder with single node"""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        root = TreeNode(1)
        preorder_traversal(root)
        
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue().strip(), "1")
    
    
    def test_preorder_empty_tree(self):
        """Test preorder with None"""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        root = None
        preorder_traversal(root)
        
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue().strip(), "")

        
if __name__=='__main__':
    unittest.main(verbosity=2)