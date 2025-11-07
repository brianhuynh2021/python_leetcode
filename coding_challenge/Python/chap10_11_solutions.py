from __future__ import annotations

from dataclasses import dataclass
from heapq import heappush, heappop, heapify
from typing import List, Optional, Tuple, Dict


# ===============================================================
# Chapter 10: Merge Intervals
# ===============================================================

# ---------- LC 56: Merge Intervals ----------
def merge_intervals_brutish(intervals: List[List[int]]) -> List[List[int]]:
    """
    Brute force: repeatedly merge any overlapping pair until stable.
    Time: O(n^2) worst, Space: O(n).
    """
    if not intervals:
        return []
    # Keep attempting to merge until no change
    changed = True
    current = intervals[:]
    while changed:
        changed = False
        current.sort(key=lambda x: x[0])
        merged: List[List[int]] = []
        for s, e in current:
            if not merged or s > merged[-1][1]:
                merged.append([s, e])
            else:
                merged[-1][1] = max(merged[-1][1], e)
                changed = True
        current = merged
    return current


def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Optimal: sort by start and merge in one pass.
    Time: O(n log n), Space: O(n) for output.
    """
    intervals.sort(key=lambda x: x[0])
    out: List[List[int]] = []
    for s, e in intervals:
        if not out or s > out[-1][1]:
            out.append([s, e])
        else:
            out[-1][1] = max(out[-1][1], e)
    return out


# ---------- LC 57: Insert Interval ----------
def insert_interval_brutish(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    Brute: insert then call merge_intervals.
    Time: O(n log n), Space: O(n).
    """
    return merge_intervals(intervals + [new_interval])


def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    Optimal: linear pass to insert and merge.
    Time: O(n), Space: O(n) for output.
    """
    res: List[List[int]] = []
    i = 0
    n = len(intervals)
    s, e = new_interval

    # Add all intervals before new_interval
    while i < n and intervals[i][1] < s:
        res.append(intervals[i])
        i += 1

    # Merge overlaps with new_interval
    while i < n and intervals[i][0] <= e:
        s = min(s, intervals[i][0])
        e = max(e, intervals[i][1])
        i += 1
    res.append([s, e])

    # Append the rest
    while i < n:
        res.append(intervals[i])
        i += 1

    return res


# ---------- LC 986: Interval List Intersections ----------
def intervals_intersection_brutish(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    """
    Brute force: compare all pairs.
    Time: O(n*m), Space: O(1) extra (excluding output).
    """
    res: List[List[int]] = []
    for s1, e1 in a:
        for s2, e2 in b:
            lo, hi = max(s1, s2), min(e1, e2)
            if lo <= hi:
                res.append([lo, hi])
    return res


def intervals_intersection(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    """
    Two-pointer linear sweep.
    Time: O(n+m), Space: O(1) extra (excluding output).
    """
    i = j = 0
    res: List[List[int]] = []
    while i < len(a) and j < len(b):
        s = max(a[i][0], b[j][0])
        e = min(a[i][1], b[j][1])
        if s <= e:
            res.append([s, e])
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return res


# ---------- LC 253: Meeting Rooms II ----------
def min_meeting_rooms_brutish(intervals: List[List[int]]) -> int:
    """
    Brute force: for each interval, count overlaps with others.
    Time: O(n^2), Space: O(1).
    """
    rooms = 0
    for i, (s1, e1) in enumerate(intervals):
        concurrent = 1
        for j, (s2, e2) in enumerate(intervals):
            if i == j:
                continue
            if not (e1 <= s2 or e2 <= s1):
                concurrent += 1
        rooms = max(rooms, concurrent)
    return rooms


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    """
    Optimal: sweep line over starts/ends.
    Time: O(n log n), Space: O(n).
    """
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)
    s = e = 0
    used = best = 0
    while s < len(starts):
        if starts[s] < ends[e]:
            used += 1
            best = max(best, used)
            s += 1
        else:
            used -= 1
            e += 1
    return best


# ---------- LC 759: Employee Free Time ----------
def employee_free_time_brutish(schedules: List[List[List[int]]]) -> List[List[int]]:
    """
    Brute: flatten and repeatedly merge until stable, then output gaps.
    Time: O(k^2), Space: O(k).
    """
    all_busy: List[List[int]] = [iv for emp in schedules for iv in emp]
    merged = merge_intervals_brutish(all_busy)
    # gaps between merged busy intervals are free
    free: List[List[int]] = []
    for i in range(1, len(merged)):
        prev_end = merged[i - 1][1]
        cur_start = merged[i][0]
        if cur_start > prev_end:
            free.append([prev_end, cur_start])
    return free


def employee_free_time(schedules: List[List[List[int]]]) -> List[List[int]]:
    """
    Optimal: flatten + sort + single-pass merge, then gaps.
    Time: O(k log k), Space: O(k).
    """
    all_busy: List[List[int]] = [iv for emp in schedules for iv in emp]
    all_busy.sort(key=lambda x: x[0])

    merged: List[List[int]] = []
    for s, e in all_busy:
        if not merged or s > merged[-1][1]:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)

    free: List[List[int]] = []
    for i in range(1, len(merged)):
        if merged[i][0] > merged[i - 1][1]:
            free.append([merged[i - 1][1], merged[i][0]])
    return free


# ===============================================================
# Chapter 11: Top K Elements
# ===============================================================

# ---------- LC 703: Kth Largest in a Stream ----------
class KthLargestBrutish:
    """
    Brute: keep all values; recompute via sort on each add.
    Time per add: O(n log n), Space: O(n).
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums[:]

    def add(self, val: int) -> int:
        self.arr.append(val)
        return sorted(self.arr, reverse=True)[self.k - 1]


