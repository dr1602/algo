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