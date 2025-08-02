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

📅 Date: 2025-07-21 (Mondy)
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

📅 Date: 2025-07-21 (Monday)
✅ Problem: Parentheses valid
🧠 Idea: 
    - Optimized O(logn): We apply stack LIFO, we initialize mapping of characters mapping = {')': '(', '}': '{', ']': '['}.
    - Use for loop checking each item (if is is first open brackets: '({[' put them in stack)
    - if not those open brackets, we have to check with current stack (if current stack is empty==> return False)
      . if current stack is not empty for now
      . top of stack: top = stack.pop()
      . if mapping[c] != top return False
    return not stack

🗓️ Date: 2025-07-23 (Monday)
✅ Problem: Parentheses valid
🧠 Idea/Notes: [] emty list would return False ==> return not []==> True
example: stack = [1, 5, 4, 2] pop out a item
         item_pop = stack.pop() ==> return 2

🗓️ Date: 2025-07-23 (Monday)
✅ Problem: Reverse linked list
🧠 Idea/Notes: 
   🙇 brute force approach:
       . Take all nodes into a list 
       . Iterate the list from end to begin to get new linked list
       . Return nodes[-1] (final item of list)
    🤔 optimize approach
       . use 2 pointers: prev = None, curr = head.
       . Loop all nodes and point to prev until curr is None
       . While curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
       . return prev

🗓️ Date: 2025-07-23 (Monday)
✅ Problem: Reverse linked list
🧠 Idea/Notes: 
   🙇 brute force approach:
       . Take all nodes into a list 
       . Iterate the list from end to begin to get new linked list
       . Return nodes[-1] (final item of list)
    🤔 optimize approach
       . use 2 pointers: prev = None, curr = head.
       . Loop all nodes and point to prev until curr is None
       . While curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
       . return prev

🗓️ Date: 2025-07-24 (Thurs)
✅ Problem: Min Stack (Design Stack with getMin in O(1))
🧠 Idea/Notes:

   🙇 brute force approach:
       . Use one list as stack
       . getMin() = call min(stack) every time
       . This is O(n), since min() must scan the list
       . ❌ not acceptable for FAANG interview

   🤔 optimize approach:
       . Use 2 stacks: stack and min_stack
       . push(x):
           - stack.append(x)
           - min_stack.append(min(x, min_stack[-1])) if min_stack else min_stack.append(x)
       . pop():
           - stack.pop(), min_stack.pop()
       . top():
           - return stack[-1]
       . getMin():
           - return min_stack[-1]
       . ✅ All operations run in O(1)

🧪 Sample dry run:

    push(5)     stack: [5]        min_stack: [5]
    push(2)     stack: [5, 2]     min_stack: [5, 2]
    push(4)     stack: [5, 2, 4]  min_stack: [5, 2, 2]
    push(1)     stack: [5, 2, 4, 1] min_stack: [5, 2, 2, 1]
    pop()       stack: [5, 2, 4]  min_stack: [5, 2, 2]

🎯 Key insight:
   - min_stack mirrors stack and caches "minimum so far"
   - getMin() just peeks min_stack[-1] → O(1)
   - This uses extra O(n) space but achieves constant time min retrieval

🗓️ Date: 2025-07-25 (Friday)
✅ Problem: Redoing this Min Stack (Design Stack with getMin in O(1))
🧠 Idea/Notes: using 2 pointers get the min_stack so later only O(1)

🗓️ Date: 2025-07-25 (Friday)
✅ Problem: Daily temperatures
🧠 Idea/Notes: 
    ⛓️‍💥 Brute force: loop through all days, then compare the following day(s)'s temperature greater than the current day. Put it in waits [] result if not move to next day until it get the temperature greater than current day.
        waits = []
        if temperature[day[j]] > temperature[current[day]]:
            wait.append(j-i)
            break
        j+= 1
    . Out of the loop not found any greater than put it as 0
    ⛓️‍💥 Optimize: 
    . Use stack 

🗓️ Date: 2025-07-25 (Friday)
✅ Problem: Fruits into basket
🧠 Idea/Notes: 
    ⛓️‍💥 Brute force: O(n^2)
    . Get all sub_array by 2 for loop, each sub_array we get len(set(sub_array)). 
        .If len(sub_array)<=2:
            update max_len of sub_array compare with last sub_array
    . Out of the loop return max_len
    ⛓️‍💥 Optimize:

🗓️ Date: 2025-07-27 (Sunday)
✅ Problem: Daily temperatures
🧠 Idea/Notes: 
    ⛓️‍💥 Optimize: 
    . Use stack:
    We use a stack to keep track of the days that haven’t found a warmer day yet.
    When we reach day i, we check whether the current temperature is warmer than the temperatures of the previous days stored in the stack.

    If it is, then we know that those previous days have finally found a warmer day — which is today.

    We pop that previous day off the stack (let’s call it prev_day), and we calculate:
        waits[prev_day] = i - prev_day
    This gives the number of days it took to find a warmer temperature.

    ❗ If we accidentally write:
        waits[prev_day] = i - stack[-1]
    then we’re using the next day in the stack, not the one we just popped.
    That’s a logic error — and I understand now why that was wrong.

