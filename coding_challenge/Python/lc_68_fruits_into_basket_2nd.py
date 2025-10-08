"""
🍌 Problem Statement (Simplified):
You are given an array fruits where each element represents a
type of fruit. You have two baskets, and you can only pick one
type of fruit per basket. You need to find the length of the longest
subarray with at most 2 distinct fruits.
"""


def fruit_into_baskets_brute(fruits: list[int]) -> int:
    if not fruits:
        raise ValueError("Fruits must be not empty")
    n = len(fruits)
    max_len = 0
    for i in range(n):
        for j in range(i, n):
            sub_fruits = fruits[i : j + 1]
            num_types = len(set(sub_fruits))
            if num_types <= 2:
                max_len = max(max_len, len(sub_fruits))

    return max_len


print(fruit_into_baskets_brute([1, 2, 1, 2, 3]))


def fruit_into_baskets_optimize(fruits: list[int]) -> int:
    if not fruits:
        raise ValueError("Fruits must be non-empty list")
    n = len(fruits)
    left = 0
    fruit_count = {}
    max_len = 0
    for right in range(1, n):
        fruit = fruits[right]
        fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
        while len(fruit_count) > 2:
            left_fruits = fruits[left]
            fruit_count[left_fruits] -= 1
            if fruit_count[left_fruits] == 0:
                del fruit_count[
                    left_fruits
                ]  # also can you pop method dictionary.pop('key)
            left += 1
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
    return max_len
