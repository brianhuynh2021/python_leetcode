def get_kth_largest_element(nums: list[int], k)->int:
    """
    Return the k-th largest element (1-based).
    Args:
        nums: Non-empty sequence of ints.
        k: 1 <= k <= len(nums)
    Returns:
        int: the k-th largest value
    Raises:
        ValueError: if nums is empty or k is out of range.
    """
    if not (1<= k < len(nums)):
        raise ValueError('Invalid k, k out of range')
    if not nums:
        raise ValueError('Nums must not be empty')
    
    sorted_nums = sorted(nums)
    print(sorted_nums)
    #return sorted(nums)[-k]
    return sorted_nums[k - 1]
    

print(get_kth_largest_element([2, 5, 7, 8, 9], 4))


from heapq import heappush, heappop

def get_kth_largest_element(nums: list[int], k)->int:
    if not (1<= k <= len(nums)):
        raise ValueError('Invalid k')
    if not nums:
        raise ValueError('nums must not be empty')
    heap : list[int] = []
    for num in nums:
        heappush(heap, num)
        if len(heap) > k:
            heappop(heap)
    return heap[0]

print(get_kth_largest_element([2, 5, 7, 8, 9], 3))