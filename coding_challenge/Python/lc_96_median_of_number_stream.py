

def median_number_stream_brute(nums: list[int]) -> list[int]:
    if not nums:
        return []
    copy = []
    result = []
    for num in nums:
        copy.append(num)
        copy.sort()
        mid = len(copy) // 2
        if len(copy) % 2 != 0:   
            median = copy[mid]
        else:
            median = (copy[mid] + copy[mid - 1]) / 2.0
        result.append(median)
    return result

import bisect

def median_number_stream_brute_with_bisect(nums):
    arr = []
    result = []
    for num in nums:
        bisect.insort(arr, num)
        n = len(nums)
        if n % 2 == 1:
            median = arr[n//2]
        else:
            median = (arr[n//2 - 1] + arr[n//2]) / 2.0
        result.append(median)
    return result

# Using heap
from heapq import heappush, heappop
class MedianFinder:
    """
    Two-heap running-median structure.
    - low: max-heap via negatives (stores lower half)
    - high: min-heap (stores upper half)
    """
    def __init__(self) -> None:
        self.low: list[int] = [] # max-heap (store as negative)
        self.high: list[int] = [] # min-heap
        
    
    def add_num(self, num: int) -> None:
        heappush(self.low, -num)
        heappush(self.high, -heappop(self.low))
        if len(self.high) > len(self.low):
            heappush(self.low, -heappop(self.high))
            
    def get_median(self) -> float:
        if not self.low:
            return 0.0
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2.0
    
def median_number_stream_optimized(nums: list[int]) -> list[float]:
    """
    Return the running median after each insertion using two heaps.
    Time per insert: O(log n), total O(n log n). Space: O(n)
    """
    out: list[float] = []
    if not nums:
        return out
    mf = MedianFinder()
    for x in nums:
        mf.add_num(x)
        out.append(mf.get_median())
    return out


print(median_number_stream_optimized([2, 1, 5]))
