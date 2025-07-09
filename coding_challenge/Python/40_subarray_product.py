'''
    Problem Statement
    Given an array of positive integers nums and an integer k, 
    return the number of contiguous subarrays where the product of all 
    the elements in the subarray is strictly less than k.

🔍 Example
    Input: nums = [10, 5, 2, 6], k = 100  
    Output: 8  
    Explanation: The 8 subarrays are:
    [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
'''
from typing import List 


def sub_arrays(nums: List[int], k: int)->List[List[int]]:
    n = len(nums)
    sub_arr = []
    for i in range(n):
        product = 1
        j = i
        for j in range(i, n):
            product *= nums[j]
            if product < k:
                sub_arr.append(nums[i:j+1])
            else:
                break
    return sub_arr

if __name__ == '__main__':
    nums = [10, 5, 2, 6]
    print('Sub arrays are: ', sub_arrays(nums, 100))
