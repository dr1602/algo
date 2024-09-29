'''
Insertar al Inicio de la Lista
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def prepend(self, data):
        new_node = Node(data) # Crear un nuevo nodo
        new_node.next = self.head # El nuevo nodo apunta al antiguo head
        self.head = new_node # Cambiar el head al nuevo nodo
        
    def display(self):
        current = self.head
        
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')
        
if __name__ == '__main__':
    from ejemplo2 import Node, LinkedList
    
    ll = LinkedList()
    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)
    ll.prepend(0)
    ll.display()
    
    '''
    0 -> 1 -> 2 -> 3 -> None
    '''
    
    la = LinkedList()
    la.prepend(0)
    la.prepend(1)
    la.prepend(2)
    la.prepend(3)
    la.prepend(ll)
    la.display()
    
    '''
    <ejemplo2.LinkedList object at 0x7f5d28a8bfd0> -> 3 -> 2 -> 1 -> 0 -> None
    '''