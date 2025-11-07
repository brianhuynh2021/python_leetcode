from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List, Dict


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


# ===============================================================
# LC 235: Lowest Common Ancestor of BST
# ===============================================================

def _path_to(root: Optional[TreeNode], target: TreeNode) -> List[TreeNode]:
    if root is None:
        return []
    if root is target:
        return [root]
    left = _path_to(root.left, target)
    if left:
        return [root] + left
    right = _path_to(root.right, target)
    if right:
        return [root] + right
    return []


def lowest_common_ancestor_bt_style(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    """Brute force ignoring BST property: build two paths and compare."""
    p1, p2 = _path_to(root, p), _path_to(root, q)
    lca = None
    for a, b in zip(p1, p2):
        if a is b:
            lca = a
        else:
            break
    return lca


def lowest_common_ancestor_bst(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    """Optimal for BST: O(h) time, O(1) space."""
    if root is None:
        return None
    pv, qv = p.val, q.val
    node = root
    while node:
        if pv < node.val and qv < node.val:
            node = node.left
        elif pv > node.val and qv > node.val:
            node = node.right
        else:
            return node
    return None


# ===============================================================
# LC 108: Convert Sorted Array to BST
# ===============================================================

def sorted_array_to_bst_brutish(nums: List[int]) -> Optional[TreeNode]:
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sorted_array_to_bst_brutish(nums[:mid])
    root.right = sorted_array_to_bst_brutish(nums[mid + 1 :])
    return root


def sorted_array_to_bst(nums: List[int]) -> Optional[TreeNode]:
    def build(lo: int, hi: int) -> Optional[TreeNode]:
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        node = TreeNode(nums[mid])
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    return build(0, len(nums) - 1)


# ===============================================================
# LC 501: Find Mode in BST
# ===============================================================

def find_mode_hash(root: Optional[TreeNode]) -> List[int]:
    if root is None:
        return []
    freq: Dict[int, int] = {}

    def dfs(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        dfs(node.left)
        freq[node.val] = freq.get(node.val, 0) + 1
        dfs(node.right)

    dfs(root)
    if not freq:
        return []
    maxf = max(freq.values())
    return [v for v, c in freq.items() if c == maxf]


def find_mode_inorder(root: Optional[TreeNode]) -> List[int]:
    modes: List[int] = []
    best = 0
    curr = 0
    prev: Optional[int] = None

    def visit(value: int) -> None:
        nonlocal prev, curr, best, modes
        if prev is None or value != prev:
            curr = 1
            prev = value
        else:
            curr += 1
        if curr > best:
            best = curr
            modes = [value]
        elif curr == best:
            modes.append(value)

    def inorder(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        inorder(node.left)
        visit(node.val)
        inorder(node.right)

    inorder(root)
    return modes


# ===============================================================
# LC 99: Recover Binary Search Tree
# ===============================================================

def recover_tree_brutish(root: Optional[TreeNode]) -> None:
    nodes: List[TreeNode] = []
    vals: List[int] = []

    def inorder(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        inorder(node.left)
        nodes.append(node)
        vals.append(node.val)
        inorder(node.right)

    inorder(root)
    vals.sort()
    for node, v in zip(nodes, vals):
        node.val = v


def recover_tree_inorder(root: Optional[TreeNode]) -> None:
    first: Optional[TreeNode] = None
    second: Optional[TreeNode] = None
    prev: Optional[TreeNode] = None

    def inorder(node: Optional[TreeNode]) -> None:
        nonlocal first, second, prev
        if node is None:
            return
        inorder(node.left)
        if prev is not None and prev.val > node.val:
            if first is None:
                first = prev
            second = node
        prev = node
        inorder(node.right)

    inorder(root)
    if first is not None and second is not None:
        first.val, second.val = second.val, first.val


def recover_tree_morris(root: Optional[TreeNode]) -> None:
    first: Optional[TreeNode] = None
    second: Optional[TreeNode] = None
    prev: Optional[TreeNode] = None
    cur = root

    while cur:
        if cur.left is None:
            if prev is not None and prev.val > cur.val:
                if first is None:
                    first = prev
                second = cur
            prev = cur
            cur = cur.right
        else:
            pre = cur.left
            while pre.right and pre.right is not cur:
                pre = pre.right
            if pre.right is None:
                pre.right = cur
                cur = cur.left
            else:
                pre.right = None
                if prev is not None and prev.val > cur.val:
                    if first is None:
                        first = prev
                    second = cur
                prev = cur
                cur = cur.right

    if first is not None and second is not None:
        first.val, second.val = second.val, first.val