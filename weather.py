import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")



def get_weather(city):
    """
    Fetch current weather for a city from OpenWeatherMap.
    Returns JSON data if successful, otherwise returns None.
    """

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}"
        f"&appid={API_KEY}"
        "&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return response.json()

        return None

    except requests.exceptions.RequestException:
        return None