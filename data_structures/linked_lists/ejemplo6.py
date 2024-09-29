'''
Ejemplo 5: Buscar un valor en la lista
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
            
    def search(self, key):
        current = self.head
        
        while current:
            if current.data == key:
                return True # Si se encuentra el valor, retorna True
            
            current = current.next
        return False # Si no se encuentra, retornar False
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

if __name__ == '__main__':
    from ejemplo6 import SinglyLinkedList
    
    llist = SinglyLinkedList()
    llist.append(5)
    llist.append(8)
    llist.append(10)
    llist.append(13)
    llist.append(17)
    
    print(llist.search(8)) # Salida: True
    print(llist.search(30)) # Salida: False
    
    llist.display()
    '''
    5 -> 8 -> 10 -> 13 -> 17 -> None
    '''
    
