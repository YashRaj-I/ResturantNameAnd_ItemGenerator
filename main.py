import streamlit as st
import restaurant_generator as rg
st.set_page_config(page_title="Restaurant Name Generator", page_icon="🍽️")
st.title("Restaurant Name Generator 🍽️")

cuisine = st.selectbox("Select a cuisine", ["Indian", "Italian", "Chinese", "Mexican", "French", "Japanese", "Thai", "Mediterranean", "American"])

# Load Gemini model
model = rg.configure_gemini(r"C:\Users\Asus\Documents\LLM\GeminiapiKey.env")

if cuisine:
    response = rg.generate_name_and_items(cuisine, model)
    st.header(response[0])
    menu_items = response[1].split(', ')
    # Better code: split menu items and show each on its own line
    menu_items = [item.strip() for item in response[1].split(",")]
    for dish in menu_items:
        st.markdown(f"- {dish}")
