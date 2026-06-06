"""Employee Free Time — MIT Style

Thời gian rảnh chung của nhân viên

Bài này rất giống Meeting Rooms, nhưng câu hỏi bị đảo ngược.

⸻

1. Problem

Mỗi nhân viên có lịch bận riêng:
    schedule = [
    [[1, 2], [5, 6]],   # Employee 1
    [[1, 3]],           # Employee 2
    [[4, 10]]           # Employee 3
]
Ta cần tìm:
Khoảng thời gian mà tất cả nhân viên đều rảnh
[[3, 4]]
"""

class Solution:
    def employee_free_time(self, schedule: list) -> list:
        # Step 1: get employee_time
        employee_time = []
        for employee in schedule:
            for value in employee:
                employee_time.append(value)
        # Step 2: get employee_busy_time
        changed = True
        while changed:
            changed = False
            n = len(employee_time)
            for i in range(n):
                if changed:
                    break
                for j in range(i + 1, n):
                    start_1 = employee_time[i][0]
                    end_1 = employee_time[i][1]
                    
                    start_2 = employee_time[j][0]
                    end_2 = employee_time[j][1]
                    
                    if start_1 <= end_2 and start_2 <= end_1:
                        print("overlap")
                        new_start = min(start_1, start_2)
                        new_end = max(end_1, end_2)
                        new_interval = [new_start, new_end]
                        employee_time[i] = new_interval
                        employee_time.pop(j)
                        changed = True
                        break
        busy_time = sorted(employee_time, key=lambda x: x[0])
        free_time = []
        for i in range(1, len(busy_time)):
            prev_end = busy_time[i-1][1]
            curr_start = busy_time[i][0]
            
            if prev_end < curr_start:
                free_time.append([prev_end, curr_start])
        return free_time
    
solution = Solution()
schedule = [
    [[1, 3], [6, 7]],

    [[2, 4]],

    [[2, 5], [9, 12]]
]

print(solution.employee_free_time(schedule))