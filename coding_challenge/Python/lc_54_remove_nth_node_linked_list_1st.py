class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        

class Solution:
    def remove_nth_node(self, head: Node, index: int) -> Node:
        if head is None:
            return None
        
        if index < 0:
            return head
        dummy = Node(-1)
        dummy.next = head
        
        prev = dummy
        
        for _ in range(index):
            if prev.next is None:
                return head
            prev = prev.next
        
        if prev.next is None:
            return head
        
        prev.next = prev.next.next
        
        return dummy.next
    
    def remove_nth_node_from_end(self)
    
    def print_node(self, head: Node) -> None:
        curr = head
        values = []
        
        while curr:
            values.append(str(curr.val))
            curr = curr.next
            
        print(" -> ".join(values))
        

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    
    sol = Solution()
    print("Before:")
    sol.print_node(head)
    
    head = sol.remove_nth_node(head, 2)
    print("After:")
    sol.print_node(head)