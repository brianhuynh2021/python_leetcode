'''
🎯 Đề bài: Two Sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]  # Vì nums[0] + nums[1] == 9
put more advance issues to problem: give a list of it
'''

# Brute force method
def brute_force_two_sum(nums: list[int], target: int):
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
                   result.append([i, j])
                   used_pair.add((i, j))
   return result
                   