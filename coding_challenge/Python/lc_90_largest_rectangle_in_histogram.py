"""You’re given a list of bar heights in a histogram (non-negative integers). You must find the area of the largest rectangle that can be formed using consecutive bars.

Example:
Input: heights = [2, 1, 5, 6, 2, 3]
Output: 10
# The rectangle formed by bars [5,6] has area = 5 * 2 = 10
"""

class Solution:
    def largest_rectangle_area(self, heights: list[int]) -> int:
        max_area = 0
        n = len(heights)
        # Outer loop: fix the start index of the rectangle
        for start in range(n):
            min_heigh = heights[start]
            
            # Inner loop: fix the end index of the rectangle
            for end in range(start, n):
                min_heigh = min(min_heigh, heights[end])
                width = end - start + 1
                area = min_heigh * width
                max_area = max(max_area, area)
        return max_area