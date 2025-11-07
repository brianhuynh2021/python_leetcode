# Chapter 18: Topological Sort (Graphs) — MIT-Style Notes

> Goal: Understand partial orders in DAGs. Start from brute force (try permutations), find why it fails, then derive linear-time Kahn/DFS solutions. Emphasize invariants (in-degree 0 frontier) and cycle detection.

---

## 1) Topological Sort of a Directed Graph

**Problem.** Given `n` nodes labeled `0..n-1` and directed edges, return a topological ordering or empty if a cycle exists.

**Brute-force (why it fails).** Try all permutations and check if it respects edges → **O(n! · E)**, intractable beyond tiny `n`.

**Efficient formulations.**
1) **Kahn’s Algorithm (BFS on in-degree 0).**  
   - Build graph + `in_deg`.  
   - Queue := all nodes with `in_deg == 0`.  
   - Pop `u`, append to order, decrement in-degree of its neighbors; newly zero → enqueue.  
   - If we output < `n` nodes, graph has a cycle.
2) **DFS (postorder on DAG).**  
   - 3-color: 0=unvisited,1=visiting,2=done.  
   - On back-edge to `visiting`, detect cycle.  
   - Push `u` to stack when finished; reverse at end.

**Complexity.** **O(V+E)** time, **O(V+E)** space.

**Invariants.** Every popped node in Kahn’s has no incoming edges among remaining nodes. DFS stack is a reverse topological order for DAGs.

---

## 2) Course Schedule II (LC 210)

**Problem.** Given `numCourses` and prerequisites pairs `(a, b)` meaning `b -> a`, return any valid ordering to finish all courses or empty if impossible.

**Brute-force.** All course permutations → factorial.

**Efficient.** **Kahn** or **DFS**. We implement **Kahn** to match interviewer expectations and ease of cycle detection.

**Complexity.** **O(V+E)** time, **O(V+E)** space.

**Edge cases.** No prerequisites, self-loop, disconnected components.

---

## 3) Alien Dictionary

**Problem.** Given an ordered list of words in an unknown language, recover a valid ordering of its letters (any valid one). If impossible/inconsistent, return empty.

**Brute-force.** Try all permutations of letters (up to 26!): impossible.

**Key insight.** Adjacent dictionary words encode precedence constraints at the **first differing character**.  
- For each adjacent pair `(w1, w2)`, find first `i` where `w1[i] != w2[i]`; then `w1[i] -> w2[i]`.  
- Invalid case: if `w2` is a prefix of `w1` (e.g., `"abc"`, `"ab"`), contradiction ⇒ no solution.

**Efficient.** Build graph on **all unique letters**, add edges from the constraints above, then **toposort (Kahn)**.

**Complexity.** Let `L = total length of words`, `Σ` letters. **O(L + |Σ| + E)** time, **O(|Σ| + E)** space.

**Edge cases.** Duplicated edges, single word, prefix violation.

---

## 4) Sequence Reconstruction (LC 444)

**Problem.** Given a target sequence `org` and a list of subsequences `seqs`, check whether `org` is the **unique** shortest sequence that can be reconstructed. Equivalently: the partial order implied by `seqs` has a **unique** topological order and that order equals `org`.

**Brute-force.** Generate all topological orders (potentially exponential).

**Efficient (Kahn with uniqueness check).**
- Build graph across all numbers appearing in `seqs`.  
- Kahn’s algorithm, **but** enforce uniqueness: the queue of in-degree-zero nodes must have **size exactly 1** at each step.  
- While popping, verify that popped item equals `org[idx]`. At the end, ensure all nodes processed and `idx == len(org)`.

**Complexity.** **O(V+E)** time, **O(V+E)** space.

**Edge cases.** Missing numbers not present in `seqs`, empty `seqs`, repeated pairs, gaps, elements outside `org`.

---

# Complexity Summary

| Problem | Time | Space |
|---|---|---|
| Topological Sort | O(V+E) | O(V+E) |
| Course Schedule II | O(V+E) | O(V+E) |
| Alien Dictionary | O(L + Σ + E) | O(Σ + E) |
| Sequence Reconstruction | O(V+E) | O(V+E) |

---

# Implementation Notes (FAANG + Flake8)

- Prefer `defaultdict(list)` and integer labels where given.  
- Safety checks for invalid inputs, prefix conditions, and cycles.  
- Keep helpers private (`_build_graph_*`).  
- Unit-like sanity tests under `__main__`.