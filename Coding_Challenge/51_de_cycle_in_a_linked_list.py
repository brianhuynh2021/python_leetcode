'''
🔁 Chu trình (Cycle) là gì?

Giả sử ta không có node nào trỏ đến NULL, mà một node nào đó lại trỏ ngược 
về node trước nó hoặc một node nào đó trước đó ⇒ Danh sách sẽ 
bị lặp vô hạn ⇒ gọi là có chu trình.

Ví dụ có cycle:
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
def has_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    return False

# 🧪 Test Case 1: Không có chu trình
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d
# d.next = None

print("Test 1:", "Có chu trình" if has_cycle(a) else "Không có chu trình")

# 🧪 Test Case 2: Có chu trình
x = Node(10)
y = Node(20)
z = Node(30)

x.next = y
y.next = z
z.next = y  # Tạo chu trình

print("Test 2:", "Có chu trình" if has_cycle(x) else "Không có chu trình")