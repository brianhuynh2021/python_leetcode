📅 Date: 2025-07-17 (Thursday)
✅ Problem: Longest Substring with K Distinct Characters
🧠 Idea: 
    - Brute force O(n³): 2 vòng for tạo substring + đếm số lượng ký tự distinct bằng dict/set
    - Optimized O(n): sliding window + dict tần suất, shrink khi len(dict) > k, update max_len nếu right - left + 1 lớn hơn cũ
    🧪 Test:
    - s = "eceba", k = 2 → "ece"
    - s = "aa", k = 1 → "aa"
🗣️ Action: 15h42 – tự nói lớn + tự viết lại code hoàn chỉnh không nhìn lại

📅 Date: 2025-07-17 (Thursday)
✅ Problem: Peak element in mountain array
🧠 Idea: 
    - Brute force O(n): Due to we iterate for loop until we find the item match the condition arr[i-1] < arr[i] > arr[i+1]
    - Optimized O(logn): using binary search
    🧪 Test:
    - s = "eceba", k = 2 → "ece"
    - s = "aa", k = 1 → "aa"
🗣️ Action: 