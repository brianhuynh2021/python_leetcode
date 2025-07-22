"""
Problem:
--------
Given an array of integers `nums` and an integer `k`, return the `k` most frequent elements.

Constraints:
------------
- The time complexity of your solution should ideally be better than O(n log n).
- The input list may contain duplicates.
- You may assume that `k` is always valid (1 ≤ k ≤ number of unique elements).

Approach (Brute Force):
-----------------------
1. Use a set to get distinct elements from nums.
2. For each distinct number, count its occurrences in nums using a nested loop.
3. Store the frequency and element as a tuple (count, num).
4. Sort the result list in descending order by frequency.
5. Extract and return the top-k elements from the sorted list.

Time Complexity:
----------------
- Counting frequencies: O(n * d), where d is the number of distinct elements.
- Sorting: O(d log d)
- Total: O(n * d + d log d)

Space Complexity:
-----------------
- O(d) for storing frequency pairs, where d is number of distinct elements.

Note:
-----
This is a brute-force solution. For optimized performance, consider using a hash map and min-heap or bucket sort.
"""

def top_k_frequent_elment_brute(nums: list[int], k: int)->list[int]:
    if not nums or k <= 0:
        raise ValueError('Input must be a list of integer numbers or k must be greater than 0')
    
    distinct_nums = set(nums)
    n = len(nums)
    result = []
    for num in distinct_nums:
        count = 0
        for j in range(n):
            if nums[j] == num:
                count += 1
        result.append((count, num))

    result.sort(reverse=True)
    return [item[1] for item in result[:k]]

import heapq
from collections import Counter

def top_k_frequent_elements_heap(nums: list[int], k: int) -> list[int]:
    """
    Return the k most frequent elements using a min-heap.

    Time Complexity:
    ----------------
    - Counting frequencies: O(n)
    - Heap operations: O(n log k)
    - Total: O(n log k)

    Space Complexity:
    -----------------
    - O(n) for frequency map
    - O(k) for the heap
    """
    if not nums or k <= 0:
        raise ValueError("Input must be a non-empty list and k > 0")

    # Step 1: Count frequencies using Counter
    freq_map = Counter(nums)  # O(n)

    # Step 2: Use a min-heap of size k
    heap = []

    for num, freq in freq_map.items():  # O(d)
        heapq.heappush(heap, (freq, num))  # O(log k)
        if len(heap) > k:
            heapq.heappop(heap)  # maintain size k

    # Step 3: Extract elements from the heap
    return [num for freq, num in heap]