class Node:
    """
    A class representing a single node in a singly linked list.
    Each node contains a value and a reference to the next node.
    """

    def __init__(self, val):
        self.val = val
        self.next = None


def reverse_linked_list_brute(head: Node) -> Node:
    """
    Reverse a singly linked list using a brute-force approach:
    - Store all nodes in a list
    - Re-link them in reverse order
    """
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    for i in range(len(nodes) - 1, 0, -1):
        nodes[i].next = nodes[i - 1]
    nodes[0].next = None
    return nodes[-1]


def build_linked_list(nums: list[int]):
    if not nums:
        return None
    head = Node(nums[0])
    current = head
    for num in nums[1:]:
        current.next = Node(num)
        current = current.next
    return head


def print_linked_list(head: Node):
    current = head
    output = []
    while current:
        output.append(str(current.val))
        current = current.next
    print("->".join(output) + "->None")


# ✅ MAIN – TEST EVERYTHING
if __name__ == "__main__":
    # Build the list
    nums = [1, 2, 3, 4, 5]
    head = build_linked_list(nums)

    print("Original Linked List:")
    print_linked_list(head)

    # Reverse using brute-force
    reversed_head = reverse_linked_list_brute(head)

    print("Reversed Linked List (Brute Force):")
    print_linked_list(reversed_head)
