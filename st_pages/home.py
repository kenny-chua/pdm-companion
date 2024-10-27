import streamlit as st
from streamlit_lottie import st_lottie
import requests
from resources import text


# Lottie Animation Loader Function
def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


# Home Page Function
def home():
    with st.container():
        st.title("🔆 PDM Program Companion 🔆")
        st.caption("🎉 Your personal portal to your PDM Program")

        # Thematic Python Code Display
        st.code(text.thematic_code, language="python")

        # Display Lottie Animation
        lottie_animation = load_lottie_url("https://lottie.host/a1493733-00af-4bb1-b7eb-1aa86d9cabf1/TX5XiscOyh.json")
        if lottie_animation:
            st_lottie(lottie_animation, height=100)

        # HTML for Success Message
        st.markdown(text.html_code_block_style, unsafe_allow_html=True)
