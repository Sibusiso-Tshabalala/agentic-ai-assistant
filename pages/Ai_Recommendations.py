import streamlit as st
from utils.ai_core import generate_recommendation
from components import navbar, footer

st.set_page_config(page_title="AI Travel Recommendations", layout="wide")
navbar.render()

st.title("🧠 Smart Travel Recommendations")
st.markdown("Get personalized suggestions using AI. Just enter your travel preferences below!")

with st.form("ai_form"):
    user_prompt = st.text_area("Describe your dream destination, interests, or type of vacation:",
                               "e.g., I want a beach vacation with warm weather and vibrant nightlife")
    submitted = st.form_submit_button("Get AI Recommendation")

if submitted and user_prompt:
    with st.spinner("Thinking..."):
        result = generate_recommendation(user_prompt)
        st.success("Here is what AI suggests:")
        st.markdown(f"""
        <div style='background-color:#f9f9f9; padding: 1rem; border-left: 5px solid #00aaff;'>
            {result}
        </div>
        """, unsafe_allow_html=True)

footer.render()
