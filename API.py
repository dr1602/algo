import requests

# URL de la API con el endpoint y el parametro de ciudad
api_url = 'http://api.openweathermap.org/data/2.5/weather?q=Mexico&appid=tu_api_key'

# Realizar la solicitud GET
response = requests.get(api_url)

# Verificar si la respuesta es existosa
if response.status_code == 200:
    # Parsear las respuestas en formato JSON
    data = response.json()
    print(f"El clima actual en Mexico: {data['weather'][0]['description']}")
else:
    print('Error al obtener los datos del clima')

'''
Error al obtener los datos del clima
'''

import requests

def get_stock_data():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo'
    response = requests.get(url)
    
    # Check if the response is succesful
    if response.status_code == 200:
        data = response.json()
        last_refreshed = data['Meta Data']['3. Last Refreshed']
        price = data['Time Series (5min)'][last_refreshed]['1. open']
        return price
    else:
        return None
    
stock_prices = {}
price = get_stock_data()
symbol = 'MSF'

if price is not None:
    stock_prices[symbol] = price
    
print(f'{symbol}: {price}')

'''
IBM: 223.5700

MSF: 223.5700
'''
        
    
