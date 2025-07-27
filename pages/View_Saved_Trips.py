import streamlit as st
import json
import os
from components import navbar, footer

st.set_page_config(page_title="Saved Trips", layout="wide")
navbar.render()

st.title("🗂️ View Your Saved Trips")

trip_file = "data/saved_trips.json"

if os.path.exists(trip_file):
    with open(trip_file, "r") as f:
        trips = json.load(f)

    if trips:
        for idx, trip in enumerate(trips, 1):
            st.subheader(f"Trip #{idx}: {trip['destination']}")
            st.write(f"**Start Date:** {trip['start_date']}")
            st.write(f"**End Date:** {trip['end_date']}")
            st.write(f"**Budget:** R{trip['budget']}")
            st.write(f"**Activities:** {trip['activities']}")
            st.markdown("---")
    else:
        st.info("No saved trips found.")
else:
    st.warning("Trip data file not found.")

footer.render()
