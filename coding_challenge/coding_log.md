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
    - Brute force O(n): Due to we iterate for loop until we find the item match the condition arr[i-1] < arr[i] > arr[i+1] we can get the target
    - Optimized O(logn): using binary search
        . check nums[i] < nums[i+1] ==> surely the peak is on right side ==> drop all left side
        . high index = mid
    🧪 Test:
🗣️ Action:

📅 Date: 2025-07-21 (Thursday)
✅ Problem: Search targte in 2D array
🧠 Idea: 
    - Brute force O(n^2): 2 for loops, for row in range(len(matrix)) - for val in row if item == target
    - Optimized O(logn): We treat 2D with 1D array due to all end elemetn of each rows will lower than next row's element
        . rows = len(matrix)
        . colums = len(matrix[0]) # len of an element in matrix
        . len of matrix is: rows*colums
        . use binary search: get the mid position -> convert it into matrix position by get
          row = mid//cols, col = mid%cols ==> get mid_val and compare to target
    🧪 Test:
🗣️ Action: 