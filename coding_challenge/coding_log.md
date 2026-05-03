📅 Date: 2025-07-17 (Thursday)
✅ Problem: Longest Substring with K Distinct Characters
🧠 Idea:
    - Brute force O(n³): 2 vòng for tạo substring + đếm số lượng ký tự distinct bằng dict/set
    - Optimized O(n): sliding window + dict tần suất, shrink khi len(dict) > k, update max_len nếu right - left + 1 lớn hơn cũ

    🧪 Test:
    - s = "eceba", k = 2 → "ece"
    - s = "aa", k = 1 → "aa"

🗣️ Action: 15h42 – tự nói lớn + tự viết lại code hoàn chỉnh không nhìn lại

---

📅 Date: 2025-07-17 (Thursday)
✅ Problem: Peak element in mountain array
🧠 Idea:
    - Brute force O(n):

    Due to we iterate for loop until we find the item match the condition arr[i-1] < arr[i] > arr[i+1] we can get the target
    - Optimized O(logn): using binary search
        . check nums[i] < nums[i+1] ==> surely the peak is on right side ==> drop all left side
        . high index = mid
---

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

---
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
---
🗓️ Date: 2025-07-23 (Monday)
✅ Problem: Parentheses valid
🧠 Idea/Notes:

[] emty list would return False ==> return not []==> True
example: stack = [1, 5, 4, 2] pop out a item
         item_pop = stack.pop() ==> return 2

---
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

---
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

---
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
---
🗓️ Date: 2025-07-25 (Friday)
✅ Problem: Redoing this Min Stack (Design Stack with getMin in O(1))
🧠 Idea/Notes: using 2 pointers get the min_stack so later only O(1)

---
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

---
🗓️ Date: 2025-07-25 (Friday)
✅ Problem: Fruits into basket
🧠 Idea/Notes:
    ⛓️‍💥 Brute force: O(n^2)
    . Get all sub_array by 2 for loop, each sub_array we get len(set(sub_array)).
        .If len(sub_array)<=2:
            update max_len of sub_array compare with last sub_array
    . Out of the loop return max_len
    ⛓️‍💥 Optimize:

---
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

---
🗓️ 2025-07-27
✅ Problem: Evaluate Reverse Polish Notation
🧠 Idea: Use a stack to evaluate expressions where operators come after operands (postfix/RPN).
    💻 Edge Cases:
        1. If tokens has only 1 element:
            - If it is a valid integer (check via lstrip("-").isdigit()), return that value.
            - Else, raise ValueError ("Invalid RPN: not enough operands").
        2. If tokens is empty ([]), raise ValueError ("Invalid RPN: empty input").

    💻 Main Loop:
        - For each token c in tokens:
            - If c is an operator ("+", "-", "*", "/"):
                - Pop two values from the stack: b, then a
                - Compute a op b with correct order
                - Push the result back onto the stack
            - Else:
                - Convert c to int and push to the stack

    💻 Final Step:
        - After the loop, return stack[0] as the result

---
🗓️ 2025-07-30
✅ Problem: Group Anagrams
🧠 Idea:
    🙇 Brute-force approach:
   - Duyệt từng từ i trong danh sách
   - Với mỗi i, so sánh với các từ j > i
   - Dùng sorted() để kiểm tra xem word[j] có phải hoán vị của word[i]
   - Dùng dict (check_appear) để tránh xét lại cùng nhóm
   - Độ phức tạp: **O(N² × K log K)**

🤔 Optimized approach:
   - Tạo group_map = {} dùng dict (hoặc defaultdict)
   - Với mỗi từ:
       - Tạo key = ''.join(sorted(word))
       - Nếu key chưa có trong dict, khởi tạo list mới
       - Append từ đó vào group_map[key]
   - Trả về list của tất cả các value trong group_map
   - Độ phức tạp: **O(N × K log K)**
   🔧 Pseudo-code (optimized):
    text
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

