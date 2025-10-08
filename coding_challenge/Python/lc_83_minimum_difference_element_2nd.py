def brute_force_find_min_diff_element(nums: list[int], target: int) -> int:
    """
    Find the element in the sorted list that has the smallest absolute difference with the target.
    If there are multiple such elements, return the smaller one.

    Args:
        nums (List[int]): A sorted list of integers.
        target (int): The target number to compare against.

    Returns:
        int: The number in nums that is closest to target.
    """
    min_el = nums[0]
    min_diff = abs(min_el - target)
    for num in nums[1:]:
        diff = abs(num - target)
        if diff < min_diff or (diff == min_diff and num < min_el):
            min_diff = diff
            min_el = num
    return min_el


def optimized_find_min_diff_element(nums: list[int], target: int) -> int:
    if not nums:
        raise ValueError("Input list must not be empty")
    low, high = 0, len(nums) - 1
    closest = nums[0]
    min_diff = abs(closest - target)
    while low <= high:
        mid = (low + high) // 2
        current_diff = abs(nums[mid] - target)
        if current_diff < min_diff or (
            current_diff == min_diff and nums[mid] < closest
        ):
            min_diff = current_diff
            closest = nums[mid]
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return nums[mid]
    return closest


assert optimized_find_min_diff_element([1, 3, 8, 10], 9) == 8
assert optimized_find_min_diff_element([5, 10, 15], 12) == 10
assert optimized_find_min_diff_element([4, 6, 10], 7) == 6
