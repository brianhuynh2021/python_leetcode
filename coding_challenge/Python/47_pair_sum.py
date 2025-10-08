def pair_sum_02(arr: list, target: int) -> bool:
    seen = {}
    for item in arr:
        if (target - item) in seen:
            return True
        seen[item] = True
    return False


print(pair_sum([1, 5, 7, 2, 9, 15], 9))
