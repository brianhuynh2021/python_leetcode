'''
You’re given:
	•	An array of integers nums
	•	A window size k

Your task:
👉 Slide the window of size k from left to right, and at each position, return the maximum element in the window.

⸻

🔢 Example:
nums = [1,3,-1,-3,5,3,6,7]
k = 3
Expected Output:
[3,3,5,5,6,7]
'''
from typing import List

def sliding_window_max_brute(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if n == 0 or k == 0:
        return []
    result = []
    for i in range(n-2):
        window = nums[i:i+k]
        max_value = max(window)
        result.append(max_value)
    return result

from collections import deque

import heapq

def sliding_window_max_heap(nums, k):
    max_heap = []
    result = []

    for i in range(len(nums)):
        heapq.heappush(max_heap, (-nums[i], i))

        # remove max if it's outside window
        while max_heap[0][1] <= i - k:
            heapq.heappop(max_heap)

        if i >= k - 1:
            result.append(-max_heap[0][0])  # get max value

    return result