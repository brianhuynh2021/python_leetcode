"""
🧠 Problem Understanding

You’re given two sorted singly linked lists.
Your task is to merge them into one sorted list
(also singly linked).
You should return the head of the new merged list.
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_2_linked_list(l1, l2):
    values = []
    while l1:
        values.append(l1.val)
        l1 = l1.next
    while l2:
        values.append(l2.val)
        l2 = l2.next
    values.sort()

    dummy = Node(-1)
    curr = dummy
    for val in values:
        curr.next = val
        curr = curr.next
    return dummy.next


def merge_two_sorted_lists_no_dummy(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    # Khởi tạo head: chọn node nhỏ hơn giữa l1 và l2
    if l1.val < l2.val:
        head = l1
        l1 = l1.next
    else:
        head = l2
        l2 = l2.next

    tail = head

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Gắn phần còn lại
    tail.next = l1 if l1 else l2

    return head


def merge_two_sorted_lists_optimized(l1: Node, l2: Node) -> Node:
    """
    Optimized in-place merge of two sorted linked lists.
    Time: O(n + m), Space: O(1)
    """
    dummy = Node(-1)  # value doesn't matter
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Attach the remaining part of list (either l1 or l2)
    tail.next = l1 if l1 else l2

    return dummy.next
