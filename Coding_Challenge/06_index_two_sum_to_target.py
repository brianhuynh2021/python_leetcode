def two_sum(arr: list, target: int) -> list:
    list_index = []
    for i in range(len(arr)):
        result = target - arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] == result:
                list_index.append((i, j))
    return list_index

arr = [0, 2, 8, 7, 9]
target = 9
result = two_sum(arr, target)
print(result)