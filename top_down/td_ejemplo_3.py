# Top - down (recursive with memoization)

def min_coin_change_top_down(coins, amount, memo={}):
    if amount == 0:
        return 0
    if amount in memo:
        return memo[amount]
    min_coins = float('inf')
    for coin in coins:
        if amount >= coin:
            min_coins = min(min_coins, min_coin_change_top_down(coins, amount - coin, memo) + 1)
    memo[amount] = min_coins
    return min_coins
    
'''
Explanation:
1. Uses memoization to avoid reduntant calculations
2. Recursively calculates the minimum number of coins for each amount.

'''

if __name__ == '__main__':
    
    monedas = [1, 5, 10, 25] # Denominaciones de monedas disponibles
    cantidad = 12 # Cantidad para la que queremos encontrar el cambio minimo
    
    test = min_coin_change_top_down(monedas, cantidad)
    print(test)
    print(f'El numero minimo de monedas para {cantidad} es: {test}')