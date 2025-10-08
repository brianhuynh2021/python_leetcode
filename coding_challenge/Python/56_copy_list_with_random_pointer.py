"""
    📘 Problem: Copy List with Random Pointer, trên leetcode sẽ là bài #138

    Bạn được cho một danh sách liên kết đặc biệt trong đó mỗi node có:
	•	Một trường val (giá trị số nguyên)
	•	Một con trỏ next trỏ đến node tiếp theo
	•	Một con trỏ random có thể trỏ đến bất kỳ node nào trong danh sách hoặc null

    👉 Yêu cầu:
    Tạo deep copy của danh sách — tức là tạo ra một danh sách mới độc lập hoàn toàn,
    với cùng giá trị và cấu trúc liên kết (next và random) như danh sách gốc.

    Input: [[7,None],[13,0],[11,4],[10,2],[1,0]]
    Giải thích:
	•	Node 0: val = 7, random = null
	•	Node 1: val = 13, random = node 0
	•	Node 2: val = 11, random = node 4
	•	Node 3: val = 10, random = node 2
	•	Node 4: val = 1, random = node 0

    7 → 13 → 11 → 10 → 1
     ↑    ↑      ↑
     7    1      7   (random trỏ về)
    ✅ Ví dụ minh họa dễ hiểu nhất:

    Danh sách gốc:
        A(7) → B(13) → C(11)
        |       |       |
       [None]  [A]     [C]
    ✅ Output:
    Một danh sách mới có:
        A'(7) → B'(13) → C'(11)
        |       |         |
      [None]  [A']      [C']
        •	Các node mới hoàn toàn (không trỏ đến node cũ)
        •	val, next, random giống hệt bản gốc
        •	Ví dụ, nếu đầu vào là node có val = 7, thì kết quả là
        node val = 7 (mới) với random giống cấu trúc gốc
    ⸻
    📌 Input Constraints:
        •	Số node ≤ 1000
        •	-10⁴ ≤ Node.val ≤ 10⁴
        •	random có thể là null hoặc trỏ về node bất kỳ trong danh sách
"""


class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def copy_random_list(head):
    if not head:  # Kiểm tra danh sách linkedlist có rỗng ko nhé
        return None

    old_to_new = {}  # dùng để tạo dictionary linked
    current = head  # Tạo biến tạm/node đầu để duyệt lần 1
    while current:
        # Create a new node with current value
        copy = Node(current.val)
        old_to_new[current] = copy
        current = current.next
    # Lúc này hết vòng while thứ nhất current = None rồi nhé
    # Tiếp tục duyệt lại list nodes để gán cho next và random cho list mới
    # current dưới dòng này là gán lại bằng head, các anh/chị có thể ghi temp hay biến duyệt
    # vòng 2 không nhất thiết lấy lại biến current có thể ghi temp/current_2/whatever
    # Các copy node đều có next và random băng None hết
    current = head

    while current:
        copy = old_to_new[
            current
        ]  # cái này là deepcopy # các bạn xem thêm shallowcopy ở description nhé
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
