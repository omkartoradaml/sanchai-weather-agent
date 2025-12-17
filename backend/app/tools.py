import os
import requests
from langchain.tools import Tool


def _get_weather(city: str) -> str:
    """
    Fetch current weather for a given city using OpenWeatherMap API.
    """
    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        return "Weather API key is missing."

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return f"Could not fetch weather for {city}. Please check the city name."

    data = response.json()
    temp = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return f"The current temperature in {city} is {temp}°C with {description}."


# LangChain Tool definition
weather_tool = Tool(
    name="get_weather",
    func=_get_weather,
    description="Use this tool to get the current weather of a city"
)
