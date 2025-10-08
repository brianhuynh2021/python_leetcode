def brute_force_dutch_flag(nums: list[int]) -> None:
    """
    Sorts an array containing only 0s, 1s, and 2s in-place using a brute force approach.

    This function modifies the input list `nums` by first counting the number of 0s, 1s, and 2s,
    then overwriting the list with that many 0s, followed by 1s, and then 2s.

    Parameters:
    ----------
    nums : list[int]
        A list of integers where each element is either 0, 1, or 2.

    Returns:
    -------
    None
        The input list is sorted in-place; no value is returned.

    Example:
    -------
    >>> nums = [2, 0, 2, 1, 1, 0]
    >>> dutch_flag_brute_force(nums)
    >>> print(nums)
    [0, 0, 1, 1, 2, 2]
    """
    count0 = count1 = count2 = 0
    for num in nums:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1
    i = 0
    for _ in range(count0):
        nums[i] = 0
        i += 1
    for _ in range(count1):
        nums[i] = 1
        i += 1

    for _ in range(count2):
        nums[i] = 2
        i += 1


def optimized_dutch_flag(nums: list[int]) -> None:
    """
    Sorts an array containing only 0s, 1s, and 2s using the Dutch National Flag algorithm (Dijkstra's 3-way partitioning).

    This optimized solution runs in a single pass with constant space.

    Parameters
    ----------
    nums : list[int]
        A list of integers where each element is either 0, 1, or 2.

    Returns
    -------
    None
        The list is sorted in-place.

    Example
    -------
    >>> nums = [2, 0, 2, 1, 1, 0]
    >>> dutch_flag_optimized(nums)
    >>> print(nums)
    [0, 0, 1, 1, 2, 2]
    """
    low = 0
    mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[high], nums[mid] = nums[mid], nums[high]
            mid += 1
            high -= 1
