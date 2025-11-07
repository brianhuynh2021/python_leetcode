"""
Chapter 21: Bit Manipulation — Implementations
"""

from typing import List


# 1) Single Number
def single_number(nums: List[int]) -> int:
    res = 0
    for n in nums:
        res ^= n
    return res


# 2) Single Number II
def single_number_ii(nums: List[int]) -> int:
    ones = twos = 0
    for n in nums:
        ones = (ones ^ n) & ~twos
        twos = (twos ^ n) & ~ones
    return ones


# 3) Missing Number
def missing_number(nums: List[int]) -> int:
    res = len(nums)
    for i, n in enumerate(nums):
        res ^= i ^ n
    return res


# 4) Reverse Bits
def reverse_bits(n: int) -> int:
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res


# 5) Counting Bits
def count_bits(n: int) -> List[int]:
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)
    return bits


# 6) Sum of Two Integers
def get_sum(a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    while b != 0:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)


if __name__ == "__main__":
    assert single_number([2, 2, 1]) == 1
    assert single_number_ii([2, 2, 3, 2]) == 3
    assert missing_number([3, 0, 1]) == 2
    assert reverse_bits(43261596) == 964176192
    assert count_bits(5) == [0, 1, 1, 2, 1, 2]
    assert get_sum(-2, 3) == 1
    print("All Chapter 21 tests passed.")