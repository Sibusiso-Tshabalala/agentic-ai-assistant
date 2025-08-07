import streamlit as st
from utils.book_api import book_trip

st.set_page_config(page_title="Booking Assistant", layout="wide")
st.title("🛎️ AI Booking Assistant")
st.markdown("Book your trip directly with the help of AI.")

with st.form("booking_form"):
    name = st.text_input("Your Full Name")
    destination = st.text_input("Destination")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    budget = st.number_input("Budget (ZAR)", min_value=1000, step=500)
    preference = st.selectbox("Preferred Booking Type", ["Flight", "Hotel", "Activity", "Package"])
    submitted = st.form_submit_button("Search & Book")

if submitted:
    with st.spinner("Contacting booking APIs..."):
        confirmation = book_trip(name, destination, start_date, end_date, budget, preference)

    if confirmation:
        st.success("🎉 Booking confirmed!")
        st.write(confirmation)
    else:
        st.error("❌ Booking failed. Please try again or modify your preferences.")
