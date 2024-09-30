# Ejemplo 3: funcion para verificar si una cadena es un palindromo

import unittest

def is_palindrome(s):
    return s == s[::-1]

class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome('radar'))
        self.assertFalse(is_palindrome('python'))
        
if __name__ == '__main__':
    unittest.main()

'''
odeRunnerFile.py"
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
'''

'''
assertTrue: Verifica si un valor es verdadero
assertFalse: Verifica si un valor es falso

Ejecutando las pruebas

Para ejecutar estas pruebas, guarda el codigo en un archivo y ejecuta 
en terminal

python test_example.py
'''