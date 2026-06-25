import requests

API_KEY = "e1a7c74ecc06680a0f1da029d255619e"


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