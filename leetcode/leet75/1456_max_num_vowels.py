# Sliding

## 1456. Maximum Number of Vowels in a Substring of Given Length

'''
def maxVowels(s: str, k: int) -> int:
    # Conjunto de vocales
    vowels = set('aeiou')

    # Contador inicial de vocales en los primeros k caracteres
    max_vowels = 0
    current_vowels = 0

    # Contar vocales en la primera ventana de longitud k:
    for i in range(k):
        if s[i] in vowels:
            current_vowels += 1
    
    max_vowels = current_vowels

    # Deslizar la ventana por el resto de la cadena
    for i in range(k, len(s)):
        # Restar el caracter que sale de la ventana
        if s[i - k] in vowels:
            current_vowels -= 1
        
        # Sumer el nuevo caracter que entre en la ventana
        if s[i] in vowels:
            current_vowels += 1
        
        # Actualizar el maximo de vocales
        max_vowels = max(max_vowels, current_vowels)

    return max_vowels

'''