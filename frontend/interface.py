import streamlit as st
from PIL import Image
import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.langgraph_flow import build_workflow



# 🎨 Page Config
st.set_page_config(page_title="Agentic Travel Planner", page_icon="🧳", layout="centered")

# 🖼️ Custom Header
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        color: #2E86AB;
        padding-bottom: 0.5em;
    }
    .sub-text {
        text-align: center;
        color: #555;
        font-size: 1.1em;
        margin-top: -10px;
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #2E86AB;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6em 2em;
        font-size: 1.1em;
        margin-top: 1em;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">✈️ Agentic AI Travel Planner</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Plan your flights, hotels, and itinerary using AI. Just type your request below!</div>', unsafe_allow_html=True)

# 🧠 Input Form
with st.form("trip_form"):
    user_input = st.text_area("📝 Describe your trip", "Book me a trip from JHB to CPT next Friday, back Sunday", height=100)
    submitted = st.form_submit_button("🚀 Plan My Trip")

# ⚙️ Workflow Engine
if submitted and user_input:
    st.info("🧠 Interpreting your request and building your trip...")
    with st.spinner("Please wait while we contact agents..."):
        graph = build_workflow()
        result = graph.run(user_input)

    # ✅ Display Results
    if result.get("status") == "error":
        st.error(result.get("message"))
    else:
        st.success("✅ Trip successfully planned!")

        # 🛫 Flight
        flight = result.get("flight_details")
        if flight:
            st.subheader("🛫 Flight Booking")
            st.json(flight)

        # 🏨 Hotel
        hotel = result.get("hotel_details")
        if hotel:
            st.subheader("🏨 Hotel Booking")
            st.write(f"**Hotel:** {hotel['name']}  \n**Stars:** {hotel['stars']} ⭐")

        # 📅 Calendar
        event = result.get("calendar_event")
        if event:
            st.subheader("📅 Calendar Event")
            st.code(event, language="text")

        st.caption("Need changes? Just edit the request above and re-run.")

# 💡 Footer
st.markdown("""
    <hr style="margin-top: 40px;">
    <center>
        <small>Crafted with ❤️ by your Agentic AI Assistant • Powered by OpenAI & LangGraph</small>
    </center>
""", unsafe_allow_html=True)
