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