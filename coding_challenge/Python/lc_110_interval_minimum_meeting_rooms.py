'''
EN: At its core, this problem is about finding the maximum number 
of overlapping intervals at any given point in time. 
The minimum number of rooms required equals this peak overlap.
VN: Về bản chất, bài toán này là tìm số lượng khoảng thời gian chồng 
chéo lớn nhất tại một thời điểm bất kỳ. 
Số lượng phòng tối thiểu cần thiết chính là đỉnh điểm của sự chồng 
chéo này.
Example 1: General Overlap (Ví dụ gốc)
•	Input: intervals = [[0, 30], [5, 10], [15, 20]]
•	Output: 2
•	Explanation: Meeting [5, 10] and [15, 20] 
can share the same room, but they both overlap with [0, 30].
'''

def meeting_rooms(intervals: list)->bool:
    n = len(intervals)
    
    for i in range(n):
        for j in range(i + 1, n):
            if intervals[i][0] < intervals[j][1]:
                if intervals[j][0] < intervals[i][1]:
                    return False
                continue
    return True

print(meeting_rooms([[0, 30], [5, 10], [15, 20]]))  # False
print(meeting_rooms([[7, 10], [2, 4]]))             # True
print(meeting_rooms([[8, 9], [9, 10]]))             # True

def meeting_rooms_optimzed(intervals: list)->bool:
    n = len(intervals)
    intervals.sort(key = lambda x: x[0])
    for i in range(1, n):
        if intervals[i][0] < intervals[i-1]:
            return False
    return True
# the complexity is nlogn for sort + n for compare ==> complexity is O