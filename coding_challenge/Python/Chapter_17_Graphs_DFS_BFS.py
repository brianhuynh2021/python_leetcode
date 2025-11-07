"""
Chapter 17: Graphs (DFS/BFS) — Implementations
Style: FAANG-quality, flake8-compliant, Python 3.10+ type hints.
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from typing import Deque, Dict, Iterable, List, Optional, Set, Tuple


# ---------------------------------------------------------------------------
# 1) Number of Islands
# ---------------------------------------------------------------------------

def num_islands(grid: List[List[str]]) -> int:
    """
    Count the number of islands ('1') in a grid (4-directional adjacency).

    Time: O(mn); Space: O(mn).
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    visited: Set[Tuple[int, int]] = set()

    def bfs(sr: int, sc: int) -> None:
        q: Deque[Tuple[int, int]] = deque([(sr, sc)])
        visited.add((sr, sc))
        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < m and 0 <= nc < n and
                    grid[nr][nc] == "1" and (nr, nc) not in visited
                ):
                    visited.add((nr, nc))
                    q.append((nr, nc))

    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1" and (r, c) not in visited:
                count += 1
                bfs(r, c)
    return count


# ---------------------------------------------------------------------------
# 2) Clone Graph
# ---------------------------------------------------------------------------

@dataclass
class GraphNode:
    """Undirected graph node."""
    val: int
    neighbors: List["GraphNode"]

    def __hash__(self) -> int:  # allow hashing by id
        return id(self)


def clone_graph(node: Optional[GraphNode]) -> Optional[GraphNode]:
    """
    Clone a connected undirected graph with potential cycles.

    Time: O(V+E); Space: O(V).
    """
    if node is None:
        return None

    clones: Dict[GraphNode, GraphNode] = {}
    q: Deque[GraphNode] = deque([node])
    clones[node] = GraphNode(node.val, [])

    while q:
        cur = q.popleft()
        for nei in cur.neighbors:
            if nei not in clones:
                clones[nei] = GraphNode(nei.val, [])
                q.append(nei)
            clones[cur].neighbors.append(clones[nei])

    return clones[node]


# ---------------------------------------------------------------------------
# 3) Course Schedule (Kahn's Algorithm)
# ---------------------------------------------------------------------------

def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    Return True if we can finish all courses (i.e., no directed cycle).

    Edges: b -> a meaning (a, b) in prerequisites.
    Time: O(V+E); Space: O(V+E).
    """
    graph: Dict[int, List[int]] = defaultdict(list)
    indeg: List[int] = [0] * num_courses

    for a, b in prerequisites:
        graph[b].append(a)
        indeg[a] += 1

    q: Deque[int] = deque(i for i in range(num_courses) if indeg[i] == 0)
    taken = 0

    while q:
        u = q.popleft()
        taken += 1
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return taken == num_courses


# ---------------------------------------------------------------------------
# 4) Pacific Atlantic Water Flow
# ---------------------------------------------------------------------------

def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    """
    Return coordinates [r, c] that can reach both the Pacific and Atlantic.

    Reverse-flow BFS/DFS from ocean borders inward.
    Time/Space: O(mn).
    """
    if not heights or not heights[0]:
        return []

    m, n = len(heights), len(heights[0])

    def bfs(starts: Iterable[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        vis: Set[Tuple[int, int]] = set(starts)
        q: Deque[Tuple[int, int]] = deque(starts)
        while q:
            r, c = q.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < m and 0 <= nc < n and
                    (nr, nc) not in vis and
                    heights[nr][nc] >= heights[r][c]
                ):
                    vis.add((nr, nc))
                    q.append((nr, nc))
        return vis

    pac_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
    atl_starts = [(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)]

    pac = bfs(pac_starts)
    atl = bfs(atl_starts)

    ans = [[r, c] for (r, c) in pac & atl]
    ans.sort()
    return ans


# ---------------------------------------------------------------------------
# 5) Rotten Oranges
# ---------------------------------------------------------------------------

def oranges_rotting(grid: List[List[int]]) -> int:
    """
    Multi-source BFS from all rotten; return minutes to rot all or -1.

    Time/Space: O(mn).
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    q: Deque[Tuple[int, int, int]] = deque()
    fresh = 0

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 2:
                q.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1

    last_time = 0
    while q:
        r, c, t = q.popleft()
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                q.append((nr, nc, t + 1))
                last_time = t + 1

    return -1 if fresh > 0 else last_time


# ---------------------------------------------------------------------------
# 6) Word Ladder (pattern adjacency + BFS)
# ---------------------------------------------------------------------------

def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    """
    Shortest transformation length from begin_word to end_word.

    Precompute pattern map to avoid O(N^2) neighbor scans.
    Time: O(N·L^2 + N·L), Space: O(N·L).
    """
    if end_word not in word_list:
        return 0

    L = len(begin_word)

    # Unique words set
    words: Set[str] = set(word_list)
    words.add(begin_word)

    # pattern -> list of words
    patterns: Dict[str, List[str]] = defaultdict(list)
    for w in words:
        if len(w) != L:
            # ignore words of other lengths
            continue
        for i in range(L):
            key = w[:i] + "*" + w[i + 1 :]
            patterns[key].append(w)

    # BFS
    q: Deque[Tuple[str, int]] = deque([(begin_word, 1)])
    seen: Set[str] = {begin_word}

    while q:
        cur, dist = q.popleft()
        if cur == end_word:
            return dist
        for i in range(L):
            key = cur[:i] + "*" + cur[i + 1 :]
            for nxt in patterns.get(key, ()):
                if nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, dist + 1))
            # Optional micro-optimization: clear list to avoid revisits
            patterns[key] = []
    return 0


# ---------------------------------------------------------------------------
# Sanity checks
# ---------------------------------------------------------------------------

def _test_num_islands() -> None:
    grid = [
        list("11000"),
        list("11000"),
        list("00100"),
        list("00011"),
    ]
    assert num_islands(grid) == 3


def _test_clone_graph() -> None:
    a = GraphNode(1, [])
    b = GraphNode(2, [])
    c = GraphNode(3, [])
    a.neighbors = [b, c]
    b.neighbors = [a, c]
    c.neighbors = [a, b]
    clone = clone_graph(a)
    assert clone is not a
    assert clone.val == 1
    assert len(clone.neighbors) == 2


def _test_can_finish() -> None:
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False


def _test_pacific_atlantic() -> None:
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    res = pacific_atlantic(heights)
    assert [0, 4] in res and [1, 3] in res and [1, 4] in res


def _test_oranges_rotting() -> None:
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1],
    ]
    assert oranges_rotting(grid) == 4


def _test_ladder_length() -> None:
    begin, end = "hit", "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert ladder_length(begin, end, word_list) == 5


if __name__ == "__main__":
    _test_num_islands()
    _test_clone_graph()
    _test_can_finish()
    _test_pacific_atlantic()
    _test_oranges_rotting()
    _test_ladder_length()
    print("All Chapter 17 tests passed.")