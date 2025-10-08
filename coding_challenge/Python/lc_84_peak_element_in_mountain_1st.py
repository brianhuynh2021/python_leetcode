"""
🚩 Problem Statement

You’re given a mountain array — an array that:
	•	strictly increases to a peak,
	•	and then strictly decreases.

🏔️ Example:
arr = [1, 3, 5, 7, 6, 4, 2]
The peak is the highest element arr[i] such that:
arr[i - 1] < arr[i] > arr[i + 1]
"""


def brute_force_find_peak_elment(nums: list[int]):
    """
    Returns the index of the peak element in a mountain array.
    Assumes nums is a valid mountain array.
    """
    n = len(nums)
    if not nums or n < 3:
        raise ValueError("Input list must not be empty or must be at leat 3 elements")
    for i in range(1, n - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            return i
    raise ValueError("No peak found - input may not be a valid mountain array")


def optimized_find_peak_element(nums: list[int]) -> int:
    n = len(nums)
    if not nums or n < 3:
        raise ValueError("Input array must not be empty or must be aleast 3 elements")

    low = 0
    high = n - 1
    while low < high:
        mid = (low + high) // 2
        if nums[mid] < nums[mid + 1]:
            # Peak is the biggest one, so when nums[mid] < nums[mid + 1], we’re sure that mid and left side do not include peak
            low = mid + 1
        else:  # nums[mid] > nums[mid + 1] it perhaps peak but not always
            high = mid
    return low


print(optimized_find_peak_element([1, 3, 5, 7, 6, 4, 2, 0]))
print(optimized_find_peak_element([1, 8, 9, 11, 6, 4, 2, 0]))
