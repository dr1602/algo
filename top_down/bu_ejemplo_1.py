# xamples of algorithms in Python, explained using both bottom-up and top-down approaches

# Fibonacci Sequence

def fibonacci_bottom_up(n):
    if n <= 1:
        return n
    fib = [0, 1]
    for i in range (2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
        print(f'hasta aqui va {fib}')
    return fib[n]

test = fibonacci_bottom_up(6)

'''
Explanation:
1. Starts with the base case (0 and 1)
2. Iteratively calculates the next Fibonacci number usin the previous two
3. Return nth Fibonacci number

'''

'''
Resultado

hasta aqui va [0, 1, 1]
hasta aqui va [0, 1, 1, 2]
hasta aqui va [0, 1, 1, 2, 3]
hasta aqui va [0, 1, 1, 2, 3, 5]
hasta aqui va [0, 1, 1, 2, 3, 5, 8]
'''