---
🗓️ 2025-08-01 (Friday)
✅ Problem: Largest histogram
🧠 Idea:
   🙇 Brute-force approach:
    e use two nested loops to check every pair of indices (start, end).
    For each range, we track the minimum height from start to end, and compute the rectangle area.
    If the area is greater than the current maximum, we update max_area.
    Finally, return the largest area found.

    📋 Steps:

        1. Initialize max_area = 0

        2. Outer loop:
            - For each start in range(len(heights)):
                - Initialize min_height = heights[start]
                - Inner loop:
                    - For each end in range(start, len(heights)):
                        - Update min_height = min(min_height, heights[end])
                        - Compute width = end - start + 1
                        - Compute area = min_height * width
                        - Update max_area = max(max_area, area)

        3. Return max_area

    🙇 Optimized approach:
    - Treat histogram as a window where each bar tries to **extend left/right** until blocked.
    - Use a **monotonic increasing stack** to store indices.
    - For each bar at index i with height h:
        1. If h >= heights[stack[-1]]: push i (bar can still grow).
        2. Else: pop from stack until top is lower than h, and for each popped:
            - height = heights[popped_index]
            - width = i - stack[-1] - 1 (or i if stack is empty)
            - area = height * width → update max_area
    - Remember that left block is stack[-1] it always smaller than heights[pop_index] and heights[stack[-1]] > i
    - Pay attention stack[-1] will get twice
    ### ⚙️ Steps:
    - Append sentinel 0 to heights to force final area computation.
    - Traverse all indices i, maintaining stack of increasing heights.
    - Push i only **after popping all taller bars**.
    - Return max_area.

    ### 🧱 Key Insight:
    - **Each pop** computes the max area for a bar **right before it gets blocked**.
    - Stack keeps track of all bars that are still "open to grow".

    ### 🧠 Tiny Habit:
    > ❝ Don’t push i until you’ve popped all taller bars.
    > The right boundary (i) defines the end of extension for shorter bars. ❞

---
🗓️ 2025-08-07 (Thu)
✅ Problem: Next greater element
🧠 Idea:
   🙇 Brute-force approach:

   - We use 2 for loops (i, j) if any value at index j > than value at i ==> Update result at that postion is value of index j

   🙇 Optimized approach:
   - use stack[] to keep index of greater element if there is any element greater than it we pop that index out and sitatimous (dong thoi) update result at that index in value of greater than
---
🗓️ 2025-08-08 (Friday)
✅ Problem: Asteroid collision
🧠 Idea:
   🙇 Brute-force approach:
      We use 2 for loops to do this by checking sequence of (i, j)
      result = [-1]*len(asteroids)
      psudo code:
      hit = True
      while hit:
        hit = False
        for i in len(asteroids)
            a = asteroid[i]
            b = asteroid[i+1]
            if a > 0 and  b < 0:
                if abs(a) > abs(b):
                    del asteroids[i+1]
                if abs(a) < abs(b):
                    del asteroids[i]
                else:
                    del both values
                hit = True
                break
      return result

   🙇 Optimized approach:

      stack = [] # This stack asteroid handle exploded asteroid
      for a in steroids:
        alive = True
        while hit and stack and stack[-1] > 0 and a < 0;
            if stack[-1] < -a:
                stack.pop()
            elif stack[-1] == -a:
                stack.pop()
                alive = False
            else:
                alive = False
        if alive:
            stack.append(a)
    return stack
---
🗓️ 2025-08-16 (Saturday)
✅ Problem: Heap - Top K elements
🧠 Idea:
    🙇 Brute-force approach:

        💡 Sorted all elements in ascending or descending order, then select the top k items.
        📄 Psuedo code:
            1. Import heap functions: from heapq import heappush, heappop
            2. Initialize an empty heap: heap = []
            3. For each element in elements:

            heappush(heap, element)
            If len(heap) > k:

                heappop(heap)
            4. Return heap (contains the top k largest elements)

---
🗓️ 2025-08-16 (Saturday)
✅ Problem: Kth Largest Element
🧠 Idea:
    🙇 Edge cases:
            . k <= 0 → invalid, return [] or raise ValueError.
            . k > len(elements) → cannot get kth element, return [] or raise ValueError.
            . elements is empty → return [] or raise ValueError.
    🙇 Brute-force approach:
        💡 Complexity:
            Big O(nlogn) for sorting elements

        📄 Pseudo code:
            1. Sort all elements in descending order.
            2. Return elements[k-1] because index start 0
    🙇 Brute-force approach:
        💡 Complexity:
            O(nlogk)
        💡 Pseudo code:
            1. Import heap functions: from heap import heappush, heappop
            2.Initialize empty heap: heap = []
            3. for each element in elements:
                If len(heap) > k:
                 heappop(heap)
            4. Return heap[0]

