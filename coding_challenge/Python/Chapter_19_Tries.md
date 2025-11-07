# Chapter 19: Tries — MIT-Style Notes

> Goal: Model prefix constraints efficiently. Start with brute force (string scans / hashing), identify hot paths (prefix checks & repeated lookups), then introduce a **Trie (prefix tree)** to reduce per-query work from O(L·Σ) scans to O(L) traversals.

---

## 1) Implement Trie (Prefix Tree)

**Problem.** Design a data structure that supports `insert(word)`, `search(word)`, and `starts_with(prefix)`.

**Brute force.** Store words in a hash set; `starts_with` requires scanning all words → **O(N · L)** per query.

**Trie insight.** Store letters along a path. Each node has up to `|alphabet|` children and a boolean `is_end`.  
- Insert: walk/create nodes; set `is_end=True` at the end.  
- Search: walk nodes; check `is_end`.  
- StartsWith: walk nodes; success if traversal finishes.

**Complexity.** Let `L` be the word length. Insert/Search/Prefix: **O(L)** time, **O(Σ L)** total space.

**Invariants.** Path from root to a node spells the prefix; `is_end` marks whole word completion.

---

## 2) Word Search II

**Problem.** Given a board of letters and `words`, return all words that can be formed via adjacent (4-dir) cells without reuse in one word.

**Brute force.** For each word, try to find it on the board with DFS → **O(#words · m · n · 4^L)** worst-case.

**Pruning via Trie.** Build a trie of all words and **DFS once per cell**, pruning whenever a prefix is not in the trie.  
- Mark cells as visited during a search path (temporarily set to `'#'`).  
- When reaching a trie node with `is_end`, record the word (avoid duplicates by nulling the saved word at that node).

**Complexity.** Amortized **O(mn · 4 · 3^{L-1})** with strong pruning; space **O(Σ L)** for trie + recursion stack.

**Edge cases.** Duplicate words, overlapping paths, tiny boards.

---

## 3) Replace Words

**Problem.** Given dictionary `roots` and a sentence, replace each word with the shortest root that is a prefix of it. If none, keep the original word.

**Brute force.** For each word, check all roots → **O(#words · #roots · L)**.

**Trie solution.** Insert all roots; for each sentence word, traverse the trie and stop at the **first** `is_end`. That prefix is the replacement.

**Complexity.** Build **O(Σ L)**, query per word **O(L)**.

**Invariant.** First `is_end` along the path equals shortest root.

---

## 4) Search Suggestions System

**Problem.** Given product names and `searchWord`, return for each prefix of `searchWord` up to 3 lexicographically smallest suggestions.

**Brute force.** For each prefix, scan all products and take smallest three → **O(#prefixes · N · L)**.

**Two efficient strategies.**  
1) **Sorted + Binary Search (bisect).** Prefix window via lower bound + slice → simple and very fast.  
2) **Trie with per-node top-3 cache.** Insert products in sorted order and store up to 3 names at each node (monotone queue). Query is O(len(prefix)).

**We implement the Trie approach** (it fits the chapter), with an aside that bisect is also great in interviews.

**Complexity.** Build **O(Σ L)**; query **O(P)** for prefixes length `P`, since we only read cached lists.

---

# Complexity Summary

| Problem | Time | Space |
|---|---|---|
| Implement Trie | O(L) | O(Σ L) |
| Word Search II | ~O(mn · 3^{L-1}) amortized | O(Σ L) |
| Replace Words | O(total sentence chars) | O(Σ L) |
| Search Suggestions | Build O(Σ L), Query O(P) | O(Σ L) |

---

# Implementation Notes (FAANG + Flake8)

- Use `@dataclass` for `TrieNode` with `children: dict[str, TrieNode]` and `is_end: bool`.  
- Avoid global state; keep helper methods `_find_node`, `_dfs`.  
- For Word Search II, null-out `node.word` after adding to results to de-duplicate in **O(1)**.  
- For Suggestions, sort products first; at insert, append to `node.suggestions` if `len < 3` (sorted order ensures minimal maintenance).  
- Include sanity tests under `__main__`.