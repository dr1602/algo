# Ejemplo 1: Funcion que calcula el factorial de un numero

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120 
    # assert factorial(-1) == 1 # Caso limite: factorial de un numero negativo
    
'''
Caso base: Se verifica que el factorial de 0 sea 1.
Caso típico: Se verifica que el factorial de 5 sea 120.
Caso límite: Se verifica el comportamiento para un número negativo 
(en este caso, se devuelve 1 arbitrariamente, pero podría lanzar una excepción).

assert: La palabra clave assert verifica si una condición es verdadera. Si es falsa, 
se lanza una excepción AssertionError.
'''

'''
Test result:

==================================== test session starts =====================================
platform linux -- Python 3.10.12, pytest-8.3.3, pluggy-1.5.0
rootdir: /root/algo/pytestex
plugins: anyio-4.4.0
collected 1 item                                                                             

example_1.py .                                                                         [100%]


'''