import streamlit as st

def render():
    st.markdown("""
        <style>
        .navbar {
            background-color: #f0f2f6;
            padding: 1rem;
            border-bottom: 2px solid #ccc;
        }
        .navbar h1 {
            color: #0066cc;
            font-size: 1.8rem;
        }
        </style>
        <div class="navbar">
            <h1>🌍 Agentic Travel Planner</h1>
        </div>
    """, unsafe_allow_html=True)
