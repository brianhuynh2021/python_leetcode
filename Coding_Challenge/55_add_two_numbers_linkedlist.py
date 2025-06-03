"""
Problem: Add Two Numbers using Linked List
Bài toán: Cộng hai số dùng danh sách liên kết

Each number is represented as a reversed linked list.
Mỗi số được biểu diễn dưới dạng danh sách liên kết đơn và theo thứ tự ngược.

Each node contains a single digit. Return the sum as a linked list (also reversed).
Mỗi node chứa một chữ số. Trả về tổng hai số cũng dưới dạng danh sách liên kết đảo ngược.

Input:
    l1: 2 -> 4 -> 3   (represents 342)
    l1: 2 -> 4 -> 3   (biểu diễn số 342)

    l2: 5 -> 6 -> 4   (represents 465)
    l2: 5 -> 6 -> 4   (biểu diễn số 465)

Output:
    result: 7 -> 0 -> 8   (represents 807)
    Kết quả: 7 -> 0 -> 8   (biểu diễn số 807)

Note:
    - The digits are stored in reverse order.
    - Các chữ số được lưu theo thứ tự ngược (units digit trước).

    - Return a new linked list that also follows this order.
    - Trả về một danh sách liên kết mới, cũng theo thứ tự ngược.

    - Handle carry (nhớ) khi tổng vượt quá 9.
    - Cần xử lý số nhớ khi cộng hai chữ số > 9.
"""

class ListNode:
    def __init__(self, val, next=None): # Tạo constructor cho Node/ListNode
        self.val = val
        self.next = next
        
def add_two_numbers(l1: ListNode, l2: ListNode)->ListNode:
    carry = 0 # Số nhớ từ bước cộng trước đó
    dummy = ListNode(0) # Tạo node giả
    current = dummy
    while l1 or l2 or carry:
        '''Lấy giá trị của l1 và l2 tại vị trí hiện tại để thực hiện phép cộng.
           Nhưng vì có thể l1 hoặc l2 đã hết (tức là None) → ta dùng 0 thay 
           thế để tránh lỗi.
        '''
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        digit = total % 10 # Chia 10 lấy phần dư và ta lấy được hàng đơn vị
        carry = total // 10 # Chia 10 lấy phần nguyên vd: 14 // 10 được 1 dư 4 lấy 1
        
        current.next = ListNode(digit) 
        # Tao node mới khi cộng 2 node lại với nhau được hàng đơn vị
        
        current = current.next # Di chuyển con trỏ `current` sang node vừa 
                               # thêm để chuẩn bị cho vòng lặp tiếp theo
        # Sau khi xủ lý node                    
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
            
    return dummy.next # tra ve kết quả

def build_linked_list(values):
    """Tạo danh sách liên kết từ danh sách các số"""
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    """In danh sách liên kết dạng 7 -> 0 -> 8"""
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

if __name__ == "__main__":
    # Test case từ đề bài: 342 + 465 = 807
    l1 = build_linked_list([2, 4, 3])  # 342
    l2 = build_linked_list([5, 6, 4])  # 465

    result = add_two_numbers(l1, l2)
    print("Kết quả cộng 2 số là:")
    print_linked_list(result)  # Output dự kiến: 7 -> 0 -> 8       
    