class KthLargest:
    """
    Optimal: maintain a min-heap of size k.
    Time per add: O(log k), Space: O(k).
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[:]
        heapify(self.heap)
        while len(self.heap) > k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        elif val > self.heap[0]:
            heappush(self.heap, val)
            heappop(self.heap)
        return self.heap[0]


# ---------- LC 347: Top K Frequent Elements ----------
def top_k_frequent_brutish(nums: List[int], k: int) -> List[int]:
    """
    Brute: count then sort all uniques by frequency.
    Time: O(n log n) on distincts, Space: O(n).
    """
    freq: Dict[int, int] = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1
    items = sorted(freq.items(), key=lambda p: p[1], reverse=True)
    return [v for v, _ in items[:k]]


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """
    Optimized: bucket sort by frequency.
    Time: O(n) average, Space: O(n).
    """
    freq: Dict[int, int] = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1

    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
    for v, c in freq.items():
        buckets[c].append(v)

    ans: List[int] = []
    for c in range(len(buckets) - 1, 0, -1):
        for v in buckets[c]:
            ans.append(v)
            if len(ans) == k:
                return ans
    return ans


# ---------- LC 973: K Closest Points to Origin ----------
def k_closest_points_brutish(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Brute: sort all by squared distance.
    Time: O(n log n), Space: O(1) extra.
    """
    def d2(p: List[int]) -> int:
        return p[0] * p[0] + p[1] * p[1]
    return sorted(points, key=d2)[:k]


def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Optimized: maintain a max-heap of size k (store -dist).
    Time: O(n log k), Space: O(k).
    """
    heap: List[Tuple[int, int, int]] = []  # (-d2, x, y)
    for x, y in points:
        d = x * x + y * y
        heappush(heap, (-d, x, y))
        if len(heap) > k:
            heappop(heap)
    return [[x, y] for _, x, y in heap]


# ---------- LC 1167: Minimum Cost to Connect Sticks ----------
def connect_ropes_min_cost_brutish(ropes: List[int]) -> int:
    """
    Brute: repeatedly scan for two smallest; connect.
    Time: O(n^2), Space: O(1) extra.
    """
    arr = ropes[:]
    cost = 0
    while len(arr) > 1:
        arr.sort()
        a = arr.pop(0)
        b = arr.pop(0)
        s = a + b
        cost += s
        arr.append(s)
    return cost


def connect_ropes_min_cost(ropes: List[int]) -> int:
    """
    Optimal: min-heap greedy (Huffman-like).
    Time: O(n log n), Space: O(n).
    """
    heap = ropes[:]
    heapify(heap)
    cost = 0
    while len(heap) > 1:
        a = heappop(heap)
        b = heappop(heap)
        s = a + b
        cost += s
        heappush(heap, s)
    return cost


# ---------- LC 378: Kth Smallest in a Sorted Matrix ----------
def kth_smallest_matrix_brutish(matrix: List[List[int]], k: int) -> int:
    """
    Brute: flatten then sort.
    Time: O(n^2 log n), Space: O(n^2).
    """
    arr = [x for row in matrix for x in row]
    arr.sort()
    return arr[k - 1]


def kth_smallest_matrix(matrix: List[List[int]], k: int) -> int:
    """
    Optimized: value-space binary search with stair-walk count.
    Time: O(n log range), Space: O(1).
    """
    n = len(matrix)
    lo, hi = matrix[0][0], matrix[-1][-1]

    def count_le(x: int) -> int:
        # Count numbers <= x in O(n) by walking from bottom-left.
        i, j = n - 1, 0
        cnt = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= x:
                cnt += i + 1
                j += 1
            else:
                i -= 1
        return cnt

    while lo < hi:
        mid = (lo + hi) // 2
        if count_le(mid) >= k:
            hi = mid
        else:
            lo = mid + 1
    return lo


# ---------- LC 451: Sort Characters By Frequency ----------
def frequency_sort_brutish(s: str) -> str:
    """
    Brute: sort by frequency using a key.
    Time: O(n log n), Space: O(n).
    """
    from collections import Counter
    c = Counter(s)
    return ''.join(sorted(s, key=lambda ch: (c[ch], ch), reverse=True))


def frequency_sort(s: str) -> str:
    """
    Optimized: bucket by frequency.
    Time: O(n) average, Space: O(n).
    """
    from collections import Counter
    c = Counter(s)
    buckets: List[List[str]] = [[] for _ in range(len(s) + 1)]
    for ch, f in c.items():
        buckets[f].append(ch)
    out: List[str] = []
    for f in range(len(buckets) - 1, 0, -1):
        for ch in buckets[f]:
            out.append(ch * f)
    return ''.join(out)


# ===========================
# End of module
# ===========================