"""
Bài toán: Tìm node bắt đầu chu trình trong danh sách liên kết đơn
(Linked List Cycle Start)

Phân tích:
- Một danh sách liên kết đơn có thể có chu trình (vòng lặp) nếu một node nào
đó trỏ ngược về node trước đó.
- Mục tiêu là: nếu có chu trình, hãy trả về node nơi chu trình bắt đầu.
- Nếu không có chu trình, trả về None.

Ý tưởng:
- Sử dụng kỹ thuật "hai con trỏ" (slow & fast pointer).
- Phase 1: Di chuyển slow (1 bước) và fast (2 bước) cho đến khi gặp nhau.
Nếu không gặp → không có chu trình.
- Phase 2: Đặt slow lại về head, rồi cho slow và fast đi 1 bước
mỗi lần → khi gặp nhau là node bắt đầu chu trình.

Input:
- Một danh sách liên kết đơn, được xây dựng từ một list Python.

Output:
- Node bắt đầu của chu trình nếu tồn tại, hoặc None nếu không có chu trình.

Ví dụ:
Input: [1, 3, 5, 7, 9]
→ Không có chu trình → Output: None

Nếu tạo chu trình như: node cuối (giá trị 9) trỏ về node có giá trị 5,
→ Chu trình bắt đầu tại node có giá trị 5 → Output: Node(5)
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def build_linked_list(values: list[int]):
    if not values:
        return None

    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next

    return head


def find_linked_list_cycle_node(l: Node) -> Node:
    if not l:
        return None
    slow = l
    fast = l

    while (
        fast and fast.next
    ):  # Điều kiện để thoát khỏi vòng while vì phải check node kế tiếp có None ko
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # Linked list khong co chu trinh
    # Lúc này fast đang ở node giao với slow
    # nên đặt slow đi lại từ đầu vậy cả 2 sẽ gặp nhau tại node nào đó sau khi đi
    # 1 (hoặc vài chu trình)
    slow = l
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def print_linked_list(head: Node):
    while head:
        print(f"{head.val}->", end="")
        head = head.next
    print("None")


if __name__ == "__main__":
    values = [1, 3, 5, 7, 9]
    head = build_linked_list(values)

    cycle_node = find_linked_list_cycle_node(head)

    if cycle_node:
        print(f"Chu trình bắt đầu tại node có giá trị {cycle_node.val}")
    else:
        print("Không có chu trình. Danh sách liên kết:")
        print_linked_list(head)
