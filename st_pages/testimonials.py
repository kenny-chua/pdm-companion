import streamlit as st
import time
import resources.text as text

def testimonials():
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
