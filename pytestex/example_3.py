# Ejemplo 3: Funcion que busca un elemento en una lista

def find_element(list, element):
    if element in list:
        return True
    else: 
        return False
    
def test_find_element():
    my_list = [1, 2, 3, 4]
    assert find_element(my_list, 3) == True
    assert find_element(my_list, 5) == False
    assert find_element([], 0) == False # Lista vacia
    
'''
Elemento encontrado: Se verifica que el elemento 3 se encuentre en la lista.
Elemento no encontrado: Se verifica que el elemento 5 no se encuentre en la lista.
Lista vacía: Se verifica que no se encuentre ningún elemento en una lista vacía.

Se hace testing con:

pytest example_3.py

==================================== test session starts =====================================
platform linux -- Python 3.10.12, pytest-8.3.3, pluggy-1.5.0
rootdir: /root/algo/pytestex
plugins: anyio-4.4.0
collected 1 item                                                                             

example_3.py .                                                                         [100%]

===================================== 1 passed in 0.02s ======================================
'''

