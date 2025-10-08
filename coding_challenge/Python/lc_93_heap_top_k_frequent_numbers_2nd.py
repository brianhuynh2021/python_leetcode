from collections import Counter
from heapq import heappop, heappush


def find_top_k_elment_heap(nums: list[int], k):
    if k <= 0:
        raise ValueError("k must be positive")
    if not nums:
        return []

    freq = Counter(nums)
    heap = []
    for num, f in freq.items():
        heappush(heap, (f, num))
        if len(heap) > k:
            heappop(heap)
    return [num for _, num in heap]
