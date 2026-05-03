"""
Bài toán / Problem
Bạn có một danh sách các khoảng thời gian đã được sắp xếp theo start và không overlap.
You are given a list of non-overlapping intervals sorted by start time.
ex:
intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
"""


def insert_interval(intervals: list, new_interval: list) -> list:
    intervals = intervals + [new_interval]
    intervals = sorted(intervals, key=lambda x: x[0])
    result = []
    
    for current in intervals:
        if not result or result[-1][1] < current[0]:
            result.append(current)
        else:
            result[-1][1] = max(result[-1][1], current[1])
    return result