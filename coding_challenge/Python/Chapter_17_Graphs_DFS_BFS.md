# Chapter 17: Graphs (DFS/BFS) — MIT-Style Notes

> Goal: Build intuition first. Start from brute force, identify bottlenecks, then derive an efficient DFS/BFS formulation. Show invariants, prove correctness informally, and compute time/space complexity.

---

## 1) Number of Islands

**Problem.** Given a 2D grid of `'1'` (land) and `'0'` (water), count the number of islands (4-directional adjacency).

**Brute-force idea (naïve).** For each cell `'1'`, do a flood-fill over the entire grid from scratch to check what it reaches → **O((mn)^2)** in worst case.

**Observation → State Compression.** We need to visit each cell at most once. Mark visited as we expand from a land cell. Every time we hit an unvisited `'1'`, that’s a new island; DFS/BFS from it to mark the whole component.

**Efficient formulation.**
- Iterate cells; when you see `'1'` and not visited, `ans += 1` and run DFS/BFS to mark all reachable land.
- Each cell enqueued/dequeued/visited once → **O(mn)** time, **O(mn)** space worst-case.

**MIT-style invariants.**
- Each land cell is discovered by exactly one component search.
- Visited set partitions land cells into disjoint components.

**Edge cases.**
- Empty grid. Single row/column. All water. All land.

---

## 2) Clone Graph

**Problem.** Given a node in a connected undirected graph (LeetCode Node with `.val`, `.neighbors`), return a deep copy.

**Brute-force idea.** Recursive copy that naively re-copies neighbors → cycles cause infinite recursion.

**Key insight.** Maintain a map `old -> new` (hash map). When cloning a node, if it’s already in the map, reuse it. Traverse the original graph with DFS or BFS, creating copies on the fly.

**Efficient formulation.**
- BFS from start node, map original to cloned node.
- For each popped node, wire up neighbor clones (create if missing).

**Complexity.** **O(V + E)** time, **O(V)** space (hash map + queue/stack).

**Edge cases.**
- `node is None` → return `None`.
- Single node with/without self-loop.

---

## 3) Course Schedule

**Problem.** `numCourses`, `prerequisites` pairs `(a, b)` meaning `b -> a`. Can we finish all courses? (DAG check)

**Brute-force idea.** Try all permutations/topological orders → factorial blowup.

**Two standard solutions.**
1. **Kahn’s algorithm (BFS / in-degree).** Repeatedly pick nodes of in-degree 0; remove edges; count visited.
2. **DFS cycle detection.** 3-color or recursion stack.

**Efficient formulation (Kahn).**
- Build graph + in-degrees.
- Push all 0 in-degree to queue.
- Pop, decrement neighbors; push those that reach 0.
- If processed count == `numCourses` → True else False.

**Complexity.** **O(V + E)** time, **O(V + E)** space.

**Edge cases.**
- No prerequisites. Self-dependency. Disconnected graph.

---

## 4) Pacific Atlantic Water Flow

**Problem.** From a height matrix, water can flow from cell to neighbors with **height ≥ next height** (i.e., downhill or flat). Find cells that can reach both the Pacific (top/left edges) **and** Atlantic (bottom/right edges).

**Brute-force idea.** From each cell, DFS outward checking reachability to oceans → **O(mn·mn)**.

**Reverse-graph insight.** Instead of starting from each cell, **start two multi-source searches from the oceans inward** using the reversed condition:
- In reverse, we can move from `A` to neighbor `B` if `height[B] ≥ height[A]` (so original water could flow from `B` to `A`).
- Run DFS/BFS from Pacific edges to mark `pac_reach`, and from Atlantic edges to mark `atl_reach`.
- Answer is intersection of marks.

**Complexity.** **O(mn)** time/space.

**Edge cases.**
- 1x1 grid. Flat grid. Strictly increasing/decreasing rows/cols.

---

## 5) Rotten Oranges

**Problem.** Grid with `0` empty, `1` fresh, `2` rotten. Each minute, fresh adjacent (4-dir) to rotten become rotten. Return minutes to rot all or `-1` if impossible.

**Brute-force idea.** Simulate minute-by-minute rescanning the whole grid → **O(T·mn)** with big constant.

**BFS wavefront insight.**
- Multi-source BFS: enqueue **all rotten** with time 0.
- Pop (cell, t), infect fresh neighbors → enqueue with time `t+1`. Track last time used to infect.
- If any fresh remain at the end → `-1` else last time.

**Complexity.** **O(mn)** time, **O(mn)** space.

**Edge cases.**
- No fresh. No rotten. Isolated fresh.

---

## 6) Word Ladder

**Problem.** Shortest transformation from `beginWord` to `endWord` by changing 1 letter at a time, each intermediate must be in `wordList`. Return length, or 0 if not possible.

**Brute-force idea.** BFS where edges exist for words differing by one char, but naïvely checking neighbors is **O(N·L)** per node to scan all words.

**Optimization (pattern dictionary).**
- Precompute generic patterns: replace each position by `*` (e.g., `hot` → `*ot`, `h*t`, `ho*`).
- Map each pattern to words that match it.
- In BFS, neighbors are union over its patterns (amortized near **O(1)** per edge).

**Bidirectional BFS (further optimization).**
- Search from both ends to cut depth. Here we implement forward BFS with pattern map (clean + fast).

**Complexity.** With patterns: **O(N·L^2)** preprocessing + **O(N·L)** BFS, **O(N·L)** space.

**Edge cases.**
- `endWord` not in dictionary → 0. Duplicates in list. `beginWord == endWord` (return 1 by definition if required; LC returns 0 unless end in list and at least 1 step).

---

# Complexity Summary

| Problem | Time | Space |
|---|---|---|
| Number of Islands | O(mn) | O(mn) |
| Clone Graph | O(V+E) | O(V) |
| Course Schedule | O(V+E) | O(V+E) |
| Pacific Atlantic Water Flow | O(mn) | O(mn) |
| Rotten Oranges | O(mn) | O(mn) |
| Word Ladder | O(N·L^2 + N·L) | O(N·L) |

---

# Implementation Notes (FAANG + Flake8)

- Use `typing` hints; functions are pure where possible.
- Avoid global state; pass parameters explicitly.
- Use `deque` for BFS; avoid recursion depth issues by offering iterative forms.
- Small helpers are `private` (prefix `_`) when appropriate.
- Include unit-like sanity tests in `__main__` guard to illustrate usage.