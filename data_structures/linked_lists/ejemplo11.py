'''
Ejemplo 3: Busqueda en una lista enlazada de nodos
'''

class Node():
    def __init__(self, data, next=None):
        self.data = data # El nodo guarda un valor
        self.next = next # Apunta al siguiente nodo (None por defecto)
        
def search_node(head, target_value):
    current = head # Empieza desde el nodo cabeza
    
    while current is not None: # Recorre la lista hasta el final
        if current.data == target_value:
            return True # Si el valor coincide, retorna True
        current = current.next # moverse al siguiente nodo
    return False # Si no encuentra el valor, retorna False

if __name__ == '__main__':
    # Creamos una pequena lista enlazada mutuamente
    node_1 = Node(10)           # En este ejemplo especifico, este es 3er nodo
    node_2 = Node(20, node_1)   # En este ejemplo especifico, este es 2do nodo
    node_3 = Node(30, node_2)   # En este ejemplo especifico, este es 1er nodo
    
    # El nodo cabeza es node_3
    head = node_3
    
    # Buscamos un valor en la lista
    print(search_node(head, 20)) # Salida: True, ya que el valor esta en la lista 
    print(search_node(head, 40)) # Salida: False, el valor no esta en la lista
        
        