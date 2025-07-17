📅 Date: 2025-07-17 (Thursday)
✅ Problem: Longest Substring with K Distinct Characters
🧠 Idea: 
    - Brute force O(n³): 2 vòng for tạo substring + đếm số lượng ký tự distinct bằng dict/set
    - Optimized O(n): sliding window + dict tần suất, shrink khi len(dict) > k, update max_len nếu right - left + 1 lớn hơn cũ
    🧪 Test:
    - s = "eceba", k = 2 → "ece"
    - s = "aa", k = 1 → "aa"
🗣️ Action: 15h42 – tự nói lớn + tự viết lại code hoàn chỉnh không nhìn lại