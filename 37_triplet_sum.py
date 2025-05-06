'''The “Triplet Sum to Zero” problem is a classic one, 
often referred to as the 3Sum problem. Here’s the problem statement:
⸻

❓ Problem Statement:

Given an array nums of n integers, return all unique triplets [nums[i], nums[j], nums[k]] such that:
	•	i ≠ j ≠ k
	•	nums[i] + nums[j] + nums[k] == 0

The solution set must not contain duplicate triplets.

⸻

✅ Example:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
'''

def triplet_sum(arr: list)-> list:
    
    
def insertion_sort(arr: list)-> list:
    for i in range(1, len(arr)):
        compare_element = arr[i]
        j = i
        while j > 0 and compare_element < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        compare_element = arr[j]