elements)

---
🗓️ 2025-08-16 (Sunday)
✅ Problem: Isomorphic of two strings
   Giving 2 strings, check are they isomorphic
🧠 Idea:
    🙇 Edge cases: if len(s) != len(t) return
    False
    🙇 Brute Force Approach:
      . Complexity: O(n^2)
      . Pseudo code:
        1. For each i in range len(s):
                For each j in range len(i):
                    Check is s at (i, j) != t at (i, j)
                    if not:
                        return False
        2. Return True

---
🗓️ 2025-08-22 (Friday)
✅ Problem: Correct ropes minimum ropes
   Giving list of ropes with multiple length. Giving back minimum sum of all of it each connect is 2 ropes
🧠 Idea:
 💡 Brute force + Recursion:
    Pseudo code:
    For i in range(len(ropes)):
      For each j in range(i+1, len(ropes))
        merge = ropes[i] + ropes[j]
        next_stage = []
        for k in range(n):
            Check k # i and k # j:
                Copy all the rest ropes to new_stage
                new_stage.rope[k]
        new_stage.append(merge)

        now recurve new_stage
        total = merged + def_min_cost_ropes(new_stage)
        if total < best:
            best = total
    return total

    💡 Optimized:
    1. We create new heap base on list of ropes
    2. The pop 2 times to get (2 min_heap)
    3. Compute the merge of 2 min_heap
    4. Compute cost of 2 min_heap
    5. Push cost back to the heap
    6. Do it until get only one item of the heap

---
🗓️ 2025-08-25 (Friday)
✅ Problem: Median of number stream
   Giving list of ropes with multiple length. Giving back minimum sum of all of it each connect is 2 ropes
🧠 Idea:
 💡 Brute force + Recursion:
    Pseudo code:
    For i in range(len(ropes)):
      For each j in range(i+1, len(ropes))
        merge = ropes[i] + ropes[j]
        next_stage = []
        for k in range(n):
            Check k # i and k # j:
                Copy all the rest ropes to new_stage
                new_stage.rope[k]
        new_stage.append(merge)

        now recurve new_stage
        total = merged + def_min_cost_ropes(new_stage)
        if total < best:
            best = total
    return total

    💡 Optimized:
    1. We create new heap base on list of ropes
    2. The pop 2 times to get (2 min_heap)
    3. Compute the merge of 2 min_heap
    4. Compute cost of 2 min_heap
    5. Push cost back to the heap
    6. Do it until get only one item of the heap

---
# 🗓️ 2025-08-31 (Sunday)
## ✅ Problem: Count Subarrays with Sum Equals K

### Description:
**This problem asks us to find the number of continuous subarrays whose sum equals a target value `k`.**
### 🧪 Edge Cases:
    - **Empty input**: `nums = []`, `k = 0` → should return `0`
    - **All elements are zero**: `nums = [0, 0, 0]`, `k = 0` → expect multiple valid subarrays
    - **Negative numbers**: `nums = [1, -1, 2, -2, 3]`, `k = 0` → must still work correctly
    - **Only one element**:
    - `nums = [3]`, `k = 3` → return `1`
    - `nums = [2]`, `k = 3` → return `0`
    - **Large input size**: `nums` has 100,000 items → make sure optimized runs in O(n)
🧠 Idea:
---

 💡 Brute force approach:

    - **Time Complexity:** O(n)
    - **Space Complexity:** O(1)
    ###Steps:
    1. For each `i` in length of `nums`
    2. Initialize `sum = 0`
    3. For each `j` in length of `nums`
        - `sum += nums[j]`
        - `count = 0`
        - `count += 1 if sum == k else count`
    4. return `count`

  💡 **Optimized approach: Prefix Sum + HashMap**

      - **Time Complexity:** O(n)
      - **Space Complexity:** O(n)

    ###Steps:
    1. Initialize:
      - `prefix_sum = 0`
      - `count = 0`
      - `prefix_count = defaultdict(int)`
    2. Set `prefix_count[0] = 1` (handle subarrays starting at index 0)
    3. Loop through each `num` in `nums`:
      - `prefix_sum += num`
      - `count += prefix_count[prefix_sum - k]` (check if previous prefix sum matches)
      - `prefix_count[prefix_sum] += 1`

