"""The “Triplet Sum to Zero” problem is a classic one,
often referred to as the 3Sum problem. Here’s the problem statement:
⸻

❓ Problem Statement:

Given an array nums of n integers, return all unique triplets [nums[i], nums[j], nums[k]] such that:
        •	i ≠ j ≠ k
        •	nums[i] + nums[j] + nums[k] == 0

The solution set must not contain duplicate triplets.

⸻

✅ Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
"""


def triplet_sum_brute(nums: list[int], target) -> list:
    n = len(nums)
    if n < 3:
        return []
    unique_triplets = set()
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    trip = tuple(sorted((nums[i], nums[j], nums[k])))
                    unique_triplets.add(trip)
    result = sorted([list(t) for t in unique_triplets])
    return result


nums = [-1, 0, 1, 2, -1, -4]
print(triplet_sum_brute(nums, 0))


def triplet_sum_optimized(nums: list[int], target) -> list:
    n = len(nums)
    if n < 3:
        return []
    seen = set()
    sorted_nums = sorted(nums)
    for i in range(n):
        l = i + 1
        r = n - 1
        while l < r:
            sum = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                seen.add(tuple((sorted_nums[i], sorted_nums[l], sorted_nums[r])))
                l += 1
                r -= 1
    result = sorted([list(t) for t in seen])
    return result
