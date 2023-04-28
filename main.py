
import requests
import os

# Set environment variables
os.environ['LAT']
os.environ['LONG']
os.environ['API_KEY'] = "14c52ccb6470e53bd70d27f06e1b5841"

def get_weather(LAT,LONG,API_KEY):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    print(response.json())


get_weather(LAT,LONG,API_KEY)