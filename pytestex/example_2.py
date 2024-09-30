# Ejemplo 2: Funcion que verifica si una cadena es un palindromo

def is_palindrome(s):
    return s == s[::-1]

def test_is_palindrome():
    assert is_palindrome('radar') == True
    assert is_palindrome('python') == False
    assert is_palindrome('') == True # Cadena vacia
    assert is_palindrome('A man, a plan, a canal: Panama') == True # Ignora espacios y puntuacion
    
'''
Palíndromo: Se verifica que "radar" sea un palíndromo.
No palíndromo: Se verifica que "python" no sea un palíndromo.
Cadena vacía: Se verifica que una cadena vacía sea un palíndromo.
Caso con espacios y puntuación: Se verifica un palíndromo con espacios y puntuación, 
mostrando que la función ignora estos caracteres.


==================================== test session starts =====================================
platform linux -- Python 3.10.12, pytest-8.3.3, pluggy-1.5.0
rootdir: /root/algo/pytestex
plugins: anyio-4.4.0
collected 1 item                                                                             

example_2.py F                                                                         [100%]

========================================== FAILURES ==========================================
_____________________________________ test_is_palindrome _____________________________________

    def test_is_palindrome():
        assert is_palindrome('radar') == True
        assert is_palindrome('python') == False
        assert is_palindrome('') == True # Cadena vacia
>       assert is_palindrome('A man, a plan, a canal: Panama') == True # Ignora espacios y puntuacion
E       AssertionError: assert False == True
E        +  where False = is_palindrome('A man, a plan, a canal: Panama')

example_2.py:10: AssertionError
================================== short test summary info ===================================
FAILED example_2.py::test_is_palindrome - AssertionError: assert False == True
===================================== 1 failed in 0.09s ======================================
'''