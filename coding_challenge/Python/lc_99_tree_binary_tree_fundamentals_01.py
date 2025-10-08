from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


def print_tree(root):
    if not root:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)


def print_tree_pretty(node, level=0):
    if node is not None:
        print_tree_pretty(node.right, level + 1)
        print("    " * level + f"-> {node.val}")
        print_tree_pretty(node.left, level + 1)


root = TreeNode("A")
root.left = TreeNode("B")
root.right = TreeNode("C")
root.left.left = TreeNode("D")
root.left.right = TreeNode("E")
root.right.right = TreeNode("F")

if __name__ == "__main__":
    print_tree(root)
    print("\nPretty tree view:\n")
    print_tree_pretty(root)
