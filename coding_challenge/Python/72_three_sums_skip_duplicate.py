from typing import List

def three_sum(nums: List[int])-> List[List[int]]:
    n = len(nums)
    if n < 3:
        return []
    nums.sort()
    triplets = []
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = n - 1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum > 0:
                k -= 1
            elif sum < 0:
                j += 1
            else:
                triplets.append((i, j , k))
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                j += 1
                k -= 1
                    
    return triplets