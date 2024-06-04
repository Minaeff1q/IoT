import requests
import json

def get_weather_data(latitude, longitude):
    # Open-Meteo API uses latitude and longitude for location
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        # Adjusting data structure according to Open-Meteo API response
        weather_data = {
            'city': 'Moscow',  # Open-Meteo API does not provide city name, so it's set as 'Unknown'
            'temperature': data['current_weather']['temperature'],  # Assuming temperature data exists
            'humidity': data['current_weather'].get('windspeed', 'N/A'),  # Assuming humidity data exists, else 'N/A'
        }
        return weather_data
    else:
        print(f"Error fetching data: {data.get('message', 'Unknown error')}")
        return None

def send_data_to_server(data):
    url = 'http://127.0.0.1:5000/data'
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        print("Data sent successfully")
    else:
        print(f"Failed to send data: {response.status_code}, {response.text}")

if __name__ == '__main__':
    # Replace with your desired location's latitude and longitude
    latitude = 55.7558  # Example latitude for Moscow
    longitude = 37.6173  # Example longitude for Moscow
    weather_data = get_weather_data(latitude, longitude)
    if weather_data:
        print(f"Collected data: {weather_data}")
        send_data_to_server(weather_data)
