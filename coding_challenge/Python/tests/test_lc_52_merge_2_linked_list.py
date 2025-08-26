import unittest
from lc_52_merge_two_sorted_linked_list_2nd import merge_two_sorted_lists_optimized

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(-1)
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next

class TestMergeTwoSortedLists(unittest.TestCase):
    def list_to_linkedlist(self, lst):
        dummy = ListNode()
        current = dummy
        for num in lst:
            current.next = ListNode(num)
            current = current.next
        return dummy.next

    def linkedlist_to_list(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_both_empty(self):
        self.assertIsNone(merge_two_sorted_lists(None, None))

    def test_one_empty(self):
        l1 = self.list_to_linkedlist([1, 2, 3])
        l2 = None
        result = merge_two_sorted_lists(l1, l2)
        self.assertEqual(self.linkedlist_to_list(result), [1, 2, 3])

    def test_merge_normal_case(self):
        l1 = self.list_to_linkedlist([1, 2, 4])
        l2 = self.list_to_linkedlist([1, 3, 4])
        result = merge_two_sorted_lists(l1, l2)
        self.assertEqual(self.linkedlist_to_list(result), [1, 1, 2, 3, 4, 4])

    def test_all_values_equal(self):
        l1 = self.list_to_linkedlist([2, 2])
        l2 = self.list_to_linkedlist([2, 2])
        result = merge_two_sorted_lists(l1, l2)
        self.assertEqual(self.linkedlist_to_list(result), [2, 2, 2, 2])

    def test_interleaved(self):
        l1 = self.list_to_linkedlist([1, 3, 5])
        l2 = self.list_to_linkedlist([2, 4, 6])
        result = merge_two_sorted_lists(l1, l2)
        self.assertEqual(self.linkedlist_to_list(result), [1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    unittest.main()