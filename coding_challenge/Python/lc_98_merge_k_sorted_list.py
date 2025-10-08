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
        cur = head
        while cur is not None:
            vals.append(cur.val)
            cur = cur.next
    if not vals:
        return None

    vals.sort()
    dummy = ListNode(0)
    tail = dummy
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next

    return dummy.next


def list_to_linked(lst: list[int]) -> Optional[ListNode]:
    """
    Convert a Python list to a linked list.
    """
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_to_list(node: Optional[ListNode]) -> list[int]:
    """
    Convert a linked list back to a Python list.
    """
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def merge_k_lists_heap(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap: List[Tuple[int, int, ListNode]] = []

    for idx, node in enumerate(lists):
        if node is not None:
            heapq.heappush(heap, (node.val, idx, node))
    dummy = ListNode(0)
    tail = dummy

    while heap:
        val, idx, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next

        if node.next is not None:
            heapq.heappush(heap, (node.next.val, idx, node.next))
    return dummy.next
