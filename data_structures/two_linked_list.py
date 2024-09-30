class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
# Usage

if __name__ == '__main__':
    from two_linked_list import Node
    
    linked_list = LinkedList()
    linked_list.head = Node(1)
    linked_list.head.next = Node(2)
    linked_list.head.next.next = Node(3)
    
    print(linked_list)
    # <__main__.LinkedList object at 0x7fa2c251ff40>