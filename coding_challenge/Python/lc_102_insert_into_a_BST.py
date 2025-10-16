"""
LeetCode 701: Insert into a Binary Search Tree
Difficulty: Medium
Companies: Amazon, Apple, Microsoft

Problem:
--------
You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Example 1:
    Input: root = [4,2,7,1,3], val = 5
    Output: [4,2,7,1,3,5]
    
    Tree before:            Tree after:
          4                       4
         / \                     / \
        2   7                   2   7
       / \                     / \ /
      1   3                   1  3 5

Pattern: BST Traversal
Key Insight: Traverse the tree as if you are searching for the value. When you hit a null pointer (None), that's where the new node should be inserted.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def insert_into_BST(self, root: TreeNode, val: int) -> TreeNode:
        """
        Approach 1: Recursive Solution
        
        Logic:
        - If the current node is None, we've found the insertion point. Return a new TreeNode.
        - If val < node.val, the new node belongs in the left subtree. Recurse left.
        - If val > node.val, the new node belongs in the right subtree. Recurse right.
        - The recursive calls will eventually return the newly created node, which gets linked up to its parent.
        
        Time: O(h) where h is the height (O(log n) for balanced, O(n) for skewed)
        Space: O(h) for the recursion stack
        """
        # Base case: Found the empty spot to insert the new node
        if not root:
            return TreeNode(val)
        
        # If the tree is just a single node and we haven't inserted, handle it
        if val < root.val:
            root.left = self.insert_into_BST(root.left, val)
        else: # val > root.val
            root.right = self.insert_into_BST(root.right, val)
            
        return root


    def insert_into_BST_iterative(self, root: TreeNode, val: int) -> TreeNode:
        """
        Approach 2: Iterative Solution
        
        Logic:
        - Handle the edge case of an empty initial tree.
        - Traverse down the tree using a 'current' pointer, following BST rules.
        - Stop when the next step would be None.
        - Insert the new node as the left or right child of the node where the loop terminated.
        
        Time: O(h)
        Space: O(1)
        """
        new_node = TreeNode(val)
        
        # Edge case: if the tree is empty, the new node is the root
        if not root:
            return new_node
        
        current = root
        while True:
            if val < current.val:
                # If left child is empty, insert here
                if not current.left:
                    current.left = new_node
                    return root
                # Otherwise, move to the left child
                current = current.left
                
            else: # val > current.val
                # If right child is empty, insert here
                if not current.right:
                    current.right = new_node
                    return root
                # Otherwise, move to the right child
                current = current.right
                
def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []


                