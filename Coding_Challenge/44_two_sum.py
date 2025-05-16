'''
❓ First, what is the Two Sum problem?

Can you try to explain what the Two Sum problem is in your own words?

If you’re not sure yet, I’ll guide you:

You are given:
	•	An array of integers: nums
	•	A target value: target

The task is to find two distinct indices i and j such that:

\text{nums}[i] + \text{nums}[j] = \text{target}

Example:
nums = [2, 7, 11, -2, 15], target = 9
# Output: [0, 1]  because nums[0] + nums[1] == 2 + 7 == 9
'''

def two_sum(nums, target):
    result = []
    check_appear = {}
    for i in range(len(nums)):
        find = target - nums[i]
        if find in check_appear:
            result.append([i,check_appear[find]])
        check_appear[nums[i]] = i
            
    return result

if __name__ == '__main__':
    nums = [2, 7, 11, -2, 15]
    target = 9
    print(two_sum(nums, target))
            