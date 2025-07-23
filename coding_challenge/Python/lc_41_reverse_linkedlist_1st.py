class Node:
     """
    A class representing a single node in a singly linked list.
    Each node contains a value and a reference to the next node.
    """
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_linked_list_brute(head: Node)->Node:
    """
    Reverse a singly linked list using a brute-force approach:
    - Store all nodes in a list
    - Re-link them in reverse order
    """
    while head:
        print(head.val, end="->")
        head = head.next
    print("None")