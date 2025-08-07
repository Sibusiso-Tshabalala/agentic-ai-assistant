from core.langgraph_flow import build_workflow

import streamlit as st
from components import navbar, footer

st.set_page_config(page_title="Agentic Travel Planner", layout="wide")
navbar.render()

st.title("✈️ Welcome to Agentic Travel Planner")
st.write("Plan your dream trip using AI! Use the sidebar to navigate to different pages.")
st.sidebar.header("📍 Navigate")
st.sidebar.page_link("pages/AI_Powered_Itinerary.py", label="AI-Powered Itinerary")
st.sidebar.page_link("pages/RealTime_Weather.py", label="🌤️ Real-Time Weather")
st.sidebar.page_link("pages/Booking_Assistant.py", label="🛎️ Booking Assistant")
st.sidebar.page_link("pages/View_Saved_Trips.py", label="🗂️ View Saved Trips")
footer.render()

if __name__ == "__main__":
    workflow = build_workflow()
    input_request = input("What do you want me to plan? ")
    result = workflow.run(input_request)
    print("🧠 Workflow Result:", result)
