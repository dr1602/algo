'''
Ejemplo 10: Creacion de una cadena de nodos
'''

class Node:
    def __init__(self, data, next=None):
        # El argumento 'next' se usa para apuntar al siguiente nodo, por defecto es None
        self.data = data
        self.next = next

if __name__ == '__main__':
    # Creamos nodos independientes
    node_1 = Node('Node 1') # Primer nodo, no apunta a ningun otro (next=None por defecto)
    node_2 = Node('Node 2') # Segundo nodo, sin apuntar a otro
    
    # Enlazamos los nodos manualmente
    node_1.next = node_2 # El nodo 1 ahora apunta al nodo 2
    
    # Imprimimos el dato del nodo 1
    print(node_1.data) # Salida: 'Node 1'
    
    '''
    Node 1
    '''
    
    # Verificamos a que nodo apunta node_1
    print(node_1.next.data) # Salida: 'Node 2', ya que node_1.next apunta a node_2
    
    '''
    Node 2
    '''
    
    # Creamos un tercer nodo que apunta al nodo 1
    node_3 = Node(3, node_1)
    
    # Ahora, node_# apunta a node_1, que a su vez apunta a node_2
    print(node_3.next.data) # Salida: 'Node 1', ya que node_3.next apunta a node_1
    
    '''
    Node 1
    '''