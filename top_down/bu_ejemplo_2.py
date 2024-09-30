# Factorial

# Bottom-up (iterative)

def factorial_bottom_up(n):
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
        print(f'aqui va {result}')
    
    return result

if __name__ == '__main__':
    factorial = factorial_bottom_up(4)
    print(factorial)
    
'''
Resultado:
aqui va 1
aqui va 2
aqui va 6
aqui va 24
24

Explanation:
1. Starts with the base case (0! = 1)
2. Iteratively multiplies the result by each number from 1 to n

'''