# Chapter 20: Union Find (Disjoint Set) — MIT-Style Notes

> Goal: Maintain dynamic partition of elements into disjoint sets with **near O(1)** amortized unions/finds via **path compression + union by rank/size**. Use DSU to detect cycles, count components, and merge entities by equality constraints.

---

## Disjoint Set Union (DSU)

**API.**
- `find(x)`: return representative (root) of set containing `x`.
- `union(x, y)`: merge sets; return `False` if already same set (cycle detector in undirected graphs).
- `count`: number of disjoint sets (if initialized with `n` singletons).

**Brute force (why not).** Keep components as arrays/lists; merging is O(n). Repeated merges → O(nm).  
**Optimized.** Parent tree + **path compression** (flatten on `find`) and **union by size/rank**.  
**Complexity.** Amortized **α(n)** per op (inverse Ackermann), essentially constant.

**Invariants.**
- Each node points to some parent; roots point to themselves.
- Path compression preserves partition while reducing height.

---

## 1) Number of Connected Components in Undirected Graph (LC 323)

**Problem.** Given `n` nodes `0..n-1` and undirected `edges`, return the number of connected components.

**Brute force.** BFS/DFS from each unvisited node → O(n + m) (already good).  
**Union-Find approach.** Initialize `count = n`. For each edge `(u, v)`, if union succeeds, `count -= 1`. Return `count`.

**Complexity.** **O(n + m α(n))** time, **O(n)** space.

---

## 2) Graph Valid Tree (LC 261)

**Problem.** Given `n` and undirected `edges`, is it a tree?  
**Tree conditions.**
1) Must have exactly `n - 1` edges.  
2) Must be acyclic and connected.

**Union-Find solution.**
- If `len(edges) != n - 1` → `False`.  
- Union edges; if any union finds a same-set pair → cycle → `False`.  
- Otherwise `True` (edge count ensures connectivity).

**Complexity.** **O(n + m α(n))**, **O(n)** space.

---

## 3) Accounts Merge (LC 721)

**Problem.** Accounts `[name, email1, email2, ...]`, merge those that share any email; output merged accounts with unique sorted emails.

**Brute force.** Graph building + DFS over emails (ok), but can be verbose.  
**Union-Find solution.**
- Map each email to an index; union all emails within the same account.  
- Track `email -> name` (name consistent per connected component).  
- Group emails by root; for each root, output `[name] + sorted(emails)`.

**Complexity.** Let `E = #emails`, `A = #accounts`. Build map + unions: **O(E α(E))**; grouping + sort per component dominates: **O(E log E)** overall.

**Edge cases.** Multiple accounts with same name but disjoint emails remain separate.

---

## 4) Redundant Connection (LC 684)

**Problem.** In an undirected graph that started as a tree with one extra edge added, return the extra edge that creates a cycle (if multiple, return the last in input order).

**Union-Find solution.**
- Iterate edges; if `union(u, v)` fails, `(u, v)` is the redundant connection. Return it.

**Complexity.** **O(m α(n))** time, **O(n)** space.

---

# Complexity Summary

| Problem | Time | Space |
|---|---|---|
| Number of Connected Components | O(n + m·α(n)) | O(n) |
| Graph Valid Tree | O(n + m·α(n)) | O(n) |
| Accounts Merge | O(E·α(E) + E log E) | O(E) |
| Redundant Connection | O(m·α(n)) | O(n) |

---

# Implementation Notes (FAANG + Flake8)

- DSU implemented with path compression and union by size.  
- Prefer 0-based node indices internally.  
- Validate constraints early (e.g., `edges != n-1` for valid tree).  
- Clear, typed helpers; small sanity tests in `__main__`.