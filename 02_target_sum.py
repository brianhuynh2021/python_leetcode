"""
Problem:

Given a list of numbers, return whether any two sums to k. For example, given
[10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
from typing import List


def check_target_sum(arr: List[int], target: int) -> bool:
    '''find couple that sums to target'''
    seen = set()
    for item in arr:
        if target - item in seen:
            return True
        seen.add(item)
    return False

if __name__ == '__main__':
    print(check_target_sum([], 17))
    print(check_target_sum([10, 15, 3, 7], 17))
    print(check_target_sum([10, 15, 3, 4], 17))
