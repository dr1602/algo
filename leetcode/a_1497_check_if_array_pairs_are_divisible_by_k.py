'''
1497. Check If Array Pairs Are Divisible by k

Given an array of integers 'arr' of even length 'n' and an integer 'k'.

We want to divide the array into exactly n/2 pairs such that the sum of each pair is divi-
sible by k.

Return 'true' if you cna find a way to do that or false otherwise.

Example 1:

    Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
    Output: true
    Explanation: Pairs are (1, 9), (2,8), (3,7), (4,6) and (5,10).

Example 2:

    Input: arr = [1,2,3,4,5,6], k = 7
    Output: true
    Explanation: Pairs are (1, 6), (2,5) and (3,4).
    
Example 3:

    Input: arr = [1,2,3,4,5,6], k = 10
    Output: false
    Explanation: You can try all possible pairs to see that there is no way to divide arr
    into 3 pairs each with sum divisible by 10.
    
Constraints:
    * arr.length == n
    * 1 <= n <= 10^5
    * n is even.
    * -10^9 <= arr[i] <= 10^9
    * 1 <= k <= 10^5
    
'''

### Trabajando la solucion ###

'''
Steps:

.... Check if the lenght of the arr is divisible by 2 -> n is even
.... Must all of the numbers be pairs that their addition is divisible to k? 
.... Can there be repeated numbers or are they all different?

Maybe I could use a divide and conquer approach! but instead of for sorting from the
smallest to the biggest, it could be made to find the pair that can be divided by k.

.... It must at least check each value (n) againts each other value in the array (n)
except for itself and the to validate if it is divisible by k... in the worst scenario
Probable Big O (Worst Case): On^n
Probable Big O (Best Case): On


'''

from collections import defaultdict
from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = defaultdict(int)
        
        for num in arr:
        # tomo un valor de array
            remainder = num % k
            # le asigna el valir a remainder del residuo de num / k
            freq[remainder] += 1
            # en el dict 'freq', en la posicion de remainder, se le asigna el valor 1
            # recuerda que a un valor le hace falta el valor almacenado para ser divisible entre k
            
        # esta operacion se repite para todo el array    
        
        
        for remainder in range(k):
        # por cada valor en un rango de 0 a k
            if remainder == 0:
                # si el remainder es igual a 0 sigues a la siguiente subcondicion
                if freq[remainder] % 2 != 0:
                    # si en el dictionario freq, dentro de la posicion remainder
                    ## si ese valor, su reciduo es diferente de 0 regresa falso
                    return False
            elif freq[remainder] != freq[k - remainder]:
                # por otro lado, si en el array 'freq' en la posicion remainder,
                ## si su valor es diferente al valor del array 'freq' en la posicion
                ### k - remainder
                return False
        
        return True
    
'''
This solution uses a greedy approach and makes use of a hash table data structure.

Explanation

    a. We use a hash table (default in Python) to count the frequency of remainders when each
    number in the array is divided by k.
    b. We iterate through the array once, calculating the remainder for each number and incrementing
    its count in the frequency table.
    c. Then, we check two conditions: 
        a. For remainder 0, its frequency must be even.
        b. For any other remainder r, its frequency must equal the frequency of k-r
    d. If all these conditions are met, we return True. Otherwise, we return False.
    
Time Complexity: 
    O(n), where n is the length of the array. We iterate through the array once to build the frequency
    table, and then we iterate through at most k entries in the frequency talbe.

Space Complexity:
    O(min(n,k)). In the worst case, we might have up to min(n, k) different remainders in our frequency
    table.
    
Data Structure: The main data structure used here is a hash table (dictionary in Python).

This solution uses a greedy approach because we're making locally optimal choices (pairing numbers with
complementary remainders) to arrive at a globally optimal solution.

Regarding the Big O notation:
a. Time complexity: O(n)
b. Space complexity: O(min(n,k))

This solution is efficient because it solves the problem in linear time without needing to sort
the array or use more complex algorithms. It takes advantage othe properties of modular arithmetic to
simplify the problem of finding pairs with a sum divisible by k.

The key insigut is that for two numbers a and b to have a sum divisible by k, (a % k + b % l) % must equal 0.
This allows us to reduce the problem to matching remainders, which we can do efficiently using a hash table.

'''

## Hash table

from collections import defaultdict

# Create a defaultdict with a default value of an empty list
my_dict = defaultdict(list)

# Add elements to the defaultdict
my_dict['fruits'].append('apple')
my_dict['vegetables'].append('carrot')

# Print the defaultdict
print(my_dict)

'''
defaultdict(<class 'list'>, {'fruits': ['apple'], 'vegetables': ['carrot']})
'''

'''
Modular Arithmetic: A Simplified Explanation
Modular arithmetic is a system of arithmetic where numbers "wrap around" after reaching a certain value, called the modulus. This is similar to how the hours on a clock wrap around from 12 to 1.   

Key Concepts:
Modulus: The maximum value before the numbers "wrap around."
Congruence: Two numbers are congruent modulo m if their difference is divisible by m. For example, 5 and 11 are congruent modulo 6 because their difference (11 - 5 = 6) is divisible by 6. We write this as 5 ≡ 11 (mod 6).
Basic Operations:
Addition: (a + b) mod m = ((a mod m) + (b mod m)) mod m
Subtraction: (a - b) mod m = ((a mod m) - (b mod m)) mod m
Multiplication: (a * b) mod m = ((a mod m) * (b mod m)) mod m   
Exponentiation: (a^b) mod m = ((a mod m)^b) mod m
Example:
Let's say we want to find 7^5 mod 11.

Calculate 7^5: 7 * 7 * 7 * 7 * 7 = 16807.
Calculate 16807 mod 11: 16807 % 11 = 2.
Therefore, 7^5 mod 11 is equal to 2.

Applications:
Modular arithmetic is used in various fields, including:

Cryptography: For encryption and decryption algorithms.
Number theory: For solving problems related to divisibility and prime numbers.
Computer science: For hashing functions, error detection codes, and random number generators.
Would you like to explore a specific application of modular arithmetic or learn more about its properties and theorems?


Fuentes y contenido relacionado

'''