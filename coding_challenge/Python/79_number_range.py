'''
    🚩 Bài toán: “Number Range” (aka “Summary Ranges”)

    🧠 Đề bài:

    Cho một mảng đã được sắp xếp tăng dần, chứa các số nguyên không trùng nhau, bạn cần gom các số liên tiếp thành đoạn, với định dạng:
        •	"start->end" nếu đoạn có nhiều số liên tiếp
        •	"n" nếu chỉ có 1 số lẻ loi

    ⸻

    🔎 Ví dụ:
        Input:  [0, 1, 2, 6, 7, 9]
        Output: ["0->2", "6->7", "9"]
    Giải thích:
	•	[0,1,2] là dãy liên tiếp → "0->2"
	•	[6,7] → "6->7"
	•	[9] → "9"
'''

# Brute force method

def brute_force_number_range(arr: list[int]):
    n = len(arr)
    i = 0
    for i in range(n-1):
        result = [arr[i]]
        j = i + 1
        while i < j:
            if arr[j] - arr[i] == 1:
                
                result.append(arr[j])
            else:
                i
                
