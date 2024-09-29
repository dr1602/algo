'''
Ejemplo 10: Construir una lista de nodos con bucle
'''

class Node:
    def __init__(self, data, next=None):
        # Almacena los datos y el puntero al siguiente nodo
        self.data = data
        self.next = next
        
if __name__ == '__main__':
    head = None # Inicialmente , la lista esta vacia (head es None)
    
    # Agregar nodos a la lista en un bucle
    for i in range(5, 0, -1): # Se crearan nodos con los valores 5, 4, 3, 2, 1
        head = Node(i, head) # El nuevo nodo apunta al nodo anterior (head)
        
    # Recorre la lista e imprimir los valores
    current = head
    
    while current is not None: # Mientras haya nodos en la lista
        print(current.data) # Imprime el valor del nodo actual
        current = current.next # Avanza al siguiente nodo
        
### NUEVO EJERCICIO DE EJEMPLO CON LIST COMPREHENSIONS
        
    new_head = None
    
    # new_head = [Node(i, new_head) for i in range(1,21)]
    #  basicamente no se puede hacer una estructura de datos de esta naturaleza con listas
    #   ya que no tiene concepto de "de nodo siguiente"
    
    # Construir una nueva lista enlazada usando un bucle convencional
    for i in range(20, 0, -1): # Construir la lista enlazada con valores del 20 al 0, parando en 1
        new_head = Node(i, new_head)
    
    new_current = new_head
    
    # Recorrer e imprimir la nueva lista enlazada
    while new_current is not None:
        print(new_current.data)
        new_current = new_current.next