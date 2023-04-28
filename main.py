import requests
import os
from fastapi import FastAPI

app = FastAPI()

# Set environment variables


YOUR_API_KEY=os.environ['API_KEY']

@app.get("/")
async def get_weather(lat,lon):

    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={YOUR_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Cannot find the location."}
    return response.json()




