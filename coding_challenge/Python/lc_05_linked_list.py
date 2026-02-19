# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head

#     def insert_at_the_end_of_node(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last_node = self.head  # start to traverse the LinkedList from head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def print_nodes(self):
#         current_node = self.head
#         print("current node ==>", current_node)
#         while current_node:
#             print(current_node.data, end=" -> ")
#             current_node = current_node.next
#         print("None")


# ll = LinkedList()
# ll.insert_at_the_end_of_node(2)
# ll.insert_at_the_end_of_node(4)
# ll.print_nodes()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        
    def insert_at_end(self, data):