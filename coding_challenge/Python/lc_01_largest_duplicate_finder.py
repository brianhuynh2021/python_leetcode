def find_largest_duplicate(nums: list) -> int:
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


print(find_largest_duplicate([1, 3, 5, 7, 7, 9, 6, 8, 8, 8, 7]))

