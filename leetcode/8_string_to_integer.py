# 8. String to integer (atoi)

'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit singed integer.

The algorithm for myAtoi(string s) is as follows:

1. Whitespace: Ignore any leading whitespace('')
2. Signedness: Determine the sign by checking if the next character is '-' or '+', assuming
positivity is neither present.
3. Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered
or the end of the string is reached. If no digits were read, then the result is 0.
4. Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer
to remain in the range. Specifically, integers less than -2^31 should be rounded to -2^31, and integers
greater than 2^31 - 1 should be rounded to 2^31 - 1.

Return the integer as the final result.

Example 1:

    Input: s = '42'
    Output: 42

    Explanation:

    The underlined characters are what is read in and the caret is the current reader position.
    
    Step 1: '42' (no characters read because there is no leading whitespcae)

    Step 2: '42' (no characters read because there is neither a '-' nor '+')

    Step 3: '42' ('42' is read in)

Example 2:

    Input: s = ' -042'
    Output: -42

    Explanation:

    Step 1: "   -042" (leading whitespace is read and ignored)
            
    Step 2: "   -042" ('-' is read, so the result should be negative)
             
    Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)

Example 3:

    Input: s = '1337c0d3'
    Output: 1332

    Explanation:

    Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
         
    Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
            
    Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)

Example 4:

    Input: s = '0-1'
    Output: 0

    Explanation:

    Step 1: "0-1" (no characters read because there is no leading whitespace)
         
    Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
            
    Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)

Example 4:

    Input: s = 'words and 987'
    Output: 0

    Explanation:

    Reading stops at the first non-digit character 'w'.

Constrains:

0 <= s.length <= 200

s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

'''

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Define constants for 32-bit integer bounds
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Intialie variables
        result = 0
        sign = 1
        i = 0
        n = len(s)

        # Step 1: Skyp leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        # Handle empy string or only whitespace
        if i == n:
            return 0
        
        # Step 2: Check for sign
        if s[i] in ['-', '+']:
            sign = -1 if s[i] == '-' else 1
            i += 1

        # Step 3: Convert digits
        while i < n and s[i].isdigit():
            digit = int(s[i])

            # Check for overflow before multiplying
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1

        # Apply sign and return
        result *= sign

        # Step 4: Handle bounds
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        
        return result



## Thought Process

'''
Se pasan por 3 validaciones en el orden mencionado:
a. Se revisa que hay o no espacios en blanco antes del numero y se ignora
b. Si revisa el siguiente caracter, si es igual a - o + se considera para el signo
c. Se procede a validar los siguientes elementos del array hasta terminarlo hasta llegar a un valor distinto
a [0,1,2,3,4,5,6,7,8,9]

Pienso que primero tienes que convertir al string en array, y probablemente tener un array secundario para
almancenar los valores y luego convertirlos a numeros.

Tambien debe de haber un condicional que almacene si el valor sera positivo o negativo.

Retornas el array convertido en numero

'''

## Posible respuesta

def myAtoi(s):
    is_negative
    iterable = [0, 1, 2, 3, 4, 5, 6, 7, 9]

    new_s = s.lstrip()
    result_s
    n = len(new_s)

    if new_s[0] == '-':
        is_negative=True

    for i in new_s:
        if i in iterable:
            result_s = int(i * (10 ** n))
            n-1
        else:
            result_s = int(result_s)/10
        return result_s

            
test_2 = 'si'
myAtoi(test_2)


'''

test = '    hola'
test_3 = 'como estas'

print(test[0])
# h

print(test_3 + test.lstrip())
# como estashola

'''