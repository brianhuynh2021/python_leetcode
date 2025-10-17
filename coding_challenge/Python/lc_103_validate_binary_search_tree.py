"""
LeetCode 98: Validate Binary Search Tree
Difficulty: Medium
Companies: Amazon, Google, Facebook, Microsoft (VERY COMMON!)

Problem:
--------
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as:
- The left subtree of a node contains only nodes with values LESS THAN the node's value.
- The right subtree of a node contains only nodes with values GREATER THAN the node's value.
- Both left and right subtrees must also be valid BSTs.

Example 1:
    Input: root = [2,1,3]
    Output: true
    
    Tree:
        2
       / \
      1   3

Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.
    
    Tree:
          5
         / \
        1   4
           / \
          3   6

Pattern: BST Validation using min/max bounds
Key Insight: Each node must be within a valid range. For left children, update max bound. For right children, update min bound.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST_recursive(self, root: TreeNode) -> bool:
        """
        Approach 1: Recursive with Min/Max Bounds
        
        Logic:
        - Each node must have a value within a valid range [min_val, max_val]
        - When going to the left child, the max bound becomes current node's value
        - When going to the right child, the min bound becomes current node's value
        - Recursively validate all nodes
        
        Time: O(n) - Visit each node once
        Space: O(h) - Recursion stack height
        """
        def validate(node, min_val, max_val):
            # Base case: empty node is valid
            if not node:
                return True
            
            # Check if current node is within bounds
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Recursively validate left and right subtrees
            # Left child must be < node.val, so update max_val
            # Right child must be > node.val, so update min_val
            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))

    def isValidBST_inorder(self, root: TreeNode) -> bool:
        """
        Approach 2: Inorder Traversal
        
        Logic:
        - Inorder traversal of a valid BST produces a sorted array
        - Keep track of previous node value during inorder traversal
        - If current value <= previous value, it's not a valid BST
        
        Time: O(n)
        Space: O(h) for recursion stack
        """
        self.prev_val = float('-inf')
        
        def inorder(node):
            if not node:
                return True
            
            # Traverse left subtree
            if not inorder(node.left):
                return False
            
            # Check current node
            if node.val <= self.prev_val:
                return False
            self.prev_val = node.val
            
            # Traverse right subtree
            return inorder(node.right)
        
        return inorder(root)

    def isValidBST_iterative(self, root: TreeNode) -> bool:
        """
        Approach 3: Iterative with Stack (using min/max bounds)
        
        Logic:
        - Use a stack to store tuples of (node, min_val, max_val)
        - Pop from stack and validate bounds
        - Push left and right children with updated bounds
        
        Time: O(n)
        Space: O(h)
        """
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            node, min_val, max_val = stack.pop()
            
            # Check if current node is within bounds
            if node.val <= min_val or node.val >= max_val:
                return False
            
            # Add left child with updated max bound
            if node.left:
                stack.append((node.left, min_val, node.val))
            
            # Add right child with updated min bound
            if node.right:
                stack.append((node.right, node.val, max_val))
        
        return True