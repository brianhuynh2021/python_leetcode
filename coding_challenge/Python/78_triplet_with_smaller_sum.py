# the big O is n^3
def triplet_with_smaller_sum(arr: list[int], target):
    n = len(arr)
    if n < 3:
        return None
    result = []
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] < target:
                    result.append((arr[i], arr[j], arr[k]))
    return result

# optimzed complexity 
# First we sort it with logn and do it with O(n)
def optimized_triplet_smaller_with_sum(arr: list[int], target):
    n = len(arr)
    if n < 3:
        return None
    # sort it as ascending
    arr.sort()
    result = []
    for i in range(n-2):
        left = i + 1
        right = n - 1
        while left < right:
            if arr[i] + arr[left] + arr[right] < target:
                for k in range(right, left, -1):
                    result.append((arr[i], arr[left], arr[k]))
                left += 1
            else:
                right -= 1
    return result
if __name__=='__main__':
    arr = [1, 2, 3, 4, 5]
    target = 9
    print(triplet_with_smaller_sum(arr, target))