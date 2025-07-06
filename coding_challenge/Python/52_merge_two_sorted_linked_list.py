class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Hàm gộp 2 danh sách liên kết đã sắp xếp
def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return dummy.next

# Hàm in danh sách
def printList(head):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()

# Hàm tạo danh sách từ list Python
def buildList(values):
    if not values:
        return None
    head = ListNode(values[0])
    tail = head
    for val in values[1:]:
        tail.next = ListNode(val)
        tail = tail.next
    return head

# MAIN: chạy test
if __name__ == "__main__":
    l1 = buildList([1, 3, 5])
    l2 = buildList([2, 4, 6])

    merged = mergeTwoLists(l1, l2)
    print("Merged List:")
    printList(merged)