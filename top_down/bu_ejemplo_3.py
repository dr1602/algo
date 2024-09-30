# Minimum Coin Change

# Bottom-up (iterative)

def min_coin_change_bottom_up(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        print(f'these are the coins {coin}')
        print(f'dp_coin: {dp}')
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
            # print(f'these are the is {i}')
            print(f'dp_i: {dp}')
            
    return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == '__main__':
    
    monedas = [1, 5, 10, 25] # Denominaciones de monedas disponibles
    cantidad = 12 # Cantidad para la que queremos encontrar el cambio minimo
    
    test = min_coin_change_bottom_up(monedas, cantidad)
    print(test)
    print(f'El numero minimo de monedas para {cantidad} es: {test}')
    
'''
these are the coins 1
dp_coin: [0, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
dp_i: [0, 1, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
dp_i: [0, 1, 2, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
dp_i: [0, 1, 2, 3, inf, inf, inf, inf, inf, inf, inf, inf, inf]
dp_i: [0, 1, 2, 3, 4, inf, inf, inf, inf, inf, inf, inf, inf]
dp_i: [0, 1, 2, 3, 4, 5, inf, inf, inf, inf, inf, inf, inf]
dp_i: [0, 1, 2, 3, 4, 5, 6, inf, inf, inf, inf, inf, inf]
dp_i: [0, 1, 2, 3, 4, 5, 6, 7, inf, inf, inf, inf, inf]
dp_i: [0, 1, 2, 3, 4, 5, 6, 7, 8, inf, inf, inf, inf]
dp_i: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, inf, inf, inf]
dp_i: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, inf, inf]
dp_i: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, inf]
dp_i: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
these are the coins 5
dp_coin: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
dp_i: [0, 1, 2, 3, 4, 1, 6, 7, 8, 9, 10, 11, 12]
dp_i: [0, 1, 2, 3, 4, 1, 2, 7, 8, 9, 10, 11, 12]
dp_i: [0, 1, 2, 3, 4, 1, 2, 3, 8, 9, 10, 11, 12]
dp_i: [0, 1, 2, 3, 4, 1, 2, 3, 4, 9, 10, 11, 12]
dp_i: [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 10, 11, 12]
dp_i: [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 11, 12]
dp_i: [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 12]
dp_i: [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4]
these are the coins 10
dp_coin: [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 2, 3, 4]
dp_i: [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 3, 4]
dp_i: [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 4]
dp_i: [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3]
these are the coins 25
dp_coin: [0, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3]
3
El numero minimo de monedas para 12 es: 3
'''

'''
Explicacion:

1. Función min_coin_change_bottom_up:
coins: Una lista que contiene las denominaciones de las monedas disponibles (por ejemplo, 
[1, 5, 10, 25]).
amount: La cantidad total que queremos alcanzar con el menor número de monedas.

2. dp = [float('inf')] * (amount + 1):
Se crea una lista dp (dynamic programming) de tamaño amount + 1, donde cada elemento 
dp[i] representará el número mínimo de monedas necesarias para formar la cantidad i. 
Inicialmente, todos los valores se establecen en infinito para indicar que aún no se ha 
encontrado una solución.

3. dp[0] = 0:
El valor inicial dp[0] se establece en 0, ya que no se necesitan monedas para formar 
la cantidad 0.

4. Doble bucle:
Bucle externo: Itera sobre cada denominación de moneda en coins.
Bucle interno: Itera sobre todas las cantidades posibles desde la denominación de la
moneda actual hasta la cantidad total amount.

5. dp[i] = min(dp[i], dp[i - coin] + 1):
Para cada cantidad i, se calcula el mínimo entre el valor actual en dp[i] 
y el valor de usar una moneda de la denominación actual (coin) más el número 
mínimo de monedas necesarias para formar la cantidad restante (i - coin).
Esto significa que se está considerando si es mejor usar la moneda actual o
no para formar la cantidad i.

6. return dp[amount]:
Al final, se devuelve el valor en dp[amount], que representa el número mínimo de
monedas necesarias para formar la cantidad total.


'''