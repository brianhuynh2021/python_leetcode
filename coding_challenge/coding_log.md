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