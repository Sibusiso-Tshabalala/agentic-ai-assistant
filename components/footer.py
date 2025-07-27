import streamlit as st

def render():
    st.markdown("""
        <hr style='margin-top:2rem;margin-bottom:1rem;'>
        <div style='text-align: center; color: gray;'>
            ⓒ 2025 Agentic Travel AI Planner | Built with ❤️ using Streamlit and OpenAI
        </div>
    """, unsafe_allow_html=True)
