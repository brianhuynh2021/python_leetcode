# Định nghĩa class Node (ListNode)
class ListNode:
    def __init__(self, val):
        self.val = val        # Giá trị của node
        self.next = None      # Con trỏ đến node tiếp theo

# Hàm xóa node thứ N từ cuối danh sách
def remove_nth_from_end(head, n):
    dummy = ListNode(0)       # Tạo node giả để đứng trước node head
    dummy.next = head         # Nối dummy với head
    slow = dummy              # slow và fast đều bắt đầu từ dummy
    fast = dummy

    # Bước 1: Cho fast đi trước n bước
    for _ in range(n):
        fast = fast.next

    # Bước 2: Di chuyển cả fast và slow cho đến khi fast đến node cuối
    while fast.next:
        slow = slow.next
        fast = fast.next

    # Bây giờ slow đứng ngay trước node cần xóa
    to_delete = slow.next
    slow.next = to_delete.next  # Bỏ qua node cần xóa

    # Python không cần delete thủ công như C++
    return dummy.next           # Trả về head mới (có thể đã thay đổi)

# Hàm in toàn bộ danh sách
def print_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# Tạo danh sách: 1 → 2 → 3 → 4 → 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n = 2  # Xóa node thứ 2 từ cuối (node 4)
head = remove_nth_from_end(head, n)  # Gọi hàm xử lý

print_list(head)  # In danh sách sau khi xóa