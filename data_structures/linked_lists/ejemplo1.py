'''
Ejemplo 1: Implementacion basica de una lista enlazada simple
'''

class Node:
    def __init__(self, data):
        self.data = data # Nodo contiene datos
        self.next = None # Apunta al siguiente nodo,  incialmente es None
        
class LinkedList:
    def __init__(self):
        self.head = None # Inicialmente, la lista esta vacia (head es None)
        
    def append(self, data):
        new_node = Node(data) # Crear un nuevo nodo con los datos proporcionados
        if not self.head:
            self.head = new_node # Si la lista esta vacia, el nuevo nodo es el primero
        else:
            current = self.head # itera hasta el ultimo nodo
            while current.next:
                current = current.next
            current.next = new_node # Enlazar el ultimo nodo con el nuevo nodo.
            
    def display(self):
        current = self.head
        while current: # Iterar y mostrar cada nodo
            print(current.data, end=" -> ")
            current = current.next
        print('None')
        
if __name__ == '__main__':
    from ejemplo1 import Node, LinkedList
    
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.display()
    
    '''
    1 -> 2 -> 3 -> None
    '''
    
    la = LinkedList()
    la.append(4)
    la.append(3)
    la.append(2)
    la.append(1)
    la.append(ll)
    la.display()
    
    '''
    4 -> 3 -> 2 -> 1 -> <ejemplo1.LinkedList object at 0x7f8ae74dfc10> -> None
    
    se puede guardar una linked list, dentro de una linked list
    '''