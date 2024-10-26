import streamlit as st

from st_pages import home, testimonials, pysearch
from resources import text

# Initialize session state for page navigation if not already set
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# Sidebar navigation
with st.sidebar:
    st.header("Navigation")
    if st.button("Home"):
        st.session_state.current_page = "Home"
    if st.button("Testimonials"):
        st.session_state.current_page = "Testimonials"
    if st.button("Pybites Search"):
        st.session_state.current_page = "Pybites Search"

    st.header("About")
    st.markdown("Pybites Development Mindset")

    st.subheader("Useful PDM Links")
    st.markdown(text.useful_links)

    st.subheader("PDM Program Repository")
    st.markdown(text.gh_pdm_links)

    st.subheader("Your Project Repository")
    st.markdown(text.gh_app_links)

# Setting empty page placeholder
page_placeholder = st.empty()

# Page rendering logic
with page_placeholder:
    if st.session_state.current_page == "Home":
        home.home()
    elif st.session_state.current_page == "Testimonials":
        testimonials.testimonials()
    elif st.session_state.current_page == "Pybites Search":
        pysearch.pysearch()
