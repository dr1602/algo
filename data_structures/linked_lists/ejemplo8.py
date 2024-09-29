'''
Ejemplo 8: Eliminar en un indice especifico
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def delete_at_index(self,index):
        current = self.head
        
        if index == 0:
            self.head = current.next
            current = None
            return
        
        count = 0
        previous = None
        
        while current and count < index:
            previous = current
            current = current.next
            count += 1
            
        if current is None:
            return # Si el indices es mayor que la longitud, no hace nada
        
        previous.next = current.next
        current = None
        
    def display(self):
        current = self.head
        
        while current:
            print(current.data, end=' -> ')
            current = current.next
            
        print('None')
        
if __name__ == '__main__':
    from ejemplo8 import SinglyLinkedList
    
    llist = SinglyLinkedList()
    llist.append(5)
    llist.append(10)
    llist.append(15)
    llist.append(20)
    llist.append(25)
    llist.append(30)
    
    llist.delete_at_index(3)
    llist.display()
    
    # 5 -> 10 -> 15 -> 25 -> 30 -> None
    
    llist.delete_at_index(0)
    llist.display()
    
    # 10 -> 15 -> 25 -> 30 -> None