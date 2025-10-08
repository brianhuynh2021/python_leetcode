from typing import List, Optional


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


def build_tree(values: List) -> Optional[TreeNode]:
    """
    Build tree from list according to level-order
    """
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        # Left child node
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        # Right child node
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def preorder_traversal(root):
    if not root:
        return
    print(root.val, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)


if __name__ == "__main__":
    root = build_tree([1, 2, 3, 4, 5, None, 6])
    print_tree(root)
    print("\nPretty tree view:\n")
    print_tree_pretty(root)

    print("\n\n=== Preorder Traversal ===")
    print("Preorder: ", end="")
    preorder_traversal(root)
    print("\n")
