import streamlit as st
from play_text import user_inputs
from play_ai import extraction_comparison

st.title("What extraction key word to use?")

extraction_results = extraction_comparison(user_inputs)

# Loop through the results and display each user input with extractions
for result in extraction_results:
    st.subheader(f"Question:\n {result['user_input']}")
    st.markdown("- - -")
    for key, value in result['extractions'].items():
        st.markdown(f"**{key.upper()}:**/n {value}")
    st.markdown("---")
