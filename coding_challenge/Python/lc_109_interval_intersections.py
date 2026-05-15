"""
    Bài toán / Problem
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
"""


from typing import List

class Solution:
    def intervalIntersection(
        self,
        firstList: List[List[int]],
        secondList: List[List[int]]
    ) -> List[List[int]]:
        
        result = []
        i = 0
        j = 0
        
        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]
            
            # Intersection = đoạn bắt đầu muộn hơn và kết thúc sớm hơn
            left = max(a_start, b_start)
            right = min(a_end, b_end)
            
            # Nếu left <= right thì có giao
            if left <= right:
                result.append([left, right])
            
            # Đoạn nào kết thúc trước thì bỏ đoạn đó
            if a_end < b_end:
                i += 1
            else:
                j += 1
        
        return result