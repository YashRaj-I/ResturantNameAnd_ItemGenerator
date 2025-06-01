# restaurant_generator.py

import google.generativeai as genai
from langchain_core.prompts import PromptTemplate

api_key_path = r"C:\Users\Asus\Documents\RestaurantNameGenerator\GeminiapiKey.env"
from dotenv import load_dotenv
import os

def configure_gemini(api_key_path):
    load_dotenv(api_key_path)
    api_key = os.getenv("API_KEY")
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-1.5-flash')


# Main function to generate restaurant name and menu
def generate_name_and_items(cuisine, model):
    # Prompt to generate restaurant name
    name_prompt = f"I want to open a restaurant for {cuisine} food. suggest a fancy name for it. Only return one name, nothing else."

    # Generate restaurant name
    name_response = model.generate_content(name_prompt)
    restaurant_name = name_response.text.strip()

    # Prompt to generate menu
    menu_prompt = f"suggest a menu for {restaurant_name} restaurant. Only return the menu as comma separated list."
    menu_response = model.generate_content(menu_prompt)
    menu_items = menu_response.text.strip()

    return restaurant_name, menu_items

