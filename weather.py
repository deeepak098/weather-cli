import requests

city = input("Enter city: ")

API_KEY = "e1a7c74ecc06680a0f1da029d255619e"

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q={city}"
    f"&appid={API_KEY}"
    f"&units=metric"
)

response = requests.get(url)

print("Status Code:", response.status_code)
print(response.json())