'''
Ejemplo 7: Insertar en un indice especifico
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_index(self, data, index):
        new_node = Node(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        count = 0
        
        while current and count < index - 1:
            count += 1
            current = current.next
            
        if current is None:
            return # Si el indice es mayo que la longitud, no hace nada
        
        new_node.next = current.next
        current.next = new_node
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
            
        print('None')
        
if __name__ == '__main__':
    from ejemplo7 import SinglyLinkedList
    
    llist = SinglyLinkedList()
    llist.insert_at_index(10, 0)
    llist.insert_at_index(20, 1)
    llist.insert_at_index(15, 1)
    llist.display()
    # 10 -> 15 -> 20 -> None
    
    llist.insert_at_index(32, 0)
    llist.display()
    # 32 -> 10 -> 15 -> 20 -> None