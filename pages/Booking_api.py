import streamlit as st

st.title("📦 Booking Status & History")

st.info("This is where your bookings and confirmations will appear once integrated with a real API.")

# Simulate a sample booking
sample_booking = {
    "Origin": "Johannesburg",
    "Destination": "Cape Town",
    "Status": "Confirmed",
    "Departure": "2025-08-10",
    "Return": "2025-08-20"
}

st.subheader("Your Latest Booking")
st.json(sample_booking)
