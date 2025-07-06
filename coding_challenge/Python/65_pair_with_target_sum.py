# 🎯 Problem: Pair With Target Sum

# 📝 Mô tả đề bài | Problem Description (Song ngữ)

# Given an array of integers arr and a target number target,
# return a pair of numbers from the array that adds up to the target.

# Cho một mảng các số nguyên arr và một số nguyên target,
# hãy trả về một cặp số trong mảng có tổng bằng đúng target.

# ⸻

# 📥 Input:
# 	•	An array of integers: arr = [int, int, int, ...]
# 	•	A target integer: target = int

# 📤 Output:
# 	•	A pair (a, b) such that a + b == target
# 	•	Or None if no such pair exists

# ⸻

# 💡 How to Think (Gợi ý tư duy)

# ❓ Suppose you’re looking at one number x in the array.
# What number do you need to find next so that x + y == target?

# ❓ Giả sử em đang xét một số x trong mảng,
# thì số còn lại cần tìm y sẽ phải là bao nhiêu để x + y = target?

# → The other number must be y = target - x.

# ⸻

# 🧠 Optimization Idea | Ý tưởng tối ưu

# To avoid checking all possible pairs (O(n²)), we use a hash set to track the numbers we’ve seen:

# Để không phải kiểm tra mọi cặp (O(n²)), ta dùng tập hợp (set) để lưu lại các số đã đi qua.
# ⸻
# ✅ Python Code – MIT/Google Style

# # def find_pair_with_target_sum(arr, target):
# #     seen = set()  # Track numbers we've already seen

# #     for num in arr:
# #         complement = target - num  # Needed number to make the pair
# #         if complement in seen:
# #             return (complement, num)  # Found the valid pair
# #         seen.add(num)  # Save current number for future checking

# #     return None  # No pair found
# ⸻
# 🧪 Test Examples | Ví dụ kiểm thử

# print(find_pair_with_target_sum([3, 5, 1, 7], 8))     # Output: (5, 3) or (1, 7)
# print(find_pair_with_target_sum([1, 2, 3, 4], 10))    # Output: None
# ⸻
# ⏱️ Complexity
# 	•	Time: O(n) – Only one pass through the array
# 	•	Space: O(n) – Set may grow up to n elements

def pairs_with_target(arr: list[int], target):
    seen = set()
    for item in arr:
        completion = target - item
        if completion in seen:
            return (completion, item)
        else:
            seen.add(item)
    return None

if __name__=='__main__':
    result = pairs_with_target([3, 5, 1, 7], 8)
    print(result)