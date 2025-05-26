"""
🔁 Chu trình (Cycle) là gì?

Giả sử ta không có node nào trỏ đến NULL, mà một node nào đó lại trỏ ngược
về node trước nó hoặc một node nào đó trước đó ⇒ Danh sách sẽ
bị lặp vô hạn ⇒ gọi là có chu trình.

Ví dụ có cycle:
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_cycle(head):
    slow = head
    fast = head
    step = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        step += 1
        print(f"[Step {step}] slow at {slow.value}, fast at {fast.value}")
        if slow == fast:
            print(f"Gap nhau tai Node co gia tri: {slow.value}")
            return True
    print("==> Khong co chu trinh")
    return False

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = c

has_cycle(a)