# 🌤 Weather Dashboard

A modern and responsive Weather Dashboard built using **Python**, **Streamlit**, and the **OpenWeatherMap API**. The application allows users to search for any city and view real-time weather information with a clean and visually appealing interface.

---

## 📸 Preview

> Add a screenshot of your application here.

---

## ✨ Features

- 🌍 Search weather for any city worldwide
- 🌡 Current temperature
- 🤗 Feels like temperature
- 💧 Humidity
- 🌬 Wind speed
- 📈 Atmospheric pressure
- 👁 Visibility
- 🌅 Sunrise time
- ☀️ Official OpenWeatherMap weather icons
- 🎨 Modern glassmorphism UI
- 📱 Responsive Streamlit interface
- ⚠ Error handling for invalid cities and API failures

---

## 🛠 Tech Stack

- Python 3
- Streamlit
- Requests
- OpenWeatherMap API
- HTML & CSS (via Streamlit)

---

## 📂 Project Structure

```
Weather-Dashboard/
│
├── app.py              # Main Streamlit application
├── weather.py          # API handling logic
├── styles.css          # Custom UI styling
├── requirements.txt
│
└── assets/
```

---

## ⚙ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/weather-dashboard.git
```

Navigate into the project folder.

```bash
cd weather-dashboard
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip3 install -r requirements.txt
```

---

### 3. Get an OpenWeatherMap API Key

1. Create an account at

https://openweathermap.org/

2. Generate your API key.

3. Open `weather.py`

Replace

```python
API_KEY = "YOUR_API_KEY"
```

with

```python
API_KEY = "YOUR_API_KEY_HERE"
```

---

### 4. Run the application

```bash
streamlit run app.py
```

or

```bash
python3 -m streamlit run app.py
```

---

## 🚀 How It Works

1. User enters a city name.
2. Streamlit captures the input.
3. `weather.py` builds the OpenWeatherMap API URL.
4. A GET request is sent to the API.
5. The API returns weather data in JSON format.
6. The JSON response is parsed.
7. The dashboard extracts important weather information.
8. Streamlit displays the data using a modern user interface.

---

## 🔄 Workflow

```
User
   │
   ▼
Enter City
   │
   ▼
Streamlit UI
(app.py)
   │
   ▼
get_weather(city)
(weather.py)
   │
   ▼
OpenWeatherMap API
   │
   ▼
JSON Response
   │
   ▼
Extract Weather Information
   │
   ▼
Display Beautiful Dashboard
```

---

## 📡 API Used

**OpenWeatherMap Current Weather API**

Example Request

```
https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=YOUR_API_KEY&units=metric
```

Method

```
GET
```

Response Format

```
JSON
```

---

## 📚 Concepts Learned

This project demonstrates the following concepts:

- REST APIs
- HTTP Requests
- GET Requests
- JSON Parsing
- HTTP Status Codes
- API Authentication
- Python Functions
- Error Handling
- Modular Programming
- Streamlit UI Development
- CSS Styling

---

## 📌 Future Improvements

- 5-Day Weather Forecast
- Hourly Forecast
- Dynamic Weather Backgrounds
- Dark Mode
- Animated Weather Icons
- Air Quality Index
- UV Index
- Weather Maps
- Search History
- Favorite Cities
- GPS Location Support

---

## 👨‍💻 Author

**Deepak Saladi**

GitHub: https://github.com/deeepak098

---

## ⭐ If you like this project

Give it a ⭐ on GitHub if you found it useful.
