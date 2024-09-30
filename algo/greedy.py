# Example: Coin Change Problem

def gredy_coin_change(coins, amount):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            result.append(coin)
            amount -= coin
    
    return result

if __name__ == '__main__':
    coins = [1, 2, 5, 10]
    amount = 11
    
    test = gredy_coin_change(coins, amount)
    print(test)
    # [10, 1]