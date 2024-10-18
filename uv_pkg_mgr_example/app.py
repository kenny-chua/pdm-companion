import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time
import resources.text as text

# Initialize session state for page navigation if not already set
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Sidebar for navigation
with st.sidebar:
    st.header("Navigation")
    if st.button("Home"):
        st.session_state.current_page = "Home"
    if st.button("Testimonials"):
        st.session_state.current_page = "Testimonials"

    st.header("About")
    st.markdown("Pybites Development Mindset")

    st.subheader("Useful PDM Links")
    st.markdown(text.useful_links)

    st.subheader("PDM Program Repository")
    st.markdown(text.gh_pdm_links)

    st.subheader("Your Project Repository")
    st.markdown(text.gh_app_links)


# Lottie Animation Loader Function
def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()


# Home Page Function
def home_page():
    with st.container():
        st.title("🔆 PDM Program Companion 🔆")
        st.caption("🎉 Your personal portal to your PDM Program")

        # Thematic Python Code Display
        st.code(text.thematic_code, language="python")

        # Display Lottie Animation
        lottie_animation = load_lottie_url(
            "https://lottie.host/a1493733-00af-4bb1-b7eb-1aa86d9cabf1/TX5XiscOyh.json"
        )
        if lottie_animation:
            st_lottie(lottie_animation, height=100)

        # HTML for Success Message

        st.markdown(text.html_code_block_style, unsafe_allow_html=True)


# Testimonials Page Function
def testimonials_page():
    st.title("Testimonials")
    testimonials = [text.T1, text.T2, text.T3, text.T4, text.T5, text.T6]

    # Display testimonials one at a time, rotating through them
    placeholder = st.empty()
    for _ in range(6):  # Loop for displaying testimonials
        for testimonial in testimonials:
            with placeholder:
                st.markdown(
                    text.testimonial_style.format(testimonial), unsafe_allow_html=True
                )
            time.sleep(2)


# Main Page Rendering Logic
# Use a placeholder to hold the page content and control rendering
page_placeholder = st.empty()

# Render the selected page based on session state
with page_placeholder:
    if st.session_state.current_page == "Home":
        home_page()
    elif st.session_state.current_page == "Testimonials":
        testimonials_page()
