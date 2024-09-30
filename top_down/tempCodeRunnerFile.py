# Factorial

# Bottom-up (iterative)

def factorial_top_down(n):
    if n == 0:
        return 1
    print(f'vamos aqui {n}')
    return n * factorial_top_down(n - 1)

'''
Explanation:
1. Recursively calculates the factorial by multiplying n with the factorial of n - 1
2. It goes from top to bottom the number you input, with the relevant calculations
from the function

'''

if __name__ == '__main__':
    test = factorial_top_down(5)
    print(test)