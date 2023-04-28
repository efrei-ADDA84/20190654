import requests
import os

# Set environment variables
latitude=os.environ['LAT']
longitude=os.environ['LONG']
YOUR_API_KEY=os.environ['API_KEY']

def get_weather(latitude,longitude,YOUR_API_KEY):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={YOUR_API_KEY}&units=metric"
    response = requests.get(url)
    print(response.json())


get_weather(latitude,longitude,YOUR_API_KEY)
