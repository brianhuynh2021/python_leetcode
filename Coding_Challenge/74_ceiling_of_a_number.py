'''
❓ Problem Understanding First

Given a sorted array of integers arr[] and a target number key, find the ceiling of the number.

The ceiling of the key is the smallest element in the array that is greater than or equal to the key.
'''

# Method 1: use brute force algorithm

# def ceiling_of_a_number_brute_force(nums: list[int], target: int):
#     for num in nums:
#         if num >= target:
#             return num
#     return None

# This method is the worst case once the target > all nums
# It mean we have to check long time to get the result
# Ceiling mean ascendence
def ceiling_of_a_number(nums: list[int], target: int):
    n = len(nums)
    if not nums:
        return None
    low = 0
    high = n - 1
    result = -1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            low = mid + 1
        else:
            result = mid
            high = mid - 1
    return nums[result] if result != -1 else None
        