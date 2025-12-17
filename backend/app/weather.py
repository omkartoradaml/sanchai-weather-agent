import os
import requests


def get_weather(city: str):
    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        return {"error": "WEATHER_API_KEY not set"}

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return {"error": f"Weather not found for {city}"}

    data = response.json()

    return {
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["main"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],
    }

