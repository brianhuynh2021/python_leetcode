"""
    Bài toán / Problem
    Bạn có một danh sách các khoảng thời gian đã được sắp xếp theo start và không overlap.
    You are given a list of non-overlapping intervals sorted by start time.
    ex:
    intervals = [[1, 3], [6, 9]]
    new_interval = [2, 5]
"""


def insert_interval_brute_force(intervals: list, new_interval: list) -> list:
    intervals = intervals + [new_interval]
    intervals = sorted(intervals, key=lambda x: x[0])
    result = []
    
    for current in intervals:
        if not result or result[-1][1] < current[0]:
            result.append(current)
        else:
            result[-1][1] = max(result[-1][1], current[1])
    return result

def insert_interval_optimized(intervals: list, new_interval) -> list:
    result = []
    i = 0
    n = len(intervals)
    
    # 1. Add intervals before new_interval
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    
    # merge overlap intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)
    
    while i < n:
        result.append(intervals[i])
        i+= 1
        
    return result