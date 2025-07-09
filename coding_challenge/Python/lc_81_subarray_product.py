'''🧠 Problem Understanding

You’re given:
	•	An array nums[] of positive integers
	•	An integer target

Your task:
Count how many contiguous subarrays have a product of all elements strictly less than the target.
🔍 Example
    Input: nums = [10, 5, 2, 6], k = 100  
    Output: 8  
    Explanation: The 8 subarrays are:
    [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
'''

def sub_arr_product(nums: list[int], target: int):
    if not nums or target <= 1:
        return 0
    n = len(nums)
    count = 0
    for i in range(n):
        product = 1
        for j in range(i,n):
            product *= nums[j]
            if product < target:
                count += 1
            else:
                break
    return count

if __name__=="__main__":
    nums = [10, 5, 2, 6]
    target = 100
    print(sub_arr_product(nums, target))    