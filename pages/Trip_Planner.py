import streamlit as st
import json
import os
from components import navbar, footer

st.set_page_config(page_title="Trip Planner", layout="wide")
navbar.render()

st.title("📝 Plan Your Trip")
st.markdown("Fill in your travel details and let us help you save your dream trip.")

with st.form("planner_form"):
    name = st.text_input("Your Name")
    destination = st.text_input("Destination")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    budget = st.number_input("Budget (USD)", min_value=100.0)
    accommodation = st.selectbox("Accommodation Type", ["Hotel", "Hostel", "Apartment", "Other"])
    notes = st.text_area("Additional Notes")
    save_btn = st.form_submit_button("Save Trip")

if save_btn:
    trip = {
        "name": name,
        "destination": destination,
        "start_date": str(start_date),
        "end_date": str(end_date),
        "budget": budget,
        "accommodation": accommodation,
        "notes": notes
    }
    os.makedirs("data", exist_ok=True)
    with open("data/trips.json", "a") as f:
        json.dump(trip, f)
        f.write("\n")
    st.success("✅ Trip saved successfully!")

footer.render()
