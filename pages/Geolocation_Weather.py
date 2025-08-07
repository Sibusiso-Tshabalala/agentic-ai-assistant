# 📄 pages/7_📍_Geolocation_Weather.py
import streamlit as st
import requests
from components import navbar, footer

st.set_page_config(page_title="Geolocation Weather", layout="wide")
navbar.render()

st.title("📍 Weather Based on Your Location")

st.write("Allow the browser to share your location for accurate weather updates.")

location = st.text_input("Enter your city or coordinates (latitude,longitude)", "Cape Town")

if location:
    try:
        if "," in location:
            lat, lon = location.split(",")
        else:
            geo_url = f"https://nominatim.openstreetmap.org/search?q={location}&format=json"
            geo_data = requests.get(geo_url).json()
            lat = geo_data[0]['lat']
            lon = geo_data[0]['lon']

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_data = requests.get(weather_url).json()
        current = weather_data['current_weather']

        st.subheader("🌤️ Current Weather")
        st.write(f"**Temperature:** {current['temperature']}°C")
        st.write(f"**Wind Speed:** {current['windspeed']} km/h")
        st.write(f"**Weather Code:** {current['weathercode']}")

    except Exception as e:
        st.error(f"Could not fetch weather info: {e}")

footer.render()