# 🗓️ 2025-09-06 (Friday)
## ✅ Problem: Sliding Window Max

### Description:
    *Input:
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
    *Output:
        [3, 3, 5, 5, 6, 7]
### Solutions:
    Brute force:
        •	The current window
        •	The maximum of the window
        •	The result so far
    Optimized:
    	•	The index i and nums[i]
        •	The deque content (indices and their values)
        •	What we remove (either because it’s out of window or smaller than current)
        •	What we append to result
---
📅 Date: 2025-12-14 (Sunday)

✅ Problem: Merge Sorted Array (merge nums2 into nums1 in-place)

🧠 Idea:

🙇 Brute force approach #1 (easy):
	•	Copy all valid elements into a new list, then sort
	•	Example:
	•	merged = nums1[:m] + nums2
	•	merged.sort()
	•	copy merged back to nums1
	•	Complexity:
	•	Time: O((m+n) log(m+n))
	•	Space: O(m+n) (because we built merged)

🙇 Brute force approach #2 (standard merge but extra memory):
	•	Use two pointers to merge into a new array result, then copy back to nums1
	•	Complexity:
	•	Time: O(m+n)
	•	Space: O(m+n)

🤔 Optimized approach (FAANG expected):
	•	Key insight: nums1 has buffer at the end, so we fill from the back to avoid shifting
	•	Use 3 pointers:
	•	i = m-1 (last valid in nums1)
	•	j = n-1 (last in nums2)
	•	k = m+n-1 (write position)
	•	While i>=0 and j>=0:
	•	place bigger one into nums1[k], move pointer
	•	After that, only need to copy remaining nums2 (if any)
	•	Complexity:
	•	Time: O(m+n)
	•	Space: O(1)

🧪 Test:
	•	nums1 = [1,2,3,0,0,0], m=3; nums2=[2,5,6], n=3 → [1,2,2,3,5,6]
	•	nums1 = [1], m=1; nums2=[], n=0 → [1]
	•	nums1 = [0], m=0; nums2=[1], n=1 → [1]
	•	nums1 = [4,5,6,0,0,0], m=3; nums2=[1,2,3], n=3 → [1,2,3,4,5,6]
---
🗓️ Date: 2026-05-03 (Sunday)
✅ Problem: Insert Interval
🧠 Idea/Notes:
    🙇 Simple approach: Sorting + merge
        . Add new_interval into intervals
        . Sort intervals by start value
        . Create result = []
        . Loop through each current interval
        . If result is empty OR last interval in result does not overlap with current:
            result.append(current)
        . Else:
            merge them by updating the end:
            result[-1][1] = max(result[-1][1], current[1])
        . Return result

    🤔 Key idea:
        . Since intervals may overlap after adding new_interval, sort first
        . Then merge intervals one by one
        . Two intervals overlap when:
            result[-1][1] >= current[0]

    💻 Code detail:
        . intervals = intervals + [new_interval]
          This creates a new list and does not mutate the original outer list

        . intervals = sorted(intervals, key=lambda x: x[0])
          Sort by start time

    🤔 Optimized approach:
        . Since intervals are already sorted and non-overlapping, we do not need to sort again
        . Add all intervals that end before new_interval starts
        . Merge all intervals that overlap with new_interval
        . Add the merged new_interval into result
        . Add the remaining intervals after new_interval

    🧪 Test:
        intervals = [[1, 3], [6, 9]]
        new_interval = [2, 5]
        output = [[1, 5], [6, 9]]

        intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
        new_interval = [4, 8]
        output = [[1, 2], [3, 10], [12, 16]]

    ⏱️ Complexity:
        . Sorting + merge approach:
            Time: O(n log n) because of sorting
            Space: O(n) for result
        . Optimized approach:
            Time: O(n)
            Space: O(n) for result
---
