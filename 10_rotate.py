class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n  # Ensure k is within the range of the list length
        nums[:] = nums[-k:] + nums[:-k] 
result = Solution()
print(result.rotate([1,2,3,4,5,6,7], 3))