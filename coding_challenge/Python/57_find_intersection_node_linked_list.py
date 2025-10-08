"""
    🔍  Mô tả bài toán:

        Bạn được cho hai danh sách liên kết đơn: List A và List B.
	    Nhiệm vụ là tìm nút giao nhau đầu tiên, nơi mà hai danh sách bắt đầu chia sẻ
        cùng một chuỗi các nút (tức là hai con trỏ cùng trỏ tới cùng một node trong bộ nhớ).
    🧠 Ví dụ hình minh hoạ:
        List A: a1 → a2
                        ↘
                        c1 → c2 → c3
                        ↗
        List B: b1 → b2 → b3
    Kết quả bạn cần trả về là node c1, vì từ đó trở đi hai danh sách có chung node.

"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Hàm tìm node giao nhau giữa hai danh sách
def find_intersection_linked_list(head_1, head_2):
    # Kiểm tra nếu một trong hai danh sách rỗng thì chắc chắn không giao nhau
    if not head_1 or not head_2:
        return None

    # Khởi tạo 2 con trỏ tạm để duyệt từ đầu danh sách
    p1, p2 = head_1, head_2

    # Duyệt đồng thời hai con trỏ
    # Khi một con trỏ đi hết danh sách thì nó sẽ chuyển sang đầu danh sách còn lại
    # Nếu hai danh sách giao nhau, hai con trỏ sẽ gặp nhau tại node giao
    while p1 != p2:
        p1 = p1.next if p1 else head_2
        p2 = p2.next if p2 else head_1

    # Trả về node giao nhau, hoặc None nếu không có giao nhau
    return p1  # trả về p1 hay p2 đều được


# Hàm in danh sách liên kết
def print_list(head, label):
    print(f"{label}: ", end="")
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# Hàm in kết quả node giao nhau
def print_node(node):
    if node:
        print(f"Node giao nhau có giá trị: {node.val}")
    else:
        print("Không có node giao nhau.")


if __name__ == "__main__":
    # Tạo đoạn chung giữa hai danh sách: c1 -> c2 -> c3
    c1 = Node(8)
    c2 = Node(10)
    c3 = Node(12)
    c1.next = c2
    c2.next = c3

    # Tạo danh sách A: a1 -> a2 -> c1
    a1 = Node(3)
    a2 = Node(7)
    a1.next = a2
    a2.next = c1

    # Tạo danh sách B: b1 -> b2 -> b3 -> c1
    b1 = Node(99)
    b2 = Node(1)
    b3 = Node(5)
    b1.next = b2
    b2.next = b3
    b3.next = c1

    # In danh sách A và B
    print_list(a1, "Danh sách A")
    print_list(b1, "Danh sách B")

    # Gọi hàm kiểm tra node giao nhau
    intersection = find_intersection_linked_list(a1, b1)

    # In kết quả
    print_node(intersection)
