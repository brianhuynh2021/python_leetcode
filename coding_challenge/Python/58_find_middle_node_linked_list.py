# Bài toán “Middle of the Linked List” là một bài toán 
# rất phổ biến và kinh điển khi làm việc với danh sách liên kết (linked list). 
# Cùng phân tích bài toán để hiểu rõ hơn nhé!

# 🚩 Phân tích bài toán:
# 	•	Đề bài: Cho một danh sách liên kết đơn, tìm nút ở chính giữa danh sách.
# 	•	Nếu danh sách có số lượng nút lẻ, hãy trả về nút chính giữa.
# 	•	Nếu danh sách có số lượng nút chẵn, hãy trả về nút thứ hai trong hai nút ở giữa.

# Ví dụ:
# 	•	Input: 1 → 2 → 3 → 4 → 5
# Output: 3
# 	•	Input: 1 → 2 → 3 → 4 → 5 → 6
# Output: 4

# 📌 Ý tưởng giải pháp:

# Một cách hiệu quả để giải quyết bài toán này là sử dụng kỹ thuật hai con trỏ (two-pointer):
# 	•	Con trỏ nhanh (fast pointer): Di chuyển mỗi lần 2 bước.
# 	•	Con trỏ chậm (slow pointer): Di chuyển mỗi lần 1 bước.

# Khi con trỏ nhanh di chuyển tới cuối danh sách, con trỏ chậm sẽ nằm ngay tại nút giữa.

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        
def get_middle_node(head: Node):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def print_linked_list(l):
    while l:
        print(f"{l.val}->", end="")
        l = l.next
    print('None')

def build_linked_list(data = list[int])->Node:
    if not data:
        return None
    head = Node(data[0])
    tail = head
    for val in data[1:]:
        tail.next = Node(val)
        tail = tail.next
    return head

if __name__ == '__main__':
    values = [1, 3, 5, 7, 9]
    head = build_linked_list(values)
    
    print('Danh sach lien ket don')
    print_linked_list(head)
    
    middle = get_middle_node(head)
    print('Nút giữa là: ', middle.val)
    
    value_1 = [2, 4, 6, 8, 10, 12]
    head_1 = build_linked_list(value_1)
    
    print('Danh sach lien ket don')
    print_linked_list(head_1)
    
    middle_1 = get_middle_node(head_1)
    print('Nút giữa là: ', middle_1.val)