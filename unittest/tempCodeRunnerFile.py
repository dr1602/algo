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