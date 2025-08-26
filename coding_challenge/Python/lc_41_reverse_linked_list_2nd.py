class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        
def reverse_linked_list_optimzed(head: Node):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev