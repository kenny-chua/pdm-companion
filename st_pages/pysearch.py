import streamlit as st


def pysearch():
    with st.container():
        # Get user input from the text area
        user_input = st.text_area("Please enter your question:")

        # Check if the "Submit" button is clicked
        if st.button("Submit"):
            # Store the user input in session state for later use
            st.session_state['user_input'] = user_input
        else:
            # set the session state to empty if no input is provided
            st.session_state['user_input'] = ""

    return st.session_state['user_input']