'''
🚩 Problem Statement

You’re given a mountain array — an array that:
	•	strictly increases to a peak,
	•	and then strictly decreases.

🏔️ Example:
arr = [1, 3, 5, 7, 6, 4, 2]
The peak is the highest element arr[i] such that:
arr[i - 1] < arr[i] > arr[i + 1]
'''

def brute_force_find_peak_elment(nums: list[int]):
    """
    Returns the index of the peak element in a mountain array.
    Assumes nums is a valid mountain array.
    """
    n = len(nums)
    if not nums or n < 3:
        raise ValueError('Input list must not be empty or must be at leat 3 elements')
    for i in range(1, n - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            return i
    raise ValueError('No peak found - input may not be a valid mountain array')

def optimized_find_peak_element(nums: list[int]):
    n = len(nums)
    if not nums or n < 3:
        raise ValueError('Input list must be not empty or at least 3 elements')
    
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high)//2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return high
        
            