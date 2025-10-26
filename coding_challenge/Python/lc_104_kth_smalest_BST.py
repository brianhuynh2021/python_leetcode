class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        """
        Interative inorder traversal. The kth visited node (inorder) is the answer.
        Time: O(h + k), Space: O(h)
        """
        stack, cur = [], root
        while True:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
            
        def k_smallest_recursive(self, root: TreeNode, k: int) -> int:
            self.count = 0
            self.ans = None
            def inorder(node):
                if not node or self.ans is not None:
                    return
                inorder(node.left)
                self.count += 1
                if self.count == k:
                    self.ans = node.val
                    return
                inorder(node.right)
            inorder(root)
            return self.ans
        