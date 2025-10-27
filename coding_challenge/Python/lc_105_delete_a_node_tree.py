class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
        
    
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """Delete a node in BST with given key and return new root"""
        if not root:
            return None
        
        # Step 1: Search for node
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Found the node to delete
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Node with two children:
            # find inorder successor (min node in right subtree)
            successor = self._minValueNode(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)

        return root

    def _minValueNode(self, node: TreeNode) -> TreeNode:
        """Find the node with the smallest value in a BST subtree."""
        current = node
        while current.left:
            current = current.left
        return current