# AI-Powered Itinerary Generator (Updated)
import streamlit as st
from utils.ai_core import generate_recommendation
import datetime

st.set_page_config(page_title="AI-Powered Itinerary", layout="wide")
st.title("🧠 AI-Powered Itinerary Planner")
st.markdown("Plan a multi-day trip using the power of AI.")

with st.form("itinerary_form"):
    destination = st.text_input("Where do you want to go?")
    days = st.number_input("How many days?", min_value=1, max_value=30, value=3)
    interests = st.text_area("What are your interests (e.g. food, nature, museums)?")
    start_date = st.date_input("Start Date", datetime.date.today())
    submitted = st.form_submit_button("Generate Itinerary")

if submitted:
    with st.spinner("Generating itinerary with AI..."):
        itinerary = generate_recommendation(destination, days, interests)

    st.success("Here's your AI-generated trip plan:")
    st.markdown("---")
    for day, events in itinerary.items():
        st.subheader(f"📅 {day}")
        for event in events:
            st.markdown(f"- 🎯 {event}")

    if st.button("💾 Save this Trip"):
        with open("trip_data.txt", "a", encoding="utf-8") as f:
            f.write(f"Destination: {destination}\n")
            f.write(f"Days: {days}\n")
            f.write(f"Interests: {interests}\n")
            f.write("\nAI Trip Itinerary:\n")
            for day, events in itinerary.items():
                f.write(f"{day}:\n")
                for event in events:
                    f.write(f"- {event}\n")
            f.write("\n---\n")
        st.success("Trip saved to trip_data.txt ✅")
