# Examples of algorithms in Python, explained using both bottom-up and top-down approaches

# Fibonacci Top-down (Recursive)

def fibonacci_top_down(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_top_down(n - 1, memo) + fibonacci_top_down(n - 2, memo)
    print(f'La iteracion va aqui {memo[n]}')
    return memo[n]

test = fibonacci_top_down(6)
print(test)

'''
Explanation:
1. Uses a memoization dictionary to store previously calculated results
2. if the result is already in the memo, it returns in directly
3. Otherwise, it calculates the result recursively and stores it in the memo

'''

'''
Resultado

La iteracion va aqui 1
La iteracion va aqui 2
La iteracion va aqui 3
La iteracion va aqui 5
La iteracion va aqui 8
8
'''