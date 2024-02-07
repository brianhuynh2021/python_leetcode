# def remove_duplicate(nums):

#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         return len(set(nums))
def remove_duplicate(nums):
    if not nums:
                return 0
    position = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[position]:
            position += 1
            nums[position] = nums[i]
    print(nums)
    return position + 1
result = remove_duplicate([0, 0, 1, 1, 1, 2, 3, 3, 4])
print(result)