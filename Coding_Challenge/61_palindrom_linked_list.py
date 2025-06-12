"""
===========================================
💥 BÀI TOÁN: PALINDROME LINKED LIST
===========================================

🎯 Mục tiêu:
    Kiểm tra xem một danh sách liên kết đơn (Singly Linked List)
    có phải là chuỗi Palindrome hay không – tức là đọc xuôi
    hay ngược đều giống nhau.

🧠 Ý tưởng thuật toán (cực hay!):
    ✅ Bước 1: Dùng kỹ thuật "RÙA và THỎ" (slow và fast pointer)
             để tìm ra điểm giữa danh sách liên kết.
    ✅ Bước 2: Đảo ngược nửa sau của danh sách.
    ✅ Bước 3: So sánh từng phần tử từ hai phía (đầu và cuối).
              Nếu giống nhau hoàn toàn → là Palindrome!

🧪 Ví dụ:
    Input:  [1, 2, 2, 1]
    Linked: 1 → 2 → 2 → 1 → None
    ✅ Output: True (vì đọc xuôi hay ngược đều giống nhau)

    Input:  [1, 2, 3]
    Linked: 1 → 2 → 3 → None
    ❌ Output: False (vì không đối xứng)
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# -----------------------------------------
# 🎯 Tạo linked list từ list Python
def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

# -----------------------------------------
# 🔄 Đảo ngược linked list
def reverse_linked_list(head):
    prev = None
    while head:
        next_node = head.next      # Ghi nhớ node kế tiếp
        head.next = prev           # Đảo chiều liên kết
        prev = head                # Di chuyển prev về node hiện tại
        head = next_node           # Sang node tiếp theo
    return prev  # Trả về node đầu tiên sau khi đảo

# -----------------------------------------
# 💥 Kiểm tra Linked List có phải Palindrome
def is_palindrome(head):
    if not head or not head.next:
        return True  # Danh sách rỗng hoặc 1 phần tử luôn là Palindrome

    # Bước 1: Tìm node giữa bằng slow–fast pointer
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Bước 2: Nếu là danh sách lẻ → bỏ node giữa
    if fast:
        slow = slow.next

    # Bước 3: Đảo ngược nửa sau danh sách
    right = reverse_linked_list(slow)

    # Bước 4: So sánh từng node giữa nửa đầu và nửa sau
    left = head
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True

# -----------------------------------------
# 🧪 Test
if __name__ == "__main__":
    values = [1, 2, 3, 2, 1]
    head = build_linked_list(values)
    print("✅ Is Palindrome:", is_palindrome(head))
    print(is_palindrome(build_linked_list([1, 2, 2, 1])))
    print(is_palindrome(build_linked_list([1, 2, 3])))
    print(is_palindrome(build_linked_list([1])))
    print(is_palindrome(build_linked_list([])))
    