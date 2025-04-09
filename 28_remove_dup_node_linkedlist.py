# With set

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if not head:
        return

    seen = set()
    current = head
    prev = None

    while current:
        if current.data in seen:
            prev.next = current.next  # Duplicate found, skip the node
        else:
            seen.add(current.data)  # First occurrence, add to set
            prev = current
        current = current.next

def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Example usage
head = Node(10)
head.next = Node(12)
head.next.next = Node(11)
head.next.next.next = Node(12)
head.next.next.next.next = Node(10)

print("Original List:")
print_list(head)

remove_duplicates(head)

print("List after removing duplicates:")
print_list(head)


# def remove_duplicates_no_buffer(head):
#     if not head:
#         return

#     current = head

#     while current:
#         runner = current
#         while runner.next:
#             if runner.next.data == current.data:
#                 runner.next = runner.next.next  # Remove duplicate
#             else:
#                 runner = runner.next
#         current = current.next