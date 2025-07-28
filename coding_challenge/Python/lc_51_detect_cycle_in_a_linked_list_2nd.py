"""
🔁 Chu trình (Cycle) là gì?

Giả sử ta không có node nào trỏ đến NULL, mà một node nào đó lại trỏ ngược
về node trước nó hoặc một node nào đó trước đó ⇒ Danh sách sẽ
bị lặp vô hạn ⇒ gọi là có chu trình.

Ví dụ có cycle:
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def detect_cycle_brute(head: Node) -> bool:
    """
    Detects if there is a cycle in the linked list using a set to track visited nodes.

    Args:
        head (Node): Head of the singly linked list.

    Returns:
        bool: True if cycle exists, False otherwise.
    """
    visited_nodes = set()
    curr_node = head
    while curr_node:
        if curr_node in visited_nodes:
            return True # Cycle detected
        visited_nodes.add(curr_node)
        curr_node = curr_node.next
    return False

def detect_cycle_optimized(head: Node) -> bool:
    """
    Uses Floyd’s Tortoise and Hare algorithm to detect a cycle in a linked list.

    Args:
        head (Node): Head of the singly linked list.

    Returns:
        bool: True if a cycle exists, False otherwise.
    """
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False