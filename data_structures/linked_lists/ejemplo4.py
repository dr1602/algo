'''
Ejemplo 4: Encontrar el Tamano de la Lista Enlazada
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1 # Incrementar el contador por cada nodo
            current = current.next
        return count
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')
        
if __name__ == '__main__':
    from ejemplo4 import LinkedList
    
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    
    print(f'Tamano de la lista es: {ll.size()}')
    
    ll.display()
    
    '''
    Tamano de la lista es: 6
    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
    '''
    
    la = LinkedList()
    la.append('a')
    la.append('b')
    la.append('c')
    la.display()
    
    # a -> b -> c -> None
    
    ll.append(la)
    ll.display()
    
    # 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> <ejemplo4.LinkedList object at 0x7f799dda1870> -> None
    
    ll.display(la.display())
    
    # error
    