"""
Chapter 18: Topological Sort (Graphs) — Implementations
Style: FAANG-quality, flake8-compliant, Python 3.10+ type hints.
"""

from __future__ import annotations

from collections import defaultdict, deque
from typing import Deque, Dict, Iterable, List, Optional, Set, Tuple


# ---------------------------------------------------------------------------
# 1) Topological Sort of a Directed Graph
# ---------------------------------------------------------------------------

def topo_sort(n: int, edges: List[Tuple[int, int]]) -> List[int]:
    """
    Return a topological ordering of nodes 0..n-1 or [] if cycle exists.

    Kahn's Algorithm.
    Time/Space: O(V+E).
    """
    graph: Dict[int, List[int]] = defaultdict(list)
    indeg: List[int] = [0] * n

    for u, v in edges:
        graph[u].append(v)
        indeg[v] += 1

    q: Deque[int] = deque([i for i in range(n) if indeg[i] == 0])
    order: List[int] = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return order if len(order) == n else []


# ---------------------------------------------------------------------------
# 2) Course Schedule II (LC 210)
# ---------------------------------------------------------------------------

def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    Return any valid order to finish all courses or [] if impossible.

    Edges: b -> a for pair (a, b).
    Time/Space: O(V+E).
    """
    graph: Dict[int, List[int]] = defaultdict(list)
    indeg: List[int] = [0] * num_courses

    for a, b in prerequisites:
        graph[b].append(a)
        indeg[a] += 1

    q: Deque[int] = deque([i for i in range(num_courses) if indeg[i] == 0])
    order: List[int] = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return order if len(order) == num_courses else []


# ---------------------------------------------------------------------------
# 3) Alien Dictionary
# ---------------------------------------------------------------------------

def alien_order(words: List[str]) -> str:
    """
    Recover a possible letter order from sorted dictionary 'words'.
    Return "" if no valid ordering exists.

    Time: O(L + |Σ| + E); Space: O(|Σ| + E).
    """
    # Collect unique letters
    letters: Set[str] = set()
    for w in words:
        for ch in w:
            letters.add(ch)

    graph: Dict[str, List[str]] = defaultdict(list)
    indeg: Dict[str, int] = {ch: 0 for ch in letters}

    # Build edges from adjacent word pairs
    for w1, w2 in zip(words, words[1:]):
        # Invalid prefix case: longer word before its prefix
        if len(w1) > len(w2) and w1.startswith(w2):
            return ""

        # Add first differing character edge
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                graph[c1].append(c2)
                indeg[c2] += 1
                break
        # If all matched and no prefix violation, no edge added

    # Kahn's algorithm over letters
    q: Deque[str] = deque([c for c in letters if indeg[c] == 0])
    order: List[str] = []

    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return "".join(order) if len(order) == len(letters) else ""


# ---------------------------------------------------------------------------
# 4) Sequence Reconstruction (LC 444)
# ---------------------------------------------------------------------------

def sequence_reconstruction(org: List[int], seqs: List[List[int]]) -> bool:
    """
    Check if 'org' is the unique sequence reconstructable from 'seqs'.

    Uniqueness via Kahn: queue size must be exactly 1 at each step,
    and the popped node must match org[idx]. Also ensure all elements
    in org appear and no extra elements exist.
    Time/Space: O(V+E).
    """
    if not org:
        return False

    # Gather all nodes present in seqs
    nodes: Set[int] = set()
    for s in seqs:
        nodes.update(s)

    # Must contain exactly the elements in org
    if set(org) != nodes or not nodes:
        return False

    graph: Dict[int, List[int]] = defaultdict(list)
    indeg: Dict[int, int] = {x: 0 for x in nodes}

    # Build edges from consecutive pairs in each sequence
    for s in seqs:
        for a, b in zip(s, s[1:]):
            graph[a].append(b)
            indeg[b] += 1

    # Kahn with uniqueness
    q: Deque[int] = deque([x for x in nodes if indeg[x] == 0])
    idx = 0

    while q:
        if len(q) != 1:
            return False  # not unique
        u = q.popleft()

        if idx >= len(org) or u != org[idx]:
            return False
        idx += 1

        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return idx == len(org)


# ---------------------------------------------------------------------------
# Sanity checks
# ---------------------------------------------------------------------------

def _test_topo_sort() -> None:
    n = 6
    edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
    order = topo_sort(n, edges)
    # Check order length and precedence constraints
    assert len(order) == n
    pos = {v: i for i, v in enumerate(order)}
    for u, v in edges:
        assert pos[u] < pos[v]


def _test_find_order() -> None:
    assert find_order(2, [[1, 0]]) in ([0, 1],)
    assert find_order(2, [[1, 0], [0, 1]]) == []


def _test_alien_order() -> None:
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    res = alien_order(words)
    assert res != ""  # one valid order is "wertf"


def _test_sequence_reconstruction() -> None:
    org = [1, 2, 3]
    seqs = [[1, 2], [1, 3], [2, 3]]
    assert sequence_reconstruction(org, seqs) is True

    org2 = [1, 2, 3]
    seqs2 = [[1, 2], [1, 3]]
    assert sequence_reconstruction(org2, seqs2) is False  # not unique


if __name__ == "__main__":
    _test_topo_sort()
    _test_find_order()
    _test_alien_order()
    _test_sequence_reconstruction()
    print("All Chapter 18 tests passed.")