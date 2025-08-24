

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