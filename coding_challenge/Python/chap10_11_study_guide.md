# MIT-Style Study Guide — Chapter 10 & 11 (Intervals + Top-K/Heaps)

Each problem includes: **Goal**, **Core Concepts**, **Brute Force (first)**, **Complexity & Space**, and an **Optimized solution**.
Matching Python implementations are in `chap10_11_solutions.py`.

---

## Chapter 10: Merge Intervals

### 1) LC 56 — Merge Intervals
**Goal.** Given `intervals`, merge all overlapping intervals.

**Core Concepts.**
- Sort by start; greedily merge by extending the current window while overlaps.
- Overlap check: `curr.start <= merged[-1].end`.

**Brute Force (first).**
- Compare every pair to mark overlaps; repeatedly merge until stable.
- Complexity: `O(n^2)` time (worst), `O(n)` space.

**Optimized.**
- Sort once `O(n log n)`; scan to merge in one pass `O(n)`.
- Time: `O(n log n)`, Space: `O(n)` for output.

---

### 2) LC 57 — Insert Interval
**Goal.** Insert `newInterval` into sorted, non-overlapping `intervals` and merge if needed.

**Core Concepts.**
- Append all intervals ending **before** new interval.
- Merge overlaps with `newInterval`.
- Append the rest.

**Brute Force (first).**
- Insert then call “Merge Intervals” on the whole list.
- Time: `O(n log n)`, Space: `O(n)`.

**Optimized.**
- Single pass linear merge with the new interval.
- Time: `O(n)`, Space: `O(n)` for output.

---

### 3) LC 986 — Interval List Intersections
**Goal.** Given two lists of **disjoint, sorted** intervals A and B, return their intersections.

**Core Concepts.**
- Two pointers over A and B.
- Intersect if `max(starts) <= min(ends)`; advance the interval with the smaller end.

**Brute Force (first).**
- Compare every A with every B.
- Time: `O(n*m)`, Space: `O(1)` extra.

**Optimized.**
- Two-pointer linear sweep.
- Time: `O(n+m)`, Space: `O(1)` extra (plus output).

---

### 4) LC 253 — Meeting Rooms II (Minimum Meeting Rooms)
**Goal.** Given meeting intervals, find the minimum rooms to host all meetings.

**Core Concepts.**
- Sweep line: separate and sort starts vs. ends.
- Or min-heap of end-times to track active meetings.

**Brute Force (first).**
- For each meeting, try to reuse any room by checking overlaps naively.
- Time: `O(n^2)`, Space: `O(n)`.

**Optimized.**
- Sort starts/ends; sweep with two pointers → peak overlap.
- Or push/pop end times in a min-heap.
- Time: `O(n log n)`, Space: `O(n)`.

---

### 5) LC 759 — Employee Free Time
**Goal.** Given multiple employees' busy intervals (each employee's list is disjoint and sorted), return the common **free time** intervals (positive length).

**Core Concepts.**
- Flatten all busy intervals, sort by start, and merge to get the union (busy).
- Gaps between consecutive merged busy intervals are free times.

**Brute Force (first).**
- Compare all pairs to union; repeat until stable.
- Time: `O(k^2)` on all intervals, Space: `O(k)`.

**Optimized.**
- Min-heap by start, or flatten+sort then single pass merge.
- Time: `O(k log k)`, Space: `O(k)`.

---

## Chapter 11: Top K Elements (Heaps / Selection)

### 6) LC 703 — Kth Largest Element in a Stream
**Goal.** Maintain the k-th largest as numbers stream in.

**Core Concepts.**
- Keep a **min-heap** of size ≤ k. Heap top is k-th largest.

**Brute Force (first).**
- Store all elements; on each `add`, sort descending and pick k-th.
- Time per add: `O(n log n)`, Space: `O(n)`.

**Optimized.**
- Min-heap of size k; push and pop if size>k.
- Per add: `O(log k)`, Space: `O(k)`.

---

### 7) LC 347 — Top K Frequent Elements
**Goal.** Return k elements with highest frequency.

**Core Concepts.**
- Frequency map.
- Either min-heap of (freq, value) size k, or **bucket sort** by frequency.

**Brute Force (first).**
- Sort all unique elements by frequency.
- Time: `O(n log n)` (on distincts), Space: `O(n)`.

**Optimized.**
- Bucket sort: `O(n)` average.
- Or min-heap: `O(n log k)`.

---

### 8) LC 973 — K Closest Points to Origin
**Goal.** Return k points closest to origin by Euclidean distance.

**Core Concepts.**
- Use distance^2 to avoid sqrt.
- Either **max-heap** size k, or quickselect.

**Brute Force (first).**
- Sort all by distance and take k.
- Time: `O(n log n)`, Space: `O(1)` extra.

**Optimized.**
- Max-heap size k: `O(n log k)`.
- Or quickselect: average `O(n)`.

---

### 9) LC 1167 — Minimum Cost to Connect Sticks (Connect Ropes)
**Goal.** Combine ropes; cost of connecting two ropes is their sum; return minimum total cost to connect all.

**Core Concepts.**
- Always connect two **smallest** first → Huffman-like greedy with min-heap.

**Brute Force (first).**
- Repeatedly scan to find two minimums, connect, append; repeat.
- Time: `O(n^2)`, Space: `O(1)` extra.

**Optimized.**
- Min-heap; pop two, push back sum.
- Time: `O(n log n)`, Space: `O(n)`.

---

### 10) LC 378 — Kth Smallest in a Sorted Matrix
**Goal.** Matrix rows and columns are sorted ascending. Find the k-th smallest number.

**Core Concepts.**
- Either min-heap seeded by column heads, or value-space binary search using `count≤mid` in `O(n)`.

**Brute Force (first).**
- Flatten then sort.
- Time: `O(n^2 log n)`, Space: `O(n^2)`.

**Optimized.**
- Min-heap: `O(k log n)`.
- Binary search over value range with stair-walk count: `O(n log(range))`.

---

### 11) LC 451 — Sort Characters By Frequency (Frequency Sort)
**Goal.** Sort characters in string by descending frequency.

**Core Concepts.**
- Count then bucket by frequency or use a max-heap.

**Brute Force (first).**
- Sort by custom key using counts.
- Time: `O(n log n)`, Space: `O(n)`.

**Optimized.**
- Bucket: `O(n)` average; Max-heap: `O(n log σ)`.

---

## See `chap10_11_solutions.py` for concrete Python implementations.