import streamlit as st
from components import navbar, footer

st.set_page_config(page_title="Destination Gallery", layout="wide")
navbar.render()

st.title("🖼️ Explore Destinations")
st.markdown("Check out some amazing travel spots around the world.")

# Demo gallery
destinations = {
    "Bali, Indonesia": "https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0",
    "Paris, France": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34",
    "Cape Town, South Africa": "https://images.unsplash.com/photo-1506459225024-1428097a7e18",
    "Tokyo, Japan": "https://images.unsplash.com/photo-1549692520-acc6669e2f0c"
}

cols = st.columns(2)
for idx, (name, url) in enumerate(destinations.items()):
    with cols[idx % 2]:
        st.image(url, use_column_width=True, caption=name)

footer.render()
