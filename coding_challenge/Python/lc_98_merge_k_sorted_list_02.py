"""
🎯 PROBLEM: Merge K Sorted Lists (LeetCode 23) - MIT/FAANG STYLE ANALYSIS

📋 PROBLEM STATEMENT:
You are given an array of k linked-lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

🧠 CORE CONCEPTS & PATTERNS:

1. **Divide & Conquer**: Break down into smaller subproblems
2. **Merge Two Lists**: Foundation operation (merge 2 sorted lists)
3. **Priority Queue/Min-Heap**: Efficient minimum finding
4. **Pointer Manipulation**: Linked list traversal and reconstruction

🚀 APPROACH PROGRESSION (FAANG Interview Style):

APPROACH 1: Brute Force - Compare All Heads
❌ Time: O(k*N), Space: O(1) where N = total nodes
- Compare all k heads, pick minimum, repeat
- Inefficient: repeatedly scanning k lists

APPROACH 2: Min-Heap (Priority Queue)
✅ Time: O(N*log(k)), Space: O(k)
- Use heap to efficiently find minimum among k heads
- Most intuitive optimal solution

APPROACH 3: Divide & Conquer (Merge Pairs)
✅ Time: O(N*log(k)), Space: O(log(k)) - recursion stack
- Merge lists in pairs: k→k/2→k/4→...→1
- Most elegant and space-efficient

APPROACH 4: Sequential Merging
⚠️ Time: O(k*N), Space: O(1)
- Merge lists one by one: merge(merge(l1,l2),l3)...
- Simple but suboptimal time complexity
"""

import heapq
from typing import List, Optional, Tuple


class ListNode:
    __slots__ = ("val", "next")

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


def merge_k_lists_bruteforce(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Brute-force merge k sorted linked lists.
    Steps:
        1. Collect all node values into a Python list `vals`.
        2. Sort `vals`.
        3. Build a new linked list from sorted values, return its head
    Time: O (N log N), Space: O(N), where N = total number of nodes.
    """
    vals: List[int] = []
    for head in lists:
        curr = head
        while curr is not None:
            vals.append(curr.val)
            curr = curr.next
    if not vals:
        return None
    vals.sort()
    
    # Build new linked list base on vals
    dummy = ListNode(0)
    tail = dummy
    for val in vals:
        tail.next = ListNode(val)
        tail = tail.next
    
    return dummy.next

def merge_k_list_optimzed_min_heap_approach(linked_list: List[Optional[ListNode]]):
    """
    Merge k sorted lists using Min-Heap (Priority Queue).
    
    🔑 KEY IDEA:
    - Instead of comparing all k heads each time (O(k)),
    - Use a min-heap to get the smallest in O(log k)
    
    📊 ALGORITHM:
    1. Put first node of each list into min-heap
    2. Pop smallest node from heap → add to result
    3. If that node has .next, push it into heap
    4. Repeat until heap is empty
    
    ⏱️ TIME: O(N log k)
        - N total nodes
        - Each heap operation: O(log k)
        - Total: N × log k
    
    💾 SPACE: O(k)
        - Heap stores at most k nodes at any time
    
    🎯 WHY BETTER THAN BRUTE FORCE?
        - Brute Force: O(N log N) - sorts ALL nodes
        - Heap: O(N log k) - only maintains k candidates
        - When k << N (k much smaller than N), HUGE improvement!
        - Example: k=3, N=10000 → log 3 vs log 10000
    
    ⚠️ PYTHON HEAP TRICK:
        - heapq compares tuples: (val, idx, node)
        - idx prevents comparison errors when vals are equal
        - Python can't compare ListNode objects directly!
    """
    # Min-heap: stores (node.val, list_index, node)
    heap: List[Tuple[int, int, ListNode]] = []
    for idx, node in enumerate(linked_list):
        if node is not None:
            heapq.heappush(heap, (node.val, idx, node))
    
    dummy = ListNode(0)
    tail = dummy
    while heap:
        val, idx, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        
        # If current node has next, add it to heap   
        if node.next is not None:
            heapq.heappush(heap, (node.next.val, idx, node.next))
    return dummy.next

def print_linked_list(linked_list: List[Optional[ListNode]]) -> None:
    if not linked_list:
        print("Linked list is Emtpy")
        return
    
    for head in linked_list:
        curr = head
        while curr is not None:
            print(curr.val, end=" -> ")
            curr = curr.next
    print("None")
    
if __name__=="__main__":
    # Test case 1: Example from problem
    list1 = ListNode(1, ListNode(4, ListNode(5)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    list3 = ListNode(2, ListNode(6))
    lists = [list1, list2, list3]
    
    print("Input lists:")
    print_linked_list(lists)
    
    print("\nMerged result (Brute Force):")
    result = merge_k_lists_bruteforce(lists)
    print_linked_list([result])
    
    print("\n" + "="*50 + "\n")
    
    # Test case 2: Empty lists
    print("Test case 2: Empty lists")
    result2 = merge_k_lists_bruteforce([])
    print_linked_list([result2] if result2 else [])
    
    print("\n" + "="*50 + "\n")
    
    # Test case 3: Single list
    print("Test case 3: Single list")
    single = ListNode(1, ListNode(2, ListNode(3)))
    result3 = merge_k_lists_bruteforce([single])
    print_linked_list([result3])
    
    print("\n" + "="*50 + "\n")
    
    # Test case 4: Lists with one element each
    print("Test case 4: Lists with one element each")
    l1 = ListNode(1)
    l2 = ListNode(0)
    result4 = merge_k_lists_bruteforce([l1, l2])
    print_linked_list([result4])

