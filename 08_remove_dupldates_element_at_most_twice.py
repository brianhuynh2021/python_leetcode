from typing import List

def remove_dulicate(nums: List[int])-> int:
    if len(nums) <= 2:
        return len(nums)
    
    i = 2
    for j in range(2, len(nums)):
        if nums[j] != nums[i-2]:
            nums[i] = nums[j]
            i += 1
    return i    

# def removeDuplicates(self, nums: List[int]) -> int:
#         if len(nums) <= 2:
#             return len(nums)
        
#         # Start from the third position as the first two are always allowed
#         i = 2
#         for j in range(2, len(nums)):
#             # Check if the current element is the same as the element two positions back
#             if nums[j] != nums[i-2]:
#                 nums[i] = nums[j]
#                 i += 1  # Move the 'tail' of the new list forward

#         return i