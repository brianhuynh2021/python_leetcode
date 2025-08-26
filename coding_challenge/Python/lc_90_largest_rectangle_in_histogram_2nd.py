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
    
    def largest_rectangle_histogram_optimized(self, heights: list[int]) -> int:
        if not heights:
            raise ValueError("Heights must not be empty")

        heights.append(0)
        stack = []
        max_area = 0
        for i, h in enumerate(heights):
            # pop until the stack is increasing
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                height = heights[top]
                # if stack is empty -> width = i
                width = i if not stack else i - stack[-1] - 1
                area = height * width
                max_area = max(max_area, area)
            stack.append(i)
        return max_area

def largest_rectangle_histogram(heights: list[int]):
    heights.append(0)
    stack = [] # This stack save those index of bars greater than them
    max_area = 0
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            top_index = stack.pop() # Determine this is the indexcố định height
            height = heights[top_index] # get the height
            width = i if not stack else i - stack[-1] - 1#i - stack[-1] - 1 là để trừ đi 2 cột chắn (biên trái và phải)
            area = height * width
            max_area = max(max_area, area)
        stack.append(i)
    return max_area

heights = [2, 4, 3]
print(largest_rectangle_histogram(heights))
