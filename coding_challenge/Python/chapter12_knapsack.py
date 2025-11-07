"""
Chapter 12 — 0/1 Knapsack (DP) implementations.

Style:
- Start with clear APIs.
- Flake8-compliant, type hinted.
- Brute force -> memoization -> tabulation/space-optimized where relevant.

Run this file to see basic sanity tests.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Iterable, List, Sequence, Tuple


# -----------------------------
# 12.1 0/1 Knapsack — Max Value
# -----------------------------

def knapsack_bruteforce(
    weights: Sequence[int],
    values: Sequence[int],
    capacity: int,
) -> int:
    """Exponential brute force: try all take/skip choices.

    Time: O(2^n)
    Space: O(n) recursion depth
    """
    n = len(weights)

    def dfs(i: int, remaining: int) -> int:
        if i == n or remaining <= 0:
            return 0
        best = dfs(i + 1, remaining)
        if weights[i] <= remaining:
            best = max(best, values[i] + dfs(i + 1, remaining - weights[i]))
        return best

    return dfs(0, capacity)


def knapsack_memo(
    weights: Sequence[int],
    values: Sequence[int],
    capacity: int,
) -> int:
    """Top-down DP with memoization on (i, remaining).

    Time: O(n*capacity), Space: O(n*capacity)
    """
    n = len(weights)

    @lru_cache(maxsize=None)
    def dfs(i: int, remaining: int) -> int:
        if i == n or remaining <= 0:
            return 0
        skip = dfs(i + 1, remaining)
        take = 0
        if weights[i] <= remaining:
            take = values[i] + dfs(i + 1, remaining - weights[i])
        return max(skip, take)

    return dfs(0, capacity)


def knapsack_01_max_value(
    weights: Sequence[int],
    values: Sequence[int],
    capacity: int,
) -> int:
    """Bottom-up 1D space-optimized 0/1 knapsack.

    Time: O(n*capacity)
    Space: O(capacity)

    Args:
        weights: item weights
        values: item values
        capacity: knapsack capacity

    Returns:
        Maximum achievable value without exceeding capacity.
    """
    if capacity <= 0 or not weights:
        return 0
    n = len(weights)
    if n != len(values):
        raise ValueError("weights and values must have the same length")

    dp = [0] * (capacity + 1)
    for i in range(n):
        w_i, v_i = weights[i], values[i]
        # iterate downward for 0/1 behavior
        for c in range(capacity, w_i - 1, -1):
            dp[c] = max(dp[c], v_i + dp[c - w_i])
    return dp[capacity]


# ---------------------
# 12.2 Subset Sum (bool)
# ---------------------

def subset_sum_bruteforce(nums: Sequence[int], target: int) -> bool:
    """Try all subsets.

    Time: O(2^n)
    Space: O(n)
    """
    n = len(nums)

    def dfs(i: int, t: int) -> bool:
        if t == 0:
            return True
        if i == n or t < 0:
            return False
        return dfs(i + 1, t) or dfs(i + 1, t - nums[i])

    return dfs(0, target)


def subset_sum(nums: Sequence[int], target: int) -> bool:
    """1D DP for subset sum decision (0/1).

    Time: O(n*target), Space: O(target)
    """
    if target < 0:
        return False
    dp = [False] * (target + 1)
    dp[0] = True
    for x in nums:
        if x < 0:
            # If negatives exist, this simple DP doesn't apply.
            # Could be extended with offset table; we assume non-negative.
            raise ValueError("subset_sum assumes non-negative integers")
        for t in range(target, x - 1, -1):
            dp[t] = dp[t] or dp[t - x]
    return dp[target]


# -------------------------------
# 12.3 Equal Subset Sum Partition
# -------------------------------

def can_partition_equal_subset(nums: Sequence[int]) -> bool:
    """Check if array can be partitioned into two subsets with equal sum.

    Time: O(n*S), Space: O(S), where S = sum(nums)
    """
    s = sum(nums)
    if s % 2 == 1:
        return False
    return subset_sum(nums, s // 2)


# ----------------------------------
# 12.4 Minimum Subset Sum Difference
# ----------------------------------

def min_subset_sum_difference(nums: Sequence[int]) -> int:
    """Minimize |sum(A) - sum(B)| by subset reachability up to S//2.

    Time: O(n*S), Space: O(S)
    """
    s = sum(nums)
    half = s // 2
    dp = [False] * (half + 1)
    dp[0] = True
    for x in nums:
        if x < 0:
            raise ValueError("This implementation assumes non-negative nums")
        for t in range(half, x - 1, -1):
            dp[t] = dp[t] or dp[t - x]
    # Find best achievable t <= half
    for t in range(half, -1, -1):
        if dp[t]:
            return s - 2 * t
    return 0


# ---------------------------
# 12.5 Count of Subset Sum(s)
# ---------------------------

def count_subset_sum(nums: Sequence[int], target: int) -> int:
    """Count number of subsets summing to target (0/1).

    Time: O(n*target), Space: O(target)
    """
    if target < 0:
        return 0
    dp = [0] * (target + 1)
    dp[0] = 1  # empty subset
    for x in nums:
        if x < 0:
            raise ValueError("count_subset_sum assumes non-negative integers")
        for t in range(target, x - 1, -1):
            dp[t] += dp[t - x]
    return dp[target]


# -----------------
# 12.6 Target Sum
# -----------------

def target_sum_ways(nums: Sequence[int], target: int) -> int:
    """LeetCode 494: count ways to assign +/- to reach target.

    Transform to Count Subset Sum:
      P - N = target
      P + N = sum(nums) -> 2P = target + sum(nums)
      P = (target + sum(nums)) / 2 must be integer and >= 0.
    """
    s = sum(nums)
    tot = target + s
    if tot % 2 != 0:
        return 0
    p = tot // 2
    if p < 0:
        return 0
    # Count subsets that sum to p
    return count_subset_sum(nums, p)


# ---------
# Utilities
# ---------

def _assert_equal(actual, expected) -> None:
    if actual != expected:
        raise AssertionError(f"Expected {expected}, got {actual}")


if __name__ == "__main__":
    # 12.1 Knapsack
    _assert_equal(
        knapsack_01_max_value([1, 3, 4, 5], [1, 4, 5, 7], 7), 9
    )
    _assert_equal(
        knapsack_memo([1, 3, 4, 5], [1, 4, 5, 7], 7), 9
    )
    _assert_equal(
        knapsack_bruteforce([1, 3, 4, 5], [1, 4, 5, 7], 7), 9
    )

    # 12.2 Subset Sum
    _assert_equal(subset_sum([1, 2, 3, 7], 6), True)
    _assert_equal(subset_sum([1, 2, 7, 1, 5], 10), True)
    _assert_equal(subset_sum([1, 3, 4, 8], 6), False)

    # 12.3 Equal Partition
    _assert_equal(can_partition_equal_subset([1, 5, 11, 5]), True)
    _assert_equal(can_partition_equal_subset([1, 2, 3, 5]), False)

    # 12.4 Min Subset Diff
    _assert_equal(min_subset_sum_difference([1, 2, 7]), 4)
    _assert_equal(min_subset_sum_difference([1, 2, 3, 9]), 3)

    # 12.5 Count Subset Sum
    _assert_equal(count_subset_sum([1, 2, 3, 3], 6), 3)
    _assert_equal(count_subset_sum([1, 1, 1, 1, 1], 3), 5)

    # 12.6 Target Sum
    _assert_equal(target_sum_ways([1, 1, 1, 1, 1], 3), 5)

    print("All Chapter 12 tests passed.")