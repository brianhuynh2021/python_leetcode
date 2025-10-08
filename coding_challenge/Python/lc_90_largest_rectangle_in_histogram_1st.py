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
            min_height = heights[start]

            # Inner loop: fix the end index of the rectangle
            for end in range(start, n):
                min_height = min(min_height, heights[end])
                width = end - start + 1
                area = min_height * width
                max_area = max(max_area, area)
        return max_area

    def largest_rectangle_area_optimized(self, heights: list[int]) -> int:
        if not heights:
            raise ValueError("The heights bar must not be empty")
        heights.append(0)
        max_area = 0
        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                top_index = stack.pop()
                height = heights[top_index]
                width = i - stack[-1] - 1 if stack else i
                area = height * width
                max_area = max(max_area, area)
            stack.append(i)
        return max_area
