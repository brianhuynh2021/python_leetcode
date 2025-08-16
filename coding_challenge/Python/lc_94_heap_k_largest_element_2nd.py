def kth_largest_element(nums, k):
    if not nums or not (0 < k <= len(nums)):
        raise ValueError("Not Valid")
    sorted_nums = sorted(nums)
    return sorted_nums[-k]

from heapq import heappush, heappushpop
def kth_largest_element_optimized(nums, k):
    if not nums or not (0 < k <= len(nums)):
        raise ValueError("Not Valid")
    heap = []
    for num in nums:
        if len(heap) < k:
            heappush(heap, num)
        else:
            heappushpop(heap, num)
    return heap[0]
    