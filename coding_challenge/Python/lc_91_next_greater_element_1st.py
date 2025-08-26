'''🔍 Problem Statement (Classic Version)

You’re given an array nums of integers. For each element in nums, find the next greater element — the first element to the right that is greater than the current one. If no such element exists, return -1 for that position.

Example:
Input:  [2, 1, 2, 4, 3]
Output: [4, 2, 4, -1, -1]
'''
'''Psudo code:
1. Edge case:
    if not nums:
        raise ValueError('Array nums must not be empty')
2. Initial result = len(nums)*[-1]
3. Main for loop from i to len(n):
        for loop from i + 1 to len(n):
            if nums[j] > compare_el:
                result[i] = nums[j]
                break
4. return result
'''

def next_greater_element_brute(nums: list[int]) -> list[int]:
    if not nums:
        raise ValueError("Array nums must not be empty")
    n = len(nums)
    result = n*[-1]
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                result[i] = nums[j]
                break
    return result

def next_greater_element_optimized(nums: list[int]) -> list[int]:
    if not nums:
        raise ValueError("Array nums must not be empty")
    
    stack = []
    result = [-1]*len(nums)
    for i, num in enumerate(nums):
        while stack and num > nums[stack[-1]]:
            index = stack.pop()
            result[index] = num
        stack.append(i)
    return result