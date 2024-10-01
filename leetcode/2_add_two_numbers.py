#Suma de dos números representados por listas enlazadas

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Creamos un nodo dummy para facilitar la construcción de la lista resultante
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Iteramos mientras haya nodos en alguna de las listas o un acarreo
        while l1 or l2 or carry:
            # Obtenemos los valores de los nodos actuales (0 si no hay nodo)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculamos la suma y el nuevo acarreo
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Creamos un nuevo nodo con el dígito calculado
            current.next = ListNode(digit)
            current = current.next
            
            # Avanzamos en las listas de entrada
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        # Devolvemos la lista resultante (sin el nodo dummy)
        return dummy.next

# Función auxiliar para crear una lista enlazada a partir de una lista de Python
def createLinkedList(nums):
    dummy = ListNode(0)
    current = dummy
    for num in nums:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Función auxiliar para convertir una lista enlazada a una lista de Python
def linkedListToList(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Ejemplos de uso
solution = Solution()

# Ejemplo 1
l1 = createLinkedList([2,4,3])
l2 = createLinkedList([5,6,4])
result = solution.addTwoNumbers(l1, l2)
print("Ejemplo 1:", linkedListToList(result))  # Debería imprimir [7,0,8]

# Ejemplo 2
l1 = createLinkedList([0])
l2 = createLinkedList([0])
result = solution.addTwoNumbers(l1, l2)
print("Ejemplo 2:", linkedListToList(result))  # Debería imprimir [0]

# Ejemplo 3
l1 = createLinkedList([9,9,9,9,9,9,9])
l2 = createLinkedList([9,9,9,9])
result = solution.addTwoNumbers(l1, l2)
print("Ejemplo 3:", linkedListToList(result))  # Debería imprimir [8,9,9,9,0,0,0,1]