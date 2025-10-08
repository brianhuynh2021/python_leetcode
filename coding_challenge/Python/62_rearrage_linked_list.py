# Problem: Rearrange Linked List
# Given a singly linked list, rearrange it such that the nodes are reordered in a specific pattern:
# For example, given the list 1 → 2 → 3 → 4 → 5 → 6,
# the rearranged list should be 1 → 6 → 2 → 5 → 3 → 4.
# Input: Head of a singly linked list.
# Output: Head of the rearranged linked list.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def find_middle_node(head: Node) -> Node:
    # Use two pointers, slow and fast, to find the middle node of the linked list
    if not head:
        return None
    slow = head
    fast = head
    # Move fast pointer two steps and slow pointer one step until fast reaches the end
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # slow now points to the middle node
    return slow


def reverse_linked_list(head: Node) -> Node:
    # Reverse the linked list starting from head
    if not head:
        return None
    prev = None
    current = head
    while current:
        next_node = current.next  # Store next node
        current.next = prev  # Reverse current node's pointer
        prev = current  # Move prev to current
        current = next_node  # Move to next node
    # prev is new head of reversed list
    return prev


def rearrange_linked_list(head: Node) -> Node:
    # Rearrange the linked list by alternating nodes from start and end
    if not head or not head.next:
        return head

    # Find the middle of the linked list
    middle = find_middle_node(head)
    # Reverse the second half of the list starting from middle
    second_half = reverse_linked_list(middle)

    first = head
    second = second_half

    # Merge nodes from first half and reversed second half alternately
    while second.next:
        temp1 = first.next  # Store next node of first half
        temp2 = second.next  # Store next node of second half

        first.next = (
            second  # Link current node of first half to current node of second half
        )
        second.next = (
            temp1  # Link current node of second half to next node of first half
        )

        first = temp1  # Move to next node in first half
        second = temp2  # Move to next node in second half

    return head


def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" → ".join(result))


if __name__ == "__main__":
    print("Test: Rearranging linked list")
    values = [1, 2, 3, 4, 5, 6]
    head = build_linked_list(values)
    print("Original list:")
    print_linked_list(head)

    rearranged = rearrange_linked_list(head)
    print("Rearranged list:")
    print_linked_list(rearranged)
