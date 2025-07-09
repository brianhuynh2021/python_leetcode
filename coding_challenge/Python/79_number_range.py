"""
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
"""

# Brute force method


def brute_force_number_range(arr: list[int]):
    n = len(arr)
    result = []
    sub_arr = [arr[0]]
    for j in range(1, n):
        if arr[j] - arr[j - 1] == 1:
            sub_arr.append(arr[j])
        else:
            result.append(sub_arr)
            sub_arr = [arr[j]]
    result.append(sub_arr)    
    return result

def format_range(arrs: list[list[int]])->list[str]:
    number_range = [str(arr[0]) if len(arr) == 1 else f'{arr[0]}->{arr[-1]}' for arr in arrs]
    return number_range

if __name__ == "__main__":
    arr = [0, 1, 2, 6, 7, 9]
    result = brute_force_number_range(arr)
    format_result = format_range(result)
    print(format_result)
