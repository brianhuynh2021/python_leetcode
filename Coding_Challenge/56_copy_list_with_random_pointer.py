class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head):
    if not head:
        return None

    old_to_new = {}
    current = head
    while current:
        # Create a new node with current value
        copy = Node(current.val)
        old_to_new[current] = copy
        current = current.next
    
    current = head
    while current:
        copy = old_to_new[current]
        copy.next = old_to_new.get(current.next)
        copy.random = old_to_new.get(current.random)
        current = current.next
        
    return old_to_new[head]

def print_list(head):
    current = head
    while current:
        random_val = current.random.val if current.random else None
        print(f"Node({current.val}), Random({random_val})")
        current = current.next


if __name__ == "__main__":
    # Tạo các node
    node1 = Node(7)
    node2 = Node(13)
    node3 = Node(11)
    node4 = Node(10)
    node5 = Node(1)

    # Nối next
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    # Gán random
    node1.random = None
    node2.random = node1
    node3.random = node5
    node4.random = node3
    node5.random = node1

    print("Original list:")
    print_list(node1)

    copied_head = copy_random_list(node1)

    print("\nCopied list:")
    print_list(copied_head)