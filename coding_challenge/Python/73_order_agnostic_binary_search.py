from typing import List


def order_agnostic_binary_search(arr: List[int], target: int)->bool:
    if not arr:
        return False
    if arr[0] == arr[-1]:
        return target == arr[0]
    n = len(arr)
    is_ascending = arr[0] < arr[-1]
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return True
        if is_ascending:
            if arr[mid] > target:
               high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] < target:
                high = mid - 1
            else:
                low = mid + 1
    return False

if __name__=='__main__':
    print(order_agnostic_binary_search([1, 3, 5, 7, 9], 7))     # True
    print(order_agnostic_binary_search([9, 7, 5, 3, 1], 7))     # True
    print(order_agnostic_binary_search([], 1))                  # False
    print(order_agnostic_binary_search([42], 42))              # True
    print(order_agnostic_binary_search([5, 3, 1], 0))           # False