🗓️ 2025-07-27
✅ Problem: Evaluate Reverse Polish Notation
🧠 Idea: Use a stack to evaluate expressions where operators come after operands (postfix/RPN).
    💻 Edge Cases:
        1. If tokens has only 1 element:
            - If it is a valid integer (check via lstrip("-").isdigit()), return that value.
            - Else, raise ValueError ("Invalid RPN: not enough operands").
        2. If tokens is empty ([]), raise ValueError ("Invalid RPN: empty input").

    💻 Main Loop:
        - For each token `c` in tokens:
            - If `c` is an operator ("+", "-", "*", "/"):
                - Pop two values from the stack: `b`, then `a`
                - Compute `a op b` with correct order
                - Push the result back onto the stack
            - Else:
                - Convert `c` to int and push to the stack

    💻 Final Step:
        - After the loop, return stack[0] as the result
🗓️ 2025-07-30
✅ Problem: Group Anagrams
🧠 Idea: 
    🙇 Brute-force approach:
   - Duyệt từng từ `i` trong danh sách
   - Với mỗi `i`, so sánh với các từ `j > i`
   - Dùng `sorted()` để kiểm tra xem `word[j]` có phải hoán vị của `word[i]`
   - Dùng `dict` (check_appear) để tránh xét lại cùng nhóm
   - Độ phức tạp: **O(N² × K log K)**

🤔 Optimized approach:
   - Tạo `group_map = {}` dùng `dict` (hoặc `defaultdict`)
   - Với mỗi từ:
       - Tạo `key = ''.join(sorted(word))`
       - Nếu key chưa có trong dict, khởi tạo list mới
       - Append từ đó vào `group_map[key]`
   - Trả về list của tất cả các value trong group_map
   - Độ phức tạp: **O(N × K log K)**
   🔧 Pseudo-code (optimized):
    ```text
    Function group_anagrams(words: List of strings) → List of List of strings

    1. if words is empty:
            return []
    2. Initialize group_map = empty map
    3. For each word in words:
            key = sorted(word)
            if not key in group_map:
                group_map[key] = []
            Append word to group_map[key]
    4. Return group_map.values() as list of lists
🧪 Complexity:
	•	Time: O(N × K log K)
	•	Space: O(N × K)

💡 Insight:
	•	Dùng sorted(word) để làm key thống nhất giữa các từ hoán vị
	•	Không cần so sánh từng cặp, chỉ gom theo key

🗓️ 2025-08-01 (Friday)
✅ Problem: Largest histogram
🧠 Idea: 
   🙇 Brute-force approach:
    e use two nested loops to check every pair of indices `(start, end)`.  
    For each range, we track the minimum height from `start` to `end`, and compute the rectangle area.  
    If the area is greater than the current maximum, we update `max_area`.  
    Finally, return the largest area found.

    📋 Steps:

        1. Initialize `max_area = 0`

        2. Outer loop:
            - For each `start` in `range(len(heights))`:
                - Initialize `min_height = heights[start]`
                - Inner loop:
                    - For each `end` in `range(start, len(heights))`:
                        - Update `min_height = min(min_height, heights[end])`
                        - Compute `width = end - start + 1`
                        - Compute `area = min_height * width`
                        - Update `max_area = max(max_area, area)`

        3. Return `max_area`

    🙇 Optimized approach:
    - Treat histogram as a window where each bar tries to **extend left/right** until blocked.
    - Use a **monotonic increasing stack** to store indices.
    - For each bar at index `i` with height `h`:
        1. If `h >= heights[stack[-1]]`: push `i` (bar can still grow).
        2. Else: pop from stack until top is lower than `h`, and for each popped:
            - `height = heights[popped_index]`
            - `width = i - stack[-1] - 1` (or `i` if stack is empty)
            - `area = height * width` → update `max_area`

    ### ⚙️ Steps:
    - Append sentinel `0` to `heights` to force final area computation.
    - Traverse all indices `i`, maintaining stack of increasing heights.
    - Push `i` only **after popping all taller bars**.
    - Return `max_area`.

    ### 🧱 Key Insight:
    - **Each pop** computes the max area for a bar **right before it gets blocked**.
    - Stack keeps track of all bars that are still "open to grow".

    ### 🧠 Tiny Habit:
    > ❝ Don’t push `i` until you’ve popped all taller bars.  
    > The right boundary (`i`) defines the end of extension for shorter bars. ❞