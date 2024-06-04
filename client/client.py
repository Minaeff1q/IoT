import requests
import json
import time

def get_weather_data(latitude,longitude):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'
    response = requests.get(url)
    data = response.json()
    # Пример извлечения данных, нужно адаптировать под конкретный сайт
    temperature = data['current_weather']['temperature']
    windspeed = data['current_weather']['windspeed']
    city = 'Moscow'
    return {
        'temperature': temperature,
        'windspeed': windspeed,
        'city': city
    }

def send_data_to_server(data):
    url = 'http://172.19.0.2:5000/data'  # URL сервера
    # response = requests.post(url, json=data)
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print('Data sent successfully')
        else:
            print('Failed to send data')
    except requests.exceptions.RequestException as e:
        print(f'Failed to connect to server: {e}')

if __name__ == "__main__":
    while True:
        time.sleep(5)
        latitude = 55.7558  # Example latitude for Moscow
        longitude = 37.6173  # Example longitude for Moscow
        data = get_weather_data(latitude, longitude)
        send_data_to_server(data)