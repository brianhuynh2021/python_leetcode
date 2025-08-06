def next_greater_element_brute(nums: list[int]) -> list[int]:
    if not nums:
        raise ValueError('The nums must not be empty')
    n = len(nums)
    result = n*[-1]
    
    for i in range(n):
        for j in range(i+1, n):
            if nums[j] > nums[i]:
                result[i] = nums[j]
    return result

def next_greater_element_optimized(nums: list[int]) -> list[int]:
    if not nums:
        raise ValueError('The nums must not be empty')
    result = len(nums)*[-1]
    stack = []
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            pop_index = stack.pop()
            result[pop_index] = num
        stack.append(i)
    return result
