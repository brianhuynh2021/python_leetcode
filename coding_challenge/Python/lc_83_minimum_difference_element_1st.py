"""🚀  Phân tích đề (Problem Analysis)

Giả sử đề như sau (rất phổ biến trong Leetcode):

Cho một mảng số nguyên đã được sắp xếp tăng dần arr và một số nguyên key, hãy tìm phần tử trong arr có giá trị gần nhất với key nhất. Nếu có hai phần tử có cùng hiệu tuyệt đối, trả về phần tử nhỏ hơn.
arr = [1, 3, 8, 10, 15], key = 12 → Output: 10
arr = [4, 6, 10], key = 7         → Output: 6
arr = [4, 6, 10], key = 17        → Output: 10

"""


def brute_force_find_min_diff_element(nums: list[int], target: int) -> int:
    """
    Find the element with the minimum absolute difference to the target.
    If multiple elements have the same difference, return the smaller one.

    Args:
        nums (List[int]): Sorted list of integers
        target (int): Target value to compare

    Returns:
        int: Element with minimum difference to the target
    """
    min_diff = float("inf")
    closest = nums[0]

    for num in nums:
        diff = abs(num - target)
        if diff < min_diff or (diff == min_diff and num < closest):
            min_diff = diff
            closest = num

    return closest


def test_brute_force_find_min_diff_element():
    assert brute_force_find_min_diff_element([4, 6, 10], 7) == 6
    assert brute_force_find_min_diff_element([1, 3, 8, 10, 15], 12) == 10
    assert brute_force_find_min_diff_element([1, 2, 3, 5], 4) == 3
    print("All test cases passed!")


test_brute_force_find_min_diff_element()

print("Test 1:", brute_force_find_min_diff_element([4, 6, 10], 7))  # 6
print("Test 2:", brute_force_find_min_diff_element([1, 3, 8, 10, 15], 12))  # 10
print("Test 3:", brute_force_find_min_diff_element([1, 2, 3, 5], 4))  # 3
print("Test 4:", brute_force_find_min_diff_element([1], 100))  # 1


def optimized_find_diff_element(nums: list[int], target) -> int:
    """
    Binary Search to find element with minimum difference to target
    Args:
        nums (List[int]): Sorted list
        target (int): Target number

    Returns:
        int: Element closest to target
    """
    low = 0
    high = len(nums) - 1
    closest_el = nums[0]
    closest_diff = abs(nums[0] - target)
    while low <= high:
        mid = (low + high) // 2
        current_diff = abs(nums[mid] - target)
        if current_diff < closest_diff or (
            current_diff == closest_diff and nums[mid] < closest_el
        ):
            closest_diff = current_diff
            closest_el = nums[mid]
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return nums[mid]
    return closest_el
