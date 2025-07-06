"""
You’re given a list of integers and a target number.
You need to pick 3 numbers from the list such that their sum is
as close as possible to the target.
Input: nums = [-2, 0, 1, 2], target = 2
Sorted: [-2, 0, 1, 2]

 Triplet  | Sum
-2 + 0 + 1| -1
-2 + 0 + 2| 0
-2 + 1 + 2| 1
 0 + 1 + 2| 3

We want to find the sum closest to 2.
        •  -1 is 3 units away
        •	0 is 2 units away
        •	1 is 1 unit away
        •	3 is also 1 unit away

So the best answers are 1 or 3, but in most problems like this, you’re asked to return the sum, not the triplet.
If there’s a tie, we can return any closest one.
Output: 1  or  3
"""


def insertion_sort(arr: list) -> list:
    n = len(arr)
    for i in range(1, n):
        compare_element = arr[i]
        j = i
        while j > 0 and compare_element < arr[j - 1]:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = compare_element
    return arr


def tripplet_to_closest(nums: list, target: int):
    n = len(nums)
    closest_sum = float("inf")
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return target
    return closest_sum


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print("Original nums: ", nums)
    sorted_nums = insertion_sort(nums.copy())
    print("Sorted nums: ", sorted_nums)
    print("Triplet closest: ", tripplet_to_closest(sorted_nums, 2))
