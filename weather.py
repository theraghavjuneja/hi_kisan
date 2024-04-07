import requests
import json
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("OPEN_WEATHER_API")

def fetch_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data from API. Status code: {response.status_code}")
        return None

def timestamp_to_datetime(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')


def display_tabular(data):

    print("Date and Time\t\tTemperature (°C)\tHumidity (%)\tWeather Description")
    
   
    for item in data['list']:

        timestamp = timestamp_to_datetime(item['dt'])
        temperature = item['main']['temp']
        humidity = item['main'].get('humidity', '-')
        weather_description = item['weather'][0]['description']
        
        print(f"{timestamp}\t{temperature:.2f}\t\t\t{humidity}\t\t{weather_description}")

# Example usage
api_url = f'http://api.openweathermap.org/data/2.5/forecast?q=New York&appId={API_KEY}'
data = fetch_data_from_api(api_url)
if data:
    display_tabular(data)
