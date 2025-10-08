def brute_force_rotated_arr(nums: list[int], k=int) -> bool:
    for num in nums:
        if num == k:
            return True
    return False


def optimized_rotated_arr(nums: list[int], k: int) -> bool:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == k:
            return True

        # Right half is sorted
        if nums[mid] < nums[low]:
            if nums[mid] < k <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

        # Left half is sorted
        else:
            if nums[low] <= k < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return False


print(optimized_rotated_arr([4, 5, 6, 7, 0, 1, 2], 0))  # ✅ True
print(optimized_rotated_arr([4, 5, 6, 7, 0, 1, 2], 3))  # ❌ False
print(optimized_rotated_arr([1, 3], 3))  # ✅ True
print(optimized_rotated_arr([3, 1], 3))  # ✅ True
