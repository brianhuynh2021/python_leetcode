class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def print_link_list(head: Node):
    while head:
        print(f"{head.val}->", end="")
        head = head.next
    print("None")


if __name__ == "__main__":
    # 1 -> 2 -> 3 -> None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    print_link_list(head)
