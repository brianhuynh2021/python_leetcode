"""
LeetCode 700: Search in a Binary Search Tree
Difficulty: Easy
Companies: Amazon, Microsoft, Bloomberg

Problem:
--------
Given root of BST and integer val, find node where node.val == val.
Return the subtree rooted at that node. If not found, return None.

Example 1:
    Input: root = [4,2,7,1,3], val = 2
    Output: [2,1,3]
    
Example 2:
    Input: root = [4,2,7,1,3], val = 5
    Output: None

Pattern: BST Search
Key Insight: Navigate left if val < node.val, right if val > node.val
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def search_BST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Approach 1: Recursive Solution
        
        Logic:
        - Base case: if node is None or node.val == val, return node
        - If val < node.val, search in left subtree
        - If val > node.val, search in right subtree
        
        Time: O(h) where h = height (O(log n) balanced, O(n) worst)
        Space: O(h) for recursion stack
        """
        # Base case: emptry tree or found target
        if not root or root.val == val:
            return root
        
        # BST property: go left if val is smaller
        if val < root.val:
            return self.search_BST(root.left, val)
        else:
            return self.search_BST(root.right, val)
        
    def search_BST_interative(self, root: TreeNode, val: int) -> TreeNode:
        """
        Approach 2: Interative Solution (More efficient)
        Logic:
        - Use while loop to traverse tree
        - Navigate based on BST property
        
        Time: O(h)
        Space: O(1) - no recursion stack!
        """
        current = root
        
        while current:
            if current.val == val:
                return current
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return None
    
