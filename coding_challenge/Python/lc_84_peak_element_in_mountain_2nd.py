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
        raise ValueError('Input arr must not be empty or at least 3 elements')
    for i in range(1, n -1):
        if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
            return i
    raise ValueError('No peak value')

def optimized_find_peak_element(nums: list[int])->int:
    n = len(nums)
    if not nums or n < 3:
        raise ValueError('Input arr must not be empty or at least 3 elements')
    low = 0
    high = n - 1
    while low < high:
        mid = (low + high)//2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low
print(optimized_find_peak_element([1, 3, 5, 7, 6, 4 , 2, 0]))
print(optimized_find_peak_element([1, 8, 9, 11, 6, 4 , 2, 0]))