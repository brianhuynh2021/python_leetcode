"""
You’re given:
        •	an array of integers nums
        •	an integer k

👉 You need to find the total number of continuous subarrays whose sum equals k.

Example:
nums = [1, 1, 1]
k = 2
# Output: 2 → subarrays [1,1] at index 0–1 and 1–2

"""


# Complexity is O(n^2)
# Space: O()
def subarray_sum_brute(nums: list[int], k):
    if not nums:
        return []  # or raise ValueError('Nums must not be emtpy')

    n = len(nums)
    result = []
    for start in range(n):
        total = nums[start]
        for end in range(start, n):
            total += nums[end]
            if total == k:
                result.append((start, end))
    return result


print(subarray_sum_brute([1, 2, 3, 4], 6))

from collections import defaultdict


def subarry_sum_optimized(nums: list[int], k: int):
    if not nums:
        return 0

    prefix_count = defaultdict(int)
    prefix_count[0] = 1

    prefix_sum = 0
    count = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        # Find how many times that found prefix_sum -k before
        count += prefix_count[prefix_sum - k]

        # Update current prefix_sum
        prefix_count[prefix_sum] += 1

    return count


from collections import defaultdict


def subarray_sum_optimized(nums, k):
    prefix_sum = 0
    prefix_count = defaultdict(int)

    prefix_count[0] = 1
    count = 0
    for num in nums:
        prefix_sum += num
        count += prefix_count[prefix_sum - k]
        prefix_count[prefix_sum] += 1
    return count
