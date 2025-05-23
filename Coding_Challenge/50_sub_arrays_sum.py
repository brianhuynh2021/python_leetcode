"""
Title: Count Subarrays with Sum Equals K – Optimized Prefix Sum + HashMap Technique

Description:
This problem asks us to find the number of continuous subarrays whose sum equals a target value k.
Using a brute force method would require O(n²) time, but we can optimize to O(n) using a prefix sum and a hash map to track previously seen sums.
At each step, we check if the current running sum minus k has been seen before — which indicates a valid subarray ending at the current index.
This elegant one-pass solution is efficient and handles both positive and negative numbers.

Tags: #PrefixSum #HashMap #Subarray #SlidingWindow #LeetCode #Array
"""


def subarray_sum(nums: list[int], k: int) -> int:
    """
    Counts the number of continuous subarrays whose sum equals to `k`.

    This function uses a prefix sum and a hash map to optimize the search
    from O(n^2) to O(n) time complexity.

    Parameters:
    ----------
    nums : List[int]
        The list of integers (can include negatives and zero).
    k : int
        The target sum to find in continuous subarrays.

    Returns:
    -------
    int
        The number of continuous subarrays that sum to `k`.

    Example:
    --------
    >>> subarray_sum([1, 2, 3], 3)
    2
    (The subarrays [1,2] and [3] both sum to 3)"""
    check_appear = {0: 1}
    prefix_sum = 0
    count = 0
    for num in nums:
        prefix_sum += num
        if (prefix_sum - k) in check_appear:
            count += check_appear[prefix_sum - k]
        if prefix_sum in check_appear:
            check_appear[prefix_sum] += 1
        else:
            check_appear[prefix_sum] = 1
    return count


if __name__ == "__main__":
    nums = [1, 2, 3, 1, 1]
    k = 3
    result = subarray_sum(nums, k)
    print(f"Subarray to sum of {nums} to k {k} is {result}")
