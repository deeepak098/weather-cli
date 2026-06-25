import streamlit as st
from weather import get_weather
from datetime import datetime

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Weather Dashboard",
    page_icon="🌤",
    layout="wide"
)

# -----------------------------
# LOAD CSS
# -----------------------------
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.markdown(
    "<div class='title'>🌤 Weather Dashboard</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Real-Time Weather Powered by OpenWeatherMap API</div>",
    unsafe_allow_html=True
)

st.write("")

# -----------------------------
# SEARCH BAR
# -----------------------------
col1, col2 = st.columns([4,1])

with col1:
    city = st.text_input(
        "",
        placeholder="Enter City Name..."
    )

with col2:
    search = st.button("Search")

# -----------------------------
# WEATHER
# -----------------------------
if search:

    data = get_weather(city)

    if data is None:
        st.error("City not found or API error.")
        st.stop()

    # -----------------------------
    # DATA
    # -----------------------------

    city_name = data["name"]
    country = data["sys"]["country"]

    temp = round(data["main"]["temp"])

    feels = round(data["main"]["feels_like"])

    humidity = data["main"]["humidity"]

    pressure = data["main"]["pressure"]

    visibility = data["visibility"] // 1000

    wind = data["wind"]["speed"]

    description = data["weather"][0]["description"].title()

    icon = data["weather"][0]["icon"]

    sunrise = datetime.fromtimestamp(
        data["sys"]["sunrise"]
    ).strftime("%I:%M %p")

    sunset = datetime.fromtimestamp(
        data["sys"]["sunset"]
    ).strftime("%I:%M %p")

    icon_url = (
        f"https://openweathermap.org/img/wn/{icon}@4x.png"
    )

    # -----------------------------
    # HERO CARD
    # -----------------------------

    st.markdown("<div class='glass'>", unsafe_allow_html=True)

    st.markdown(
        f"""
        <div style="text-align:center;">
            <img src="{icon_url}" width="150">
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<div class='temp'>{temp}°C</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<div class='city'>{city_name}, {country}</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<div class='desc'>{description}</div>",
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # -----------------------------
    # ROW 1
    # -----------------------------

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(
            f"""
            <div class="metric">
                <div class="metric-value">💧 {humidity}%</div>
                <div class="metric-label">Humidity</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric">
                <div class="metric-value">🌡 {feels}°C</div>
                <div class="metric-label">Feels Like</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            f"""
            <div class="metric">
                <div class="metric-value">🌬 {wind} m/s</div>
                <div class="metric-label">Wind Speed</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    # -----------------------------
    # ROW 2
    # -----------------------------

    c4, c5, c6 = st.columns(3)

    with c4:
        st.markdown(
            f"""
            <div class="metric">
                <div class="metric-value">📈 {pressure}</div>
                <div class="metric-label">Pressure</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c5:
        st.markdown(
            f"""
            <div class="metric">
                <div class="metric-value">👁 {visibility} km</div>
                <div class="metric-label">Visibility</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c6:
        st.markdown(
            f"""
            <div class="metric">
                <div class="metric-value">🌅 {sunrise}</div>
                <div class="metric-label">Sunrise</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")

    st.caption(
        "Made with ❤️ using Python, Streamlit & OpenWeatherMap API"
    )