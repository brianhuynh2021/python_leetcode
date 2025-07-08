from typing import List

def triplet_sum_smaller(nums: List[int], target: int)->int:
    n = len(nums)
    count = 0
    nums = sorted(nums) # Keep original nums outside of the function
    print('Sorted nums: ', nums)
    for i in range(n-2):
        left = i + 1
        right = n-1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum < target:
                count += right - left
                left += 1
            else:
                right -= 1
    return count

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print('Original nums: ', nums)
    print('Triplet smaller is: ', triplet_sum_smaller(nums, 5))
                    