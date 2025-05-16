# Algorithm to Find the Kth to Last Element of a Singly Linked List

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_kth_to_last(head, k):
    fast = slow = head
    
    # Move the fast pointer k steps ahead
    for _ in range(k):
        if not fast:  # If k is larger than the list length
            return None
        fast = fast.next
    
    # Move both pointers until fast reaches the end
    while fast:
        fast = fast.next
        slow = slow.next
    
    return slow.value  # slow now points to the kth to last element

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2
result = find_kth_to_last(head, k)
if result is not None:
    print(f"The {k}th to last element is: {result}")
else:
    print("List is too short.")