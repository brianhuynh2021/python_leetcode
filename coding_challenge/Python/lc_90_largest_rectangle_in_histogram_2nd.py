
class Solution:
    def  largest_rectangle_histogram_brute(self, heights: list[int]) -> int:
        '''
        Given un-negative integers heights of historgram. Find largest area of heigh histogram
        '''
        n = len(heights)
        max_area = 0
        
        for start in range(n):
            min_heigh = heights[start]
            for end in range(start, n):
                min_heigh = min(min_heigh, heights[end])
                width = end - start + 1
                area = min_heigh * width
                max_area = max(max_area, area)
        return max_area