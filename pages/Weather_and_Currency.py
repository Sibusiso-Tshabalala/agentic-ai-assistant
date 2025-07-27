import streamlit as st
import requests
from components import navbar, footer

st.set_page_config(page_title="Weather & Currency Info", layout="wide")
navbar.render()

st.title("🌤️ Real-time Weather & 💱 Currency Info")
st.write("Get up-to-date information about your destination.")

city = st.text_input("Enter city for weather:")

if city:
    weather_api = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": -33.9249,
        "longitude": 18.4241,
        "current_weather": True
    }
    # Replace hardcoded coords with a geocoding lookup if desired

    res = requests.get(weather_api, params=weather_params)
    if res.status_code == 200:
        data = res.json()
        current = data.get("current_weather", {})
        st.info(f"**Temperature:** {current.get('temperature', 'N/A')}°C | **Windspeed:** {current.get('windspeed', 'N/A')} km/h")
    else:
        st.error("Could not fetch weather.")

st.markdown("---")

currency_code = st.text_input("Enter currency code (e.g., USD, EUR, ZAR):")

if currency_code:
    try:
        response = requests.get(f"https://api.exchangerate.host/latest?base={currency_code.upper()}")
        data = response.json()
        rates = data.get("rates", {})
        st.write(f"**{currency_code.upper()}** exchange rates:")
        st.json(rates)
    except:
        st.error("Error fetching currency info.")

footer.render()
