from typing import List

def find_largest_duplicate_bruteforce(nums: list) -> int:
    """
    Find the largest number in the list that appears at least twice.

    Args:
    nums (list): A list of integers.

    Returns:
    int: The largest integer that appears at least twice in the list. Returns -1 if no such number exists.
    """
    sorted_nums = sorted(nums, reverse=True)
    for i in range(len(sorted_nums) - 1):
        if sorted_nums[i] == sorted_nums[i + 1]:
            return sorted_nums[i]
    return -1
# big O = sorted(nlogn) + n ==> O(nlogn)

print(find_largest_duplicate_bruteforce([1, 3, 5, 7, 7, 9, 6, 8, 8, 8, 7]))

def find_largest_duplicate_optimized(nums : List[int]):
    seen = set()
    largest_num = float('-inf')
    for num in nums:
        if num in seen:
            largest_num = max(num, largest_num)
        else:
            seen.add(num)
    return largest_num

def process_data_with_message(data):
    """Function that USES find_largest_duplicate_optimized"""
    result = find_largest_duplicate_optimized(data)
    if result == -1:
        return "No duplicates found"
    return f"Largest duplicate is {result}"