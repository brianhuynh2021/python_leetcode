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

def insertion_sort(arr: list)-> list:
    for i in range(1, len(arr)):
        compare_element = arr[i]
        j = i
        while j > 0 and compare_element < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = compare_element
    return arr

def triplet_sum(arr: list)-> list:
    result = []
    # Sort the arr
    print("sorted number is: ",insertion_sort(arr))
    n = len(arr)
    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        target_sum = -arr[i]
        j = i+1
        k = n - 1
        
        while j<k:
            num_1 = arr[j]
            num_2 = arr[k]
            if num_1 + num_2 < target_sum:
                j+=1
            elif num_1 + num_2 > target_sum:
                k-=1
            else:
                result.append([arr[i], arr[j], arr[k]])
                j+=1
                k-=1
                      
    return result
    

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    print('Original nums: ', nums)
    # print("Sorted nums: ", insertion_sort(nums.copy()))
    print('Triplet sum is: ', triplet_sum(nums))