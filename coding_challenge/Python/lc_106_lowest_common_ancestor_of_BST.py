from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TreeNode:
    """Binary tree node."""
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def path_to(root: Optional[TreeNode], target: TreeNode) -> List[TreeNode]:
    """
    Return the path from root to target (inclusive). If not found, return [].

    Time: O(n)
    Space: O(n) recursion + path
    """
    path: List[TreeNode] = []

    def dfs(node: Optional[TreeNode]) -> bool:
        if not node:
            return False
        path.append(node)
        if node is target:
            return True
        if dfs(node.left) or dfs(node.right):
            return True
        path.pop()
        return False

    found = dfs(root)
    return path if found else []


def lowest_common_ancestor_bruteforce(
    root: Optional[TreeNode],
    p: TreeNode,
    q: TreeNode,
) -> Optional[TreeNode]:
    """
    LCA for a generic binary tree using paths.

    Time: O(n)
    Space: O(n)
    """
    p_path = path_to(root, p)
    q_path = path_to(root, q)
    lca: Optional[TreeNode] = None
    for a, b in zip(p_path, q_path):
        if a is b:
            lca = a
        else:
            break
    return lca