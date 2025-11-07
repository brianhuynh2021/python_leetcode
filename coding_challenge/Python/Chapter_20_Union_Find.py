"""
Chapter 20: Union Find (Disjoint Set) — Implementations
Style: FAANG-quality, flake8-compliant, Python 3.10+ type hints.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from typing import Dict, List, Tuple


# ---------------------------------------------------------------------------
# DSU (Disjoint Set Union) with path compression & union by size
# ---------------------------------------------------------------------------

@dataclass
class DSU:
    parent: List[int]
    size: List[int]
    count: int

    @classmethod
    def with_n(cls, n: int) -> "DSU":
        return cls(parent=list(range(n)), size=[1] * n, count=n)

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path halving
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.count -= 1
        return True


# ---------------------------------------------------------------------------
# 1) Number of Connected Components in Undirected Graph (LC 323)
# ---------------------------------------------------------------------------

def count_components(n: int, edges: List[Tuple[int, int]]) -> int:
    """
    Return number of connected components.
    Time: O(n + m α(n)); Space: O(n).
    """
    dsu = DSU.with_n(n)
    for u, v in edges:
        dsu.union(u, v)
    return dsu.count


# ---------------------------------------------------------------------------
# 2) Graph Valid Tree (LC 261)
# ---------------------------------------------------------------------------

def valid_tree(n: int, edges: List[Tuple[int, int]]) -> bool:
    """
    A valid tree has exactly n-1 edges and is connected (acyclic).
    Use DSU to detect cycles; edge count gives connectivity.
    """
    if len(edges) != n - 1:
        return False
    dsu = DSU.with_n(n)
    for u, v in edges:
        if not dsu.union(u, v):
            return False  # cycle
    return True  # n-1 edges and no cycles implies connected


# ---------------------------------------------------------------------------
# 3) Accounts Merge (LC 721)
# ---------------------------------------------------------------------------

def accounts_merge(accounts: List[List[str]]) -> List[List[str]]:
    """
    Merge accounts that share any email.
    Returns: [name] + sorted unique emails per merged account.
    """
    # Map each unique email to an id and remember its name.
    email_to_id: Dict[str, int] = {}
    email_to_name: Dict[str, str] = {}
    next_id = 0

    # First pass: assign ids and union emails within the same account.
    # We don't yet know n; collect emails to compute it.
    buckets: List[List[int]] = []  # temp per-account ids

    for acc in accounts:
        name, *emails = acc
        ids: List[int] = []
        for email in emails:
            if email not in email_to_id:
                email_to_id[email] = next_id
                email_to_name[email] = name
                next_id += 1
            ids.append(email_to_id[email])
        buckets.append(ids)

    dsu = DSU.with_n(next_id)
    for ids in buckets:
        for i in range(1, len(ids)):
            dsu.union(ids[0], ids[i])

    # Group emails by root
    root_to_emails: Dict[int, List[str]] = defaultdict(list)
    for email, idx in email_to_id.items():
        root = dsu.find(idx)
        root_to_emails[root].append(email)

    # Build output
    res: List[List[str]] = []
    for emails in root_to_emails.values():
        emails.sort()
        name = email_to_name[emails[0]]
        res.append([name] + emails)

    # Optional: stable order
    res.sort(key=lambda row: (row[0], row[1:]))
    return res


# ---------------------------------------------------------------------------
# 4) Redundant Connection (LC 684)
# ---------------------------------------------------------------------------

def find_redundant_connection(edges: List[Tuple[int, int]]) -> List[int]:
    """
    Given edges of an undirected graph with nodes labeled 1..n,
    return the edge that creates a cycle (last one if multiple).
    """
    # n is the number of nodes; derive from edges
    n = 0
    for u, v in edges:
        n = max(n, u, v)

    dsu = DSU.with_n(n + 1)  # 1-based indexing; ignore index 0
    redundant: List[int] = []
    for u, v in edges:
        if not dsu.union(u, v):
            redundant = [u, v]
    return redundant


# ---------------------------------------------------------------------------
# Sanity checks
# ---------------------------------------------------------------------------

def _test_count_components() -> None:
    n = 5
    edges = [(0, 1), (1, 2), (3, 4)]
    assert count_components(n, edges) == 2


def _test_valid_tree() -> None:
    assert valid_tree(5, [(0, 1), (0, 2), (0, 3), (1, 4)]) is True
    assert valid_tree(5, [(0, 1), (1, 2), (2, 3), (1, 3), (1, 4)]) is False  # cycle
    assert valid_tree(4, [(0, 1), (2, 3)]) is False  # edges != n - 1


def _test_accounts_merge() -> None:
    accounts = [
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["Mary", "mary@mail.com"],
    ]
    out = accounts_merge(accounts)
    # Expect John's emails merged, plus Mary's and johnnybravo separate
    names = sorted([row[0] for row in out])
    assert names == ["John", "John", "Mary"]


def _test_redundant_connection() -> None:
    edges = [(1, 2), (1, 3), (2, 3)]
    assert find_redundant_connection(edges) == [2, 3]


if __name__ == "__main__":
    _test_count_components()
    _test_valid_tree()
    _test_accounts_merge()
    _test_redundant_connection()
    print("All Chapter 20 tests passed.")