import streamlit as st
import restaurant_generator as rg

# Page config
st.set_page_config(page_title="Restaurant Name Generator", page_icon="🍽️")
st.title("Restaurant Name Generator 🍽️")

# Background with dark overlay (for readability)
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(
            rgba(0, 0, 0, 0.6),
            rgba(0, 0, 0, 0.6)
        ), 
        url("https://c.ndtvimg.com/2020-09/if4pp5j8_vegetarian_625x300_30_September_20.jpg");
        background-size: cover;
        background-position: center;
        color: white !important;
    }

    h1, h2, h3, .stSelectbox label, .stMarkdown, p, li, .stText {
        color: white !important;
        text-shadow: 1px 1px 2px black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Cuisine selection
cuisine = st.selectbox("Select a cuisine", [
    "Indian", "Italian", "Chinese", "Mexican",
    "French", "Japanese", "Thai", "Mediterranean", "American"
])

# Load Gemini model
model = rg.configure_gemini("GeminiapiKey.env")

# Generate name and items
if cuisine:
    response = rg.generate_name_and_items(cuisine, model)
    st.header(response[0])
    menu_items = [item.strip() for item in response[1].split(",")]
    for dish in menu_items:
        st.markdown(f"- {dish}")
