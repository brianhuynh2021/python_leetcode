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

def triplet_sum_closest_target(nums: list[int], target: int)->list:
    n = len(nums)
    if n < 3:
        return []
    nums.sort()
    closest_sum = float('inf')
    for i in range(n-2):
        j = i + 1
        k = n -1
        while j < k:
            current_sum = nums[i] + nums[j] + nums[k]
            if abs(current_sum-target) < abs(closest_sum-target):
                closest_sum = current_sum
            
    result = []
    return result