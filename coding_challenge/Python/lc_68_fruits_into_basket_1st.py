def total_fruits(fruits: list[int]) -> int:
    """
    Given a list of integers representing fruit types on trees in a row,
    return the length of the longest subarray that contains at most 2 types of fruit.
    """
    start = 0
    max_fruits = 0
    check_appear = {}

    for end, fruit in enumerate(fruits):
        check_appear[fruit] = check_appear.get(fruit, 0) + 1

        while len(check_appear) > 2:
            left_fruit = fruits[start]
            check_appear[left_fruit] -= 1
            if check_appear[left_fruit] == 0:
                del check_appear[
                    left_fruit
                ]  # or you can use pop built-in method                                #
            start += 1  # by check_appear.pop('left_fruit')

        max_fruits = max(max_fruits, end - start + 1)

    return max_fruits


if __name__ == "__main__":
    print(total_fruits([1, 2, 1, 2, 3]))  # ✅ Expected: 4
    print(total_fruits([1, 2, 3, 2, 2]))  # ✅ Expected: 4
    print(total_fruits([1, 2, 3, 4, 5]))  # ✅ Expected: 2
    print(total_fruits([1, 1, 1, 1]))  # ✅ Expected: 4
    print(total_fruits([]))  # ✅ Expected: 0
