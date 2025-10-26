"""
Problem:

Given a list of numbers, return whether any two sums to k. For example, given
[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


# Complexity of brute force O(n^2), Space(n)
def check_target_sum_brute_force(a: list, k: int) -> bool:
    if not a:
        return False
    n = len(a)
    for i in range(n):
        for j in range(i + 1, n):
            if a[i] + a[j] == k:
                return True
    return False


from typing import List


# Complexity is O(n)
def check_target_sum_optimized(a: List[int], k: int) -> bool:
    if not a:
        return False
    seen = set()
    for num in a:
        if (k - num) in seen:
            return True
        else:
            seen.add(num)
    print("seen ==>", seen)

    return False


if __name__ == "__main__":
    print(check_target_sum_brute_force([], 17))
    print(check_target_sum_brute_force([10, 15, 3, 7], 17))
    print(check_target_sum_brute_force([10, 15, 3, 4], 17))
    print(check_target_sum_optimized([], 17))
    print(check_target_sum_optimized([10, 15, 3, 7], 17))
    print(check_target_sum_optimized([10, 15, 3, 4], 17))
