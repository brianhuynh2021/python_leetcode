"""
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
"""
from typing import List


def sliding_window_max_brute(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if n == 0 or k == 0:
        return []

    result = []
    for i in range(n - k + 1):
        window = nums[i : i + k]
        max_value = max(window)
        result.append(max_value)
    return result


from collections import deque
from typing import List


def sliding_window_max(nums: List[int], k: int) -> List[int]:
    if not nums or k == 0:
        return []

    n = len(nums)
    result = []
    dq = deque()  # stores indices

    for i in range(n):
        # Step 1: Remove indices outside the window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Step 2: Remove smaller values from back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Step 3: Add current index
        dq.append(i)

        # Step 4: Append max in window to result
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result
