'''
🎯 Đề bài: Two Sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]  # Vì nums[0] + nums[1] == 9
put more advance issues to problem: give a list of it
'''

# Brute force method
def brute_force_two_sum(nums: list[int], target: int)->list[tuple]:
   n = len(nums)
   if n < 2:
       return []
   result = []
   used_pair = set()
   for i in range(n-1):
       for j in range(i+1, n):
           a, b = nums[i], nums[j]
           if a + b == target:
               pair = tuple(sorted((a,b)))
               if pair not in used_pair:
                   result.append((i, j))
                   used_pair.add(pair)
   return result

def optimized_two_sum(nums: list[int], target: int)->list[tuple]:
    n = len(nums)
    if n < 2:
        return []
    result = []
    check_appear = {}
    used_pair = set()
    for i, num in enumerate(nums):
        find = target - nums[i]
        if find in check_appear:
            pair = tuple(sorted((num, find)))
            if pair not in check_appear:
                result.append((check_appear[find], i))
                used_pair.add(pair)
        check_appear[num] = i
        
    return result

def main():
    print("Test 1:")
    nums = [2, 3, 3, 4, 5]
    target = 6
    print(f"Input: {nums}, target = {target}")
    print("Output:", optimized_two_sum(nums, target))
    print("---")

    print("Test 2: (no valid pair)")
    nums = [1, 2, 3]
    target = 10
    print(f"Input: {nums}, target = {target}")
    print("Output:", optimized_two_sum(nums, target))
    print("---")

    print("Test 3: (multiple duplicate values)")
    nums = [3, 3, 3]
    target = 6
    print(f"Input: {nums}, target = {target}")
    print("Output:", optimized_two_sum(nums, target))
    print("---")

    print("Test 4: (empty list)")
    nums = []
    target = 5
    print(f"Input: {nums}, target = {target}")
    print("Output:", optimized_two_sum(nums, target))
    print("---")

    print("Test 5: (single element)")
    nums = [10]
    target = 10
    print(f"Input: {nums}, target = {target}")
    print("Output:", optimized_two_sum(nums, target))


if __name__ == "__main__":
    main()