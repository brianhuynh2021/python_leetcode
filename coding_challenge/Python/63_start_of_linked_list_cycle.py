"""
Bài toán: Tìm node bắt đầu của chu trình trong danh sách liên kết đơn (Linked List).

Mục tiêu:
- Cho một danh sách liên kết có thể chứa chu trình.
- Nếu có chu trình, trả về node bắt đầu của chu trình.
- Nếu không có chu trình, trả về None.

Input: head của danh sách liên kết đơn
Output: node bắt đầu chu trình hoặc None

Thuật toán sử dụng:
- Floyd's Cycle Detection Algorithm (Thuật toán Rùa và Thỏ - Tortoise and Hare)
- Gồm 2 bước:
    1. Dò xem có chu trình không bằng cách cho 2 con trỏ đi với tốc độ khác nhau.
    2. Khi gặp nhau, reset 1 con trỏ về đầu, đi từng bước cho đến khi gặp lại.
"""


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def start_of_linked_list(head):
    slow = head
    fast = head
    # Bước 1: Dò xem có chu trình không bằng cách dùng slow và fast
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break  # phát hiện được linked list có chu trình (cycle)
    else:
        return None  # Không có chu trình

    # Bước 2: Đặt lại slow về head để tìm node bắt đầu của chu trình
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow  # slow (hoặc fast) đang trỏ tới node bắt đầu của chu trình


def build_linked_list(values: list[int]):
    if not values:
        return None  # Trường hợp danh sách rỗng
    head = Node(values[0])  # Tạo node đầu tiên
    current = head
    for val in values[1:]:
        current.next = Node(val)  # Tạo node mới và nối vào danh sách
        current = current.next  # Di chuyển con trỏ tới node mới
    return head


def print_linked_list(head):
    current = head
    while current:
        print(f"{current.val}->", end="")  # In giá trị node hiện tại
        current = current.next
    print("None")  # Kết thúc danh sách


def create_cycle(head: Node, pos: int) -> Node:
    """
    Tạo chu trình trong linked list bằng cách nối node cuối về node tại vị trí 'pos' (0-based index).
    Nếu pos == -1 thì không tạo chu trình.
    """
    if pos == -1:
        return head

    tail = head
    cycle_entry = None
    index = 0

    while tail.next:
        if index == pos:
            cycle_entry = tail
        tail = tail.next
        index += 1

    if index == pos:
        cycle_entry = tail

    tail.next = cycle_entry
    return head


if __name__ == "__main__":
    print("Test: Start of Linked List Cycle")

    # Input: danh sách có chu trình, node cuối nối về node có giá trị 7 (index 2)
    values = [1, 5, 7, 11, 23, 59]
    head = build_linked_list(values)
    head = create_cycle(head, pos=1)  # tạo chu trình thực sự

    # Không in toàn bộ linked list vì có thể vô hạn nếu có chu trình

    # Output: node bắt đầu chu trình (dự kiến là node có giá trị 7)
    start_of_cycle = start_of_linked_list(head)
    print("Start of cycle is: ", start_of_cycle.val if start_of_cycle else None)
