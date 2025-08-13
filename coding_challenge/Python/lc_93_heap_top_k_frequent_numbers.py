from __future__ import annotations

from collections import Counter
from heapq import heappush, heappop
from typing import List, Tuple


def top_k_frequent_bruteforce(nums: List[int], k: int) -> List[int]:
    """
    Baseline solution: count then sort by frequency descending.
    Returns up to k numbers with highest frequency (any tie-breaking is acceptable).
    If nums is empty, returns [].
    Raises:
        ValueError: if k <= 0.
    """
    if k <= 0:
        raise ValueError("k must be positive")
    if not nums:
        return []

    # Use libary Counter to count key and time appear of each item
    freq = Counter(nums)
    items = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
    
    return [num for num, _ in items[:k]]


def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    """
    Optimized solution using a min-heap of size k on (freq, num).
    Returns up to k numbers with highest frequency (any order).
    If nums is empty, returns [].
    Raises:
        ValueError: if k <= 0.
    """
    if k <= 0:
        raise ValueError("k must be positive")
    if not nums:
        return []

    freq = Counter(nums)  # O(n)
    heap: List[Tuple[int, int]] = []  # (frequency, number)

    for num, f in freq.items():  # O(m log k)
        heappush(heap, (f, num))
        if len(heap) > k:
            heappop(heap)

    # Any order is acceptable; extract just the numbers.
    return [num for _, num in heap]


def top_k_frequent_heap_sorted(nums: List[int], k: int) -> List[int]:
    """
    Same as top_k_frequent_heap but returns the result sorted by frequency descending.
    Note: additional O(k log k) to sort the heap snapshot.
    """
    if k <= 0:
        raise ValueError("k must be positive")
    if not nums:
        return []

    freq = Counter(nums)
    heap: List[Tuple[int, int]] = []

    for num, f in freq.items():
        heappush(heap, (f, num))
        if len(heap) > k:
            heappop(heap)

    # Sort by frequency desc; if you want deterministic tie-break,
    # add secondary key (e.g., num ascending).
    heap.sort(key=lambda fn: (-fn[0], fn[1]))
    return [num for _, num